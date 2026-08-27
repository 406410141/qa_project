pipeline {
    agent any

    environment {
        CI = 'true'
        PATH = "/opt/homebrew/bin:${env.PATH}"
    }

    stages {

        // ==========================================
        // 0. Clean
        // ==========================================
        stage('0. Clean') {
            steps {
                echo '=== Clean Previous Test Results ==='

                sh '''
                    rm -rf allure-results
                    rm -rf playwright-testing/allure-results
                    rm -rf playwright-testing/playwright-report
                    rm -rf playwright-testing/test-results
                '''
            }
        }

        // ==========================================
        // 1. Checkout
        // ==========================================
        stage('1. Checkout') {
            steps {
                echo '=== Checkout Source Code ==='
                checkout scm
            }
        }

        // ==========================================
        // 2. Setup Environment
        // ==========================================
        stage('2. Setup Environment') {
            steps {
                echo '=== Setup Python Environment ==='

                sh '''
                    python3 -m venv venv

                    . venv/bin/activate

                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''

                echo '=== Setup Playwright Environment ==='

                sh '''
                    cd playwright-testing

                    npm ci

                    npx playwright install --with-deps
                '''
            }
        }

        // ==========================================
        // 3. Run Automated Tests
        // ==========================================
        stage('3. Run Tests') {

            parallel {

                // ----------------------------------
                // API Tests
                // ----------------------------------
                stage('API Tests') {
                    steps {
                        script {

                            echo '=== Execute API Testing ==='

                            def status = sh(
                                script: '''
                                    . venv/bin/activate

                                    pytest api-testing/test_case/ \
                                        -v \
                                        --alluredir=allure-results/api
                                ''',
                                returnStatus: true
                            )

                            if (status != 0) {
                                currentBuild.result = 'UNSTABLE'
                            }
                        }
                    }
                }

                // ----------------------------------
                // Python UI Tests
                // ----------------------------------
                stage('UI Tests - Selenium') {
                    steps {
                        script {

                            echo '=== Execute UI Testing ==='

                            def status = sh(
                                script: '''
                                    . venv/bin/activate

                                    pytest ui-testing/tests/ \
                                        -v \
                                        --alluredir=allure-results/ui
                                ''',
                                returnStatus: true
                            )

                            if (status != 0) {
                                currentBuild.result = 'UNSTABLE'
                            }
                        }
                    }
                }

                // ----------------------------------
                // Playwright Tests
                // ----------------------------------
                stage('UI Tests - Playwright') {
                    steps {
                        script {

                            echo '=== Execute Playwright Testing ==='

                            def status = sh(
                                script: '''
                                    cd playwright-testing

                                    npx playwright test
                                ''',
                                returnStatus: true
                            )

                            if (status != 0) {
                                currentBuild.result = 'UNSTABLE'
                            }
                        }
                    }
                }
            }
        }

        // ==========================================
        // 4. K6 Performance Testing
        // ==========================================
        stage('4. K6 Performance Tests') {

            steps {
                script {

                    echo '=== Execute K6 Performance Testing ==='

                    def status = sh(
                        script: '''
                            cd performance-testing

                            set +e

                            echo "=== Create Booking Test ==="
                            k6 run create_booking.js
                            s1=$?

                            echo "=== Spike Testing ==="
                            k6 run spike_testing.js
                            s2=$?

                            echo "=== Stress Testing ==="
                            k6 run stress_testing.js
                            s3=$?

                            echo "=== Merge K6 Reports ==="
                            node merge_reports.js

                            if [ $s1 -ne 0 ] || [ $s2 -ne 0 ] || [ $s3 -ne 0 ]; then
                                exit 1
                            fi
                        ''',
                        returnStatus: true
                    )

                    if (status != 0) {
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }

            post {
                always {

                    echo '=== Archive K6 Report ==='

                    archiveArtifacts(
                        artifacts: '''
                            performance-testing/index.html,
                            performance-testing/report_data/**
                        ''',
                        allowEmptyArchive: true
                    )

                    publishHTML(
                        target: [
                            allowMissing: true,
                            alwaysLinkToLastBuild: true,
                            keepAll: true,
                            reportDir: 'performance-testing',
                            reportFiles: 'index.html',
                            reportName: 'K6 Performance Report'
                        ]
                    )
                }
            }
        }

        // ==========================================
        // 5. Generate Combined Allure Report
        // ==========================================
        stage('5. Allure Report') {

            steps {

                echo '=== Generate Combined Allure Report ==='

                allure(
                    includeProperties: false,
                    jdk: '',
                    results: [
                        [path: 'allure-results/api'],
                        [path: 'allure-results/ui'],
                        [path: 'playwright-testing/allure-results']
                    ]
                )
            }
        }
    }

    // ==========================================
    // Post
    // ==========================================
    post {

        always {

            echo '=== Archive Test Artifacts ==='

            archiveArtifacts(
                artifacts: '''
                    allure-results/**,
                    playwright-testing/playwright-report/**,
                    playwright-testing/test-results/**
                ''',
                allowEmptyArchive: true
            )
        }

        success {
            echo '=== All Tests Passed ==='
        }

        unstable {
            echo '=== Some Tests Failed - Build Marked UNSTABLE ==='
        }

        failure {
            echo '=== Pipeline Failed ==='
        }
    }
}