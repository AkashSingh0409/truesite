pipeline {
    agent any

    environment {
        IMAGE_NAME = "truesite"
        CONTAINER_NAME = "truesite_container"
        DOCKER_HUB_USER = "your_dockerhub_username"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/AkashSingh0409/truesite.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'npm test' // Modify this if your project has test scripts
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh "docker tag $IMAGE_NAME $DOCKER_HUB_USER/$IMAGE_NAME:latest"
                    sh "docker push $DOCKER_HUB_USER/$IMAGE_NAME:latest"
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh """
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                docker run -d -p 3000:3000 --name $CONTAINER_NAME $DOCKER_HUB_USER/$IMAGE_NAME:latest
                """
            }
        }
    }

    post {
        success {
            echo "Deployment Successful!"
        }
        failure {
            echo "Deployment Failed!"
        }
    }
}

