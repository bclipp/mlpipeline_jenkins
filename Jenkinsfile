pipeline {
    agent any
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
        stage('init db') {
            steps {
                sh 'python3 main.py download data'
            }
        }
        stage('load one year data on tesla into db') {
            steps {
                sh 'python3 main.py download data'
            }
        }
        stage('download training data') {
            steps {
                sh 'python3 main.py download data'
            }
        }
        stage('grid search for best model and save it') {
            steps {
                sh 'mvn --version'
            }
        }
    }
 }