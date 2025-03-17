pipeline {
    agent any

    environment {
        IMAGE_NAME = "truesite"
        CONTAINER_NAME = "truesite_container"
        DOCKER_HUB_USER = "akaash19"
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
                sh 'npm install --save-dev jest'
                sh 'npm test'
            }
        }

        stage('Setup Docker') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y docker.io
                    service docker start
                '''
            }
        }

        stage('Build and Push') {
            agent {
                docker {
                    image 'docker:latest'
                    args '-v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            steps {
                sh """
                    docker build -t $IMAGE_NAME .
                    docker tag $IMAGE_NAME $DOCKER_HUB_USER/$IMAGE_NAME:latest
                    docker push $DOCKER_HUB_USER/$IMAGE_NAME:latest
                """
            }
        }

        stage('Deploy') {
            agent {
                docker {
                    image 'docker:latest'
                    args '-v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
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

