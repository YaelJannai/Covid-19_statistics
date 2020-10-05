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
    parameters {
        string(name: 'Value1', defaultValue: 'status', description: '')
        string(name: 'Value2', defaultValue: 'newCasesPeak?country=spain', description: '')
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
                        sh 'sleep 2'
                        script {
				echo "${params.Value1}"
				echo "${params.Value2}"
                            	sh 'curl localhost:5000/${params.Value1}'
                            	sh 'curl localhost:5000/${params.Value2}'
                        }
                    }
                }
            }
        }
    }
}
