pipeline {
    agent {
        docker {
            image 'python:3.8.6'
        }
    }
    stages {
        stage('Checkout') { // Checkout (git clone ...) the projects repository
            steps {
                git branch: 'main', url: 'https://github.com/YaelJannai/Covid-19_statistics.git'
            }
        }
        stage('Setup') { // Install any dependencies you need to perform testing
            steps {
                sh 'pip install flask'
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip3 install --user -r requirements.txt'
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
