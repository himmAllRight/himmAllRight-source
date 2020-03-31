+++
title  = "Creating Tests For This Website: Docker Jenkins Nodes"
date   = "2020-03-31"
author = "Ryan Himmelwright"
image  = "img/posts/creating-website-tests-docker-nodes/pnc-arena-parking-lot.jpeg"
caption = "PNC Arena (Parking Lot), Raleigh NC"
tags   = ["website", "hugo", "dev", "python", "testing", "jenkins", "docker"]
draft  = "False"
Comments = "True"
+++

Okay, quick post! Previously, I wrote about how I [automated my website
tests](/post/creating-website-tests-ci/) using Jenkins. When I wrote that post,
I just had the tests run on `any` node. However, I *wanted* to have the tests
run inside fedora docker container nodes, but ran into issues configuring it.
With the problem long fixed, I decided I would write a quick update post about
switching the pipeline to use docker container nodes.

<!--more-->


### Why Switch

When I first defined the pipeline, I had it use `any` node for the agent:

```groovy
pipeline {
    agent any

    stages {

        // This is where the stages will be defined //

    }
}
```

This just runs the job on any available node, which for me was just the same VM
server I was running Jenkins on. This was fine, but for testing I want to make
sure *everything* in my automation is configured and up to date, and the best
way to do that is with *clean* runs.

Running the pipeline inside a container ensures a clean run by spinning up a
new container to run the pipeline in, and destroying it after the run. This
means all packages and dependencies *must* be defined correctly, or the run will
fail. This is what we want.


<center>
<a href="/img/posts/docker-quickstart/docker-logo.png">
<img alt="Docker Logo" src="/img/posts/docker-quickstart/docker-logo.png" style="float: right; max-width: 100%; width:400px; padding: 5px 15px 10px 10px"/></a>
</center>

### Using Docker Nodes

When switching to using docker nodes, the first thing is to make sure `docker`
is installed on whatever machines Jenkins want to use for nodes. I won't cover
this as it can be different for every user (and I already had `docker`
installed on my Jenkins host).

With docker installed, next make sure the Jenkins server has the [Docker
Slaves](https://plugins.jenkins.io/docker-slaves/) (and possibly [Docker
Pipeline](https://plugins.jenkins.io/docker-workflow/)) plugin(s) installed.

Lastly, with some docker plugins enabled, switch the `agent` statement to use a
container image. I choose to use the `fedora:31` image:

```groovy
pipeline {
    agent {
        docker {
            image 'fedora:31'
        }
    }
    ... // rest of the pipeline
}
```


### Fixing root/sudo error

When I first set the pipeline to use the fedora image, it kept
failing. Specifically, the `sudo dnf` steps would fail because the `sudo`
command didn't exist in the container. If I removed `sudo` from the command...
I didn't have permissions to run `dnf` inside the container ಠ_ಠ (even though the
user is `root`).

After some research, I learned that it wasn't passing the root permissions to
the container, and I could "solve" this issue by providing the the `-u` flag
with `0:0` as an arg to the docker agent:

```groovy
pipeline {
    agent {
        docker {
            image 'fedora:31'
            args '-u 0:0'
        }
    }
    ... // rest of the pipeline
}
```

I don't *love* this solution... but it seems to work.

### Conclusion

That's all I have. Like I said, this was just a quick update about switching my
test nodes to use docker containers. Honestly, I'd much rather try to use
[podman](http://podman.io) containers for my test agents, but I'm sure that
would be much more complicated currently. Maybe in the future...
