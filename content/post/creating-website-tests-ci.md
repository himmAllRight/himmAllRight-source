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

While I have started using [Gitlab](https://gitlab.com) for more of my projects
recently, I decided to keep my website source hosted on Github for the time
being, so I won't be using Gitlab's CI/CD tools for this. However, I wanted it
to be known that this automation is *very* straight forward and could be easily
accomplished there as well (I tested it out there too).

For this project though, since my website is hosted on Github, and I already
have [my own Jenkins server](/post/extending-vm-hd/) configured... I will be
using a basic Jenkins pipeline. First, we will create the pipeline file to add
to the git repo, and then we will use the pipeline to configure a new
*multi-branch* pipeline in Jenkins.


## Jenkinsfile

First, lets start by creating the Jenkinsfile. Create a new file named
`Jenkinsfile` in the git repo. Next, lets create a new pipeline and get ready
to add stages:

```groovy
pipeline {
    agent any

    stages {

        // This is where the stages will be defined //

    }
}
```

*(Make sure to add the closing `}`'s!)*


### Stages

Now, lets add the stages. A stage is basically a functional chunk of our
pipeline, and will help keep the steps organized, as well as make it easier to
follow while running.

Each of these stages will be listed inside the `stages { .. }` section we
defined, one after the other (In the order I have them listed below!).

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

The first stage is 'Setup Deps'. This stage handles installing any dependencies
our Jenkins node will need installed to run the tests. Our tests will require
`hugo`, `pytest`, and `python3`. It will also require some `pip` packages, but
we will get to that later.

*Note: My current Jenkins node is running CentOS, so my package manager commands
are specific to that. As always, adjust accordingly.*


#### Start Hugo Server

```groovy
stage("Start Hugo Server") {
    steps {
        sh 'hugo serve &'
    }
}
```

With `hugo` installed (and presumably being inside the website's git repo...),
we can start the web server. This is done with `hugo serve`. The `&` is used to
have the server run as a background process, which allows the pipeline to
continue on, without killing the server process.

*Note: Make sure the tests are set to point to `localhost:1313`, as that is
where `hugo` will try to serve the website by default.*


#### Setup Python

```groovy
stage("Setup Tests") {
    steps {
        sh 'pip3 install pipenv --user'
        sh 'python3 -m pipenv install'
    }
}
```

Next, lets setup `python` by installing the packages we need. Here, I use
`pip3` to install `pipenv`. Then I have `pipenv` install the tests' required
python packages, which are defined in the repo's `Pipfile`.

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

Test time. I again utilize `pipenv` here, by having it call the test command
(`pytest -v --junit-xml himmallright-source-test-report.xml .`) so that it runs
in the pipenv virtual environment.

Two things to note here:

- The `--junit-xml` flag defines a xml filename to write the junit test report
    to. This will be used for Jenkins to collect the test results.
- The test command is wrapped between comments `set +e` and `set -e`. This
    allows tests to fail, without triggering a failure in Jenkins, which is
    what we want. This way even if tests fail, we make it all the way through
    collection so we can see *what* tests failed and *why*.

#### Collect Test Results

```groovy
stage("Collect Test Resuts") {
    steps {
        archiveArtifacts "himmallright-source-test-report.xml"
        junit "himmallright-source-test-report.xml"
    }
}
```

Lastly, we archive the junit report xml file as a Jenkins artifact, and then
have `junit` read it. This requires the
[junit](https://plugins.jenkins.io/junit/) plugin.


### Save & Commit

That should be it for the pipeline file! Commit and push it to the git repo,
and we can start working with it in Jenkins!



## Creating a Multi-Branch Pipeline


## Running Pipelines


## Viewing Results


## Conclusion

