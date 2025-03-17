pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/AkashSingh0409/truesite.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t truesite .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d -p 8080:80 truesite'
                }
            }
        }
    }
}
