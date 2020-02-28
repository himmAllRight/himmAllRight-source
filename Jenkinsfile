pipeline {
    agent any

//    parameters {
//    }

    stages {
        stage("Setup Deps") {
            steps {
                sh 'sudo yum update -y'
                sh 'sudo yum install -y epel-release'
                sh 'sudo yum install -y hugo python36-pytest'
            }
        }
        stage("Start Hugo Server") {
            steps {
                sh 'hugo serve &'
            }
        }
        stage("Setup Python") {
            steps {
                sh 'pip3 install pipenv --user'
                sh 'python3 -m pipenv install'
            }
        }
        stage("Run Tests") {
            steps {
                sh '''
                    set +e
                    python3 -m pipenv run pytest -v --junit-xml himmallright-source-test-report.xml .
                    set -e
                '''.stripIndent()
            }
        }
        stage("Collect Test Resuts") {
            steps {
                archiveArtifacts "himmallright-source-test-report.xml"
                junit "himmallright-source-test-report.xml"
            }
        }
    }
}
