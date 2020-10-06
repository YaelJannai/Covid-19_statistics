#!/usr/bin/env groovy

//Jenkinsfile


pipeline {
    agent {
        docker {
            image 'python:3.8.6'
        }
    }
    parameters {
        string(name: 'Values', defaultValue: 'status', description: '')
    }
    stages {
        stage('Checkout') { // Checkout (git clone ...) the projects repository
            steps {
                git branch: 'main', url: 'https://github.com/YaelJannai/Covid-19_statistics.git'
            }
        }
        stage('Setup') { // Install any dependencies to perform testing - install packages
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh '''
                    pip install Flask
                    pip install Flask_RESTful
                    pip install requests
                    '''
                }
            }
        }
        stage('Run') {
            parallel {
                stage('Server') { // Start the server
                    steps {
                        timeout(time: 3, unit: 'MINUTES') {
                            withEnv(["HOME=${env.WORKSPACE}"]) {
                                sh 'python app.py'
                            }
                        }
                    }
                }
		        stage('Test') { // Run all the queries from input
                    steps {
                        sh 'sleep 2'
                        script {
                            def list = "${params.Values}".tokenize(',')
                            for (int i = 0; i < list.size(); i++) {
                                def item = list[i]
                                sh "curl localhost:5000/${item}"
                            }
                        }
                    }
                }
            }
        }
    }
}
