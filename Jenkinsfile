pipeline {
    agent {
	label 'mr-mime'
    }
    stages {
	stage ('build') {
	    steps{
		sh 'hugo -DOOM -F -b "http://ryan-drafts.himmelwright.net"'
	    }
	}
	stage ('deploy') {
            steps{
		sh 'rsync -r "$WORKSPACE/public/" ryan@ponyta:/usr/share/nginx/html/'
            }
	}

    }
    post {
	failure {
	    emailext(
		subject: "${env.JOB_NAME}[${eng.BUILD_NUMBER}] Failed!",
		body: """<p>'${env.JOB_NAME} [${env.BUILD_NUMBER}]' Failed!":</p>""",
		to: "ryan.himmelwright@gmail.com"
	    )
	}
    }
}
