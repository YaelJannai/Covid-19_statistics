#!/usr/bin/env groovy

/**
 * Jenkinsfile
 */

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
                    script {
                        echo 'curl localhost:5000/status'
                        sh 'python app.py'
                        sh 'curl "https://disease.sh/v3/covid-19/historical/israel?lastdays=30"'
                    }
                }
            }
            post {
                always {
                    script {
                        echo 'curl localhost:5000/status'
                        sh 'curl "https://disease.sh/v3/covid-19/historical/israel?lastdays=30"'
                    }
                }
            }
        }
    }
}
