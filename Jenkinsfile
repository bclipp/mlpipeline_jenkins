pipeline {
    agent {
        docker { image 'python:3.7-slim-buster' }
    }
    stages {
        stage('clean workspace') {
            steps {
                cleanWs()

            }
        }
        stage('Checkout external proj') {
            steps {
                sh "git clone https://github.com/bclipp/mlpipeline_jenkins.git"
                sh "cd mlpipeline_jenkins/app"
            }
        }
        stage('setup pip'){
            steps{
                sh "pip3 install -r requirements.txt "
            }
        }
        stage('init db') {
            steps {
                sh 'python3 main.py init_db'
            }
        }
        stage('load one year data on tesla into db') {
            steps {
                sh 'python3 main.py upload_ayear_stock'
            }
        }
        stage('grid search for best GMM model and save in AWS S3') {
            steps {
                sh 'python3 main.py search_train_model'
            }
        }
    }
 }