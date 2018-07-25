pipeline {
    agent {
	label 'mr-mime'
    }
    stages {
	stage ('build') {
	    steps{
		sh 'hugo -D -F -b "http://ryan-drafts.himmelwright.net"'
	    }
	}
	stage ('deploy') {
            steps{
		sh 'rsync -r "$WORKSPACE/public/" ryan@ponyta:/usr/share/nginx/html/'
            }
	    post {
		success {
		    emailext(
			subject: "${env.JOB_NAME}[${eng.BUILD_NUMBER}] Drafts Pushed to Server!",
			body: """<p>'${env.JOB_NAME} [${env.BUILD_NUMBER}]' Drafts Pushed to Server":</p>""",
			to: "ryan.himmelwright@gmail.com"
		    )
		}
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
