pipeline {
    agent any

//    parameters {
//    }

    stages {
        stage("Setup Deps") {
            steps {
                sh 'whoami'
                sh 'pwd'
                sh 'sudo yum update -y'
                sh 'sudo yum install -y epel-release'
                sh 'sudo yum install -y pipenv hugo'
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
                sh 'pipenv install'
            }
        }
        stage("Run Tests") {
            steps {
                sh 'pipenv run pytest -v .'
            }
        }
    }
}
