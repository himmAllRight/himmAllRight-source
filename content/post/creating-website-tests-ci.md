+++
title  = "Creating Tests For This Website: CI"
date   = "2020-02-29"
author = "Ryan Himmelwright"
image  = "img/posts/creating-website-tests-pages/pnc-arena.jpeg"
caption = "PNC Arena, Raleigh NC"
tags   = ["website", "hugo", "dev", "python", "testing", "jenkins"]
draft  = "True"
Comments = "True"
+++

In the [last post](/post/creating-website-tests-pages/), I setup some simple
testing to ensure pages were being served correctly. However, the problem is
that I can't trust myself to want to run the tests before merging a branch into
`master`. Luckily, I  can have [Jenkins](https://jenkins.io) do all that
*responsible* stuff for me. In this post, we will take that test framework...
and automate it.

<!--more-->

## What I'm Using/Plan

## Jenkinsfile
### Stages
#### Setup Deps

```groovy
stage("Setup Deps") {
    steps {
        sh 'sudo yum update -y'
        sh 'sudo yum install -y epel-release'
        sh 'sudo yum install -y hugo python36-pytest'
    }
}
```

#### Setup Server

```groovy
stage("Setup Server") {
    steps {
        sh 'hugo serve &'
    }
}
```

#### Setup Tests

```groovy
stage("Setup Tests") {
    steps {
        sh 'pip3 install pipenv --user'
        sh 'python3 -m pipenv install'
    }
}
```

#### Run Tests

```groovy
stage("Run Tests") {
    steps {
        sh '''
            set +e
            python3 -m pipenv run pytest -v --junit-xml himmallright-source-test-report.xml .
            set -e
        '''.stripIndent()
    }
}
```

#### Collect Test Results

```groovy
stage("Collect Test Resuts") {
    steps {
        archiveArtifacts "himmallright-source-test-report.xml"
        junit "himmallright-source-test-report.xml"
    }
}
```


### Creating a Multi-Branch Pipeline


## Running Pipelines


## Viewing Results


## Conclusion

