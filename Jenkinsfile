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
                    bat 'docker build -t truesite .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    bat 'docker run -d -p 9090:80 truesite'
                }
            }
        }
    }
}
