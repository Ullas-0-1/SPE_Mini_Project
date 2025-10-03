pipeline {
    agent any

    environment {
        
        DOCK_HUB_CREDENTIALS_ID = 'dockerhub-creds'
        
    
        DOCKER_IMAGE_NAME = 'ullas474/scientific-calculator'
    }

    stages {
        stage('Checkout') {
            steps {
            
                git branch: 'main', url: 'https://github.com/Ullas-0-1/SPE_Mini_Project.git'
            }
        }

        stage('Test') {
            steps {
                script {
                    //running the tests inside a python docker container
                    docker.image('python:3.9-slim').inside('-u root') {
                        sh 'pip install -r requirements.txt'
                        sh 'pytest app'
                    }
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    // building docker image
                    def customImage = docker.build(DOCKER_IMAGE_NAME)

                    //logging into docker hub and pushing the image
                    docker.withRegistry('https://registry.hub.docker.com', DOCK_HUB_CREDENTIALS_ID) {
                        customImage.push("latest")
                    }
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                // deploying the application using ansible playbook
                sh 'ansible-playbook deploy.yml'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check console output for errors.'
        }
    }
}