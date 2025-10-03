pipeline {
    agent any

    environment {
        // The ID for your Docker Hub credentials in Jenkins
        DOCK_HUB_CREDENTIALS_ID = 'dockerhub-creds'
        
        // Your full Docker image name
        DOCKER_IMAGE_NAME = 'ullas474/scientific-calculator'
    }

    stages {
        stage('Checkout') {
            steps {
                // Gets the latest code from your GitHub repository
                git branch: 'main', url: 'https://github.com/Ullas-0-1/SPE_Mini_Project.git'
            }
        }

        stage('Test') {
            steps {
                script {
                    // This uses a clean Python Docker image to run tests,
                    // ensuring a consistent environment every time.
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
                    // Builds the image using your Dockerfile
                    def customImage = docker.build(DOCKER_IMAGE_NAME)

                    // Logs into Docker Hub and pushes the new image
                    docker.withRegistry('https://registry.hub.docker.com', DOCK-HUB_CREDENTIALS_ID) {
                        customImage.push("latest")
                    }
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                // Executes your Ansible playbook to deploy the container locally
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