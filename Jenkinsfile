pipeline {
    agent any

    environment {
        CI = 'true'
        PATH = "/opt/homebrew/bin:${env.PATH}"
    }


    stages {
        stage('0. Clean') {
            steps {
                echo '=== Clean Allure Result ==='
                sh 'rm -rf allure-results || true'
            }
        }

        stage('1. Checkout') {
            steps {
                checkout scm
            }
        }

        stage('2. Setup Python') {
            steps {
                echo '=== Build venv  ==='
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('3. Run Tests (Parallel)') {
            parallel {
                stage('API Tests') {
                    steps {
                        script {
                            echo '=== Excute API Testing ==='
                            def status = sh(
                                script: '''
                                . venv/bin/activate
                                pytest api-testing/test_case/ -v --alluredir=allure-results/api
                                ''',
                                returnStatus: true
                            )
                            if (status != 0) currentBuild.result = 'UNSTABLE'
                        }
                    }
                }

                stage('UI Tests') {
                    steps {
                        script {
                            echo '=== Excute UI Testing ==='
                            def status = sh(
                                script: '''
                                . venv/bin/activate
                                pytest ui-testing/tests/ -v --alluredir=allure-results/ui
                                ''',
                                returnStatus: true
                            )
                            if (status != 0) currentBuild.result = 'UNSTABLE'
                        }
                    }
                }
            }
        }

        stage('4. K6 Performance Tests') {
            steps {
                // 🔧 修改：原本是三個獨立的 sh 步驟，改成包在同一個 script + returnStatus 裡
                // 原因：原本寫法只要 create_booking.js 的 threshold 沒過（exit code 非 0），
                // Jenkins 會立刻讓這個 stage 失敗、直接跳過 spike/stress 和 merge_reports.js，
                // 導致你三個測試沒跑完、報告也產生不出來，跟 API/UI Tests 的「容錯後繼續、標記 UNSTABLE」邏輯不一致
                script {
                    echo '=== Execute K6 Performance Testing ==='
                    def status = sh(
                        script: '''
                        cd performance-testing
                        set +e
                        k6 run create_booking.js
                        s1=$?
                        k6 run spike_testing.js
                        s2=$?
                        k6 run stress_testing.js
                        s3=$?
                        node merge_reports.js
                        if [ $s1 -ne 0 ] || [ $s2 -ne 0 ] || [ $s3 -ne 0 ]; then
                            exit 1
                        fi
                        ''',
                        returnStatus: true
                    )
                    if (status != 0) currentBuild.result = 'UNSTABLE'
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'performance-testing/index.html, performance-testing/report_data/**', allowEmptyArchive: true
                    publishHTML(target: [
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'performance-testing',
                        reportFiles: 'index.html',
                        reportName: 'K6 Performance Report'
                    ])
                }
            }
        }

        stage('5. Allure Report') {
            steps {
                echo '=== Gen Report ==='
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results/api'], [path: 'allure-results/ui']]
            }
        }
    }

    post {
        always {
            echo '=== artifacts ==='
            archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
        }
    }
}