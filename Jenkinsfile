pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                pip install pytest==8.3.2 \
                            pytest-html==4.1.1 \
                            pytest-metadata==3.1.1 \
                            selenium==4.23.1
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed. Please check the logs for details.'
        }
    }
}
