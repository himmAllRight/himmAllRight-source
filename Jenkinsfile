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
		sh 'rsync -r $WORKSPACE/himmAllRight.github.io/* ryan@ponyta:/usr/share/nginx/html/'
            }
	}   
    }
}
