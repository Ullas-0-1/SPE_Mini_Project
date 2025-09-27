pipeline {
    agent any

    environment {
        PYTHON = "/Users/ullas/miniforge3/bin/python3"
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Pull code from GitHub main branch
                git branch: 'main', url: 'https://github.com/Ullas-0-1/SPE_Mini_Project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies from requirements.txt
                sh '${PYTHON} -m pip install --upgrade pip'
                sh '${PYTHON} -m pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Run pytest to validate your calculator functions
                sh '${PYTHON} -m pytest app/tests/test_calculator.py -v'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'All tests passed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check console for details.'
        }
    }
}
