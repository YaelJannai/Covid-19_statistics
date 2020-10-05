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
            parallel {
                stage('Server') {
                    steps {
                        withEnv(["HOME=${env.WORKSPACE}"]) {
                            sh 'python app.py'
                        }
                    }
                }
		stage('Test') {
                    steps {
                        withEnv(["HOME=${env.WORKSPACE}"]) {
                            	sh 'sleep 2'
				sh 'curl localhost:5000/newCasesPeak?country=spain'
                        }
                    }
                }

            }
        }
    }
}
