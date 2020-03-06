pipeline {
    agent {
        docker {
            image 'fedora:31'
            args '-u 0:0'
        }
    }

//    parameters {
//    }

    stages {
        stage("Setup Deps") {
            steps {
                sh 'dnf update -y'
                sh 'dnf install -y hugo pytest git which'
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
