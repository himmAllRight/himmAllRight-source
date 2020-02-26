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


## Multibranch Pipelines

With the `Jenkinsfile` in the repo, we can create the pipeline! Specifically,
we will be creating a mult-branch pipeline. A multi-branch scans a git project,
and creates a separate pipeline for each branch or PR in the repo. This is
beneficial for testing, as it will automatically run the tests when a PR is
created, so we can verify the change won't break before merging into the
`master` branch. Additionally, it lets us make sure we aren't breaking anything
while working in a new branch.


#### Creating the Pipeline

<center>
<a href="/img/posts/creating-website-tests-ci/new-job.png">
<img alt="Creating a new Jenkins Item" src="/img/posts/creating-website-tests-ci/new-job.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">Select Multibranch Pipeline from the new item menu in Jenkins.</div>
</center>

To create a Multi-Branch pipeline, select *New Item* in the menu on the left.
Next, enter a name for the pipeline and select *Multibranch Pipeline* at the
bottom. Click *Ok*.


#### Configuring the Pipeline

<center>
<a href="/img/posts/creating-website-tests-ci/multipipeline-config-options.png">
<img alt="Multibranch pipeline config options" src="/img/posts/creating-website-tests-ci/multipipeline-config-options.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">Configuration options when creating the multibranch
pipeline.</div>
</center>

On the pipelines configuration page, start by filling out the *Display Name*
and *Description* text boxes. Next, go down to *Branch Sources* and click on
*Add source*. My website is currently hosted on Github, so I will select that.
However, select *Git* if your project is hosted on another `git` service.

Add the Repository URL and choose the pipeline Behaviors. The Behaviors define
how the pipeline will split up branches. For example, it can be selected to
only discover branches that are also PRs.

Next, in the *Build Configuration* section, be sure that the *Script Path*
defines the path where the `Jenkinsfile` is located. If it's in the root
directory (and named `Jenkinsfile`), the default should work.

Lastly, select an interval to automatically check the repo for changes in the
*Scan Repository Triggers* section. This step is optional, but I highly
recommend it.

That's all we *need* to setup, but feel free to research more options. I mostly
have defaults selected for the rest. When complete, hit *Save*.


## Running Pipelines

<center>
<a href="/img/posts/creating-website-tests-ci/multibranch-pipeline-overview.png">
<img alt="The multibranch pipeline overview page" src="/img/posts/creating-website-tests-ci/multibranch-pipeline-overview.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">The multibranch pipeline overview page.</div>
</center>

Once the multibranch pipeline is created, it should scan the repo to try to
detect any branches or pull requests that have defined `Jenkinsfile`s. It will
create an job item in the list for each branch/PR it detects (and kick off runs
the first time).

To start runs, select *Scan Repository Now* in the menu on the left, and
it will scan all the branches again looking for changes, and kicking off a
pipeline run for any branch or pr that has changes.

<center>
<a href="/img/posts/creating-website-tests-ci/branch-overview.png">
<img alt="The overview page of a single branch" src="/img/posts/creating-website-tests-ci/branch-overview.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">The overview page of a single branch.</div>
</center>

To manually a specific branch run, click on the branch name to enter the
branch's job overview page. Then, simply click *Build Now* on the left. Once
the run starts, it runs like a normal jenkins job and can be viewed by clicking
the job's run number to the bottom left. The job's progress can then be viewed
on that page, or using *Blue Ocean* (Reccomended).


## Viewing Results


## Conclusion

