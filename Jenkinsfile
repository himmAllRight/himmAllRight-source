pipeline {
    agent any //{
//        docker {
//            image 'fedora:32'
//            args '-u 0:0'
//        }
//    }

    stages {
        stage("Setup Deps") {
            steps {
                sh 'dnf update -y'
                sh 'dnf install -y hugo pytest git which python3-pip'
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
