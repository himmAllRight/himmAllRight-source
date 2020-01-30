pipeline {
#agent any
    agent {
        docker { image 'fedora:latest' }
    }
//    parameters {
//    }

    stages {
        stage("Setup Deps") {
            steps {
                sh 'whoami'
                sh 'pwd'
                sh 'sudo dnf update -y'
                sh 'sudo dnf install -y hugo python3-pytest'
            }
        }
        stage("Setup Server") {
            steps {
                sh 'ls -lah'
                sh 'pwd'
                sh 'git checkout add-tests'
                sh 'hugo serve &'
            }
        }
        stage("Setup Tests") {
            steps {
                sh 'pip3 install pipenv --user'
                sh 'python3 -m pipenv install'
            }
        }
        stage("Run Tests") {
            steps {
                sh 'python3 -m pipenv run pytest -v .'
            }
        }
    }
}
