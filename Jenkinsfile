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
                sh 'sudo yum install -y hugo python36-pytest'
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
                sh 'python3 -m pipenv run pytest -v --junit-xml himmallright-source-test-report.xml .'
            }
        }
        stage("Collect Test Resuts") {
            steps {
                archiveArtifacts "himmallright-source-test-report.xml"
            }
        }
    }
}
