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
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip3 install --user -r requirements.txt'
                }
            }
        }
        stage('Run') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python app.py'
                }
            }
        }
        stage('Test') {
            steps {
                def response1 = sh 'curl localhost:8080/newCasesPesdf'
                def response2 = sh 'curl localhost:8080/newCasesPeak?country=spain'
                def response3 = sh 'curl localhost:3333/newCasesPeak?country=spain'
                echo response1
                echo response2
                echo response3
            }
        }
    }
}
