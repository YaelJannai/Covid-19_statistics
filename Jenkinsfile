pipeline {
    agent {
        docker {
            image 'python:3.8.6'
        }
    }
    stages {
        stage('Checkout') { // Checkout (git clone ...) the projects repository
            steps {
                git branch: 'main', credentialsId: 'git_credentials', url: 'https://github.com/YaelJannai/Covid-19_statistics.git'
            }
        }
        stage('Setup') { // Install any dependencies you need to perform testing
            steps {
                script {
                    sh """
                    pip install -r requirements.txt
                    """
                }
            }
        }
        stage('test') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
