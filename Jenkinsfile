pipeline {
    agent any

    environment {
        CI = 'true'
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
                pip install -r requirement.txt
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

        stage('4. Allure Report') {
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