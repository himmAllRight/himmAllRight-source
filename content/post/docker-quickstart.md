+++
title  = "Quick Start to Docker"
date   = "2018-02-20"
author = "Ryan Himmelwright"
image  = "img/header-images/baltimore-dock-gray.jpg"
tags   = ["DevOps", "Homelab", "Linux", "Containers", "Docker",]
draft  = true
+++

Over the past few months, and particularly over the holiday season, I've started
to deep dive and play around with some technologies I've had my eye on the last
few years. One such technology, is Docker. While Docker has a massive eco-system
surrounding it, and can take years to truly master, this post will hopefully
help you get up and playing with docker containers in just a few minutes. Lets
get started.

<!--more-->



## Installing Docker

<img src="../../img/posts/docker-quickstart/docker-logo.png" style="max-width: 100%; width: 400px; float: right; margin: 0px 15px 5px 5px;" alt="Docker Logo" />

Installing docker on [Solus](https://solus-project.com) was easy enough. I just
had to install the package, and then enable the service:

``` bash
sudo eopkg it docker
sudo systemctl enable docker
sudo systemctl start docker
```

On other distributions, it may not be in the package manager, or it might be
under a different name. To be sure, check out the community edition
[installation
documentation](https://docs.docker.com/install/linux/docker-ce/fedora/#set-up-the-repository)
for your specific distro.


## Adding User to Docker Group

When I first played with docker a few years ago, I ran everything using `sudo`,
which isn't the best idea. To get around this, a user can simply be added to the
`docker` group in order to run all the docker under that user:

``` bash
sudo usermod -a -G docker ryan
```

If the docker group is not created for some reason, it can be added:

``` bash
sudo groupadd docker
```

*Note: These commands MAY differ based on distro.*

## Some Useful Commands

Before we get too caught up in learning some of the docker basics, lets just go
over a few useful commands that make navigating docker a bit easier.


#### docker ps

First, just like linux has the `ps` command to see running processes, docker has
`docker ps` to see it's created and running containers. To see the currently
running containers, use the basic `docker ps` command:

``` bash
docker ps
```

This doesn't always tel the whole story though. Containers might not be running
*all* of the time. They could be stopped, *or* if something fails, it might have
exited. Containers that are stopped or exited won't show up in the default
`docker ps` command. To see *all* of the current containers on the system, run
`ps` with the `-a` flag.

``` bash
docker ps -a
```

#### docker inspect

Another useful command to know when working with docker containers is `docker
inspect`.

``` bash
docker inspect container_name

## Or ##

docker inspect container_id
```

The `inspect` command will dump out the xml for all the low level information
for the docker container/docker object. The output contains everything about the
container, Full ID, time created, state, volumes, network information...
everything. It can be *extremely* useful to pipe the output of `inspect` to grep
get information about the container. For example, to easily grab the container's
IP address, the following command can be used:

``` bash
docker inspect container_name | grep IPAddress
```

#### help

Last but not least, don't forget about the `help` command. To see all the
different docker commands, just run:

``` bash
docker help
```

Beyond that, when using specific command, `inspect` for example, a description
and possible options can be shown using the `--help` flag:

``` bash
docker inspect --help
```

Just as `man` pages can be extremely useful when working on a Linux system,
`help` is valuable when using docker.




## Images

A docker container is spun up from a docker images. Images can be pulled down
from [Dockerhub](https://hub.docker.com/). To search docker hub from command
line, use the `docker search` command:

``` bash
docker search nginx
```

<a href="../../img/posts/docker-quickstart/docker-search.png"><img src="../../img/posts/docker-quickstart/docker-search.png" style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;" alt="Docker Search output" /></a>
<div class="caption">The search output for nginx images</div>

The search will return a list of the all the public images in order from most to
least stars. When a desired image is found, pull it down using the `docker pull`
command:

``` bash
docker pull nginx:latest
```

<a href="../../img/posts/docker-quickstart/docker-pull.png"><img src="../../img/posts/docker-quickstart/docker-pull.png" style="max-width: 100%; width:100%; float: left; margin: 0px 15px 0px 0px;" alt="Docker Pull output" /></a>
<div class="caption">Pulling the latest nginx image</div>

Docker will then download all the layers for the image. When it completes, it
will be added to the list of local images available for spinning spinning up
docker containers from. To see all of the local images, use the `docker images`
command:

``` bash
docker images
```

To delete an image, use the `docker images rm` command, or my preferred, lazier
command, `docker rmi`:

``` bash
docker image rm image_name

## OR ##

docker rmi image_name
```

Lastly, it should be noted that custom images can be created/tailored by using a
[Dockerfile](https://docs.docker.com/engine/reference/builder/#usage). Once a
Dockerfile is defined, an image can be created from it using the `docker build`
command. For example, the following Dockerfile would use an
[ubuntu](https://hub.docker.com/_/ubuntu/) image for the base, but also update &
install several packages in the images:

``` yaml
# This is a custom ubuntu image with SSH already installed
FROM ubuntu:latest
MAINTAINER himmallright <ryan.himmelwright@gmail.com>

RUN apt-get update

RUN apt-get install -y vim stow git tmux fish htop emacs

```

To build the image, run the following command in the same directory as the
Dockerfile (if defining a specific file, use the `-f` option):

``` bash
docker build -t ubuntu-base:v1 .
```

I like to use the `-t` to specify a `name:tag` for the image, so I can easily
find it in my `docker images` list.

## Creating Containers

Docker containers can be *created* (and not run) with the `docker create`
command. When creating containers, it is useful to use flags to tailor the
details of the container, and, to make it more useful. For example, the `-m`
flag can be used to create a memory limit, `--name` to name it, etc. For
example, to create a simple nginx container:

```
docker create --name web-test nginx:latest
```


## Starting & Running Containers

To *start* a container created with `docker create`, or one that has simply
stopped for some reason, use the `docker start` command. For example, to start
the container created in the previous step:

```
docker start web-test
```

Instead of using a `docker create` and `docker start` combination, `docker run`
can be used to both instantiate *and* start a container.


## Running Applications or shells
```
docker rm `docker ps -aq`
```

## Port Forwarding

## Volumes

## In Conclusion 


