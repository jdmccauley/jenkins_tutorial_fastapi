pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('test') {
            withPythonEnv('python3') {
                sh 'pip3 install pytest'
                sh 'pytest'
            }
        }
    }
}