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

Installing docker on [Solus](https://solus-project.com) was easy enough. I just
had to install the package, and then enable the service:

```
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

```
sudo usermod -a -G docker ryan
```

If the docker group is not created for some reason, it can be added:

```
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

```
docker ps
```

This doesn't always tel the whole story though. Containers might not be running
*all* of the time. They could be stopped, *or* if something fails, it might have
exited. Containers that are stopped or exited won't show up in the default
`docker ps` command. To see *all* of the current containers on the system, run
`ps` with the `-a` flag.

```
docker ps -a
```

#### docker inspect

Another useful command to know when working with docker containers is `docker
inspect`.

```
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

```
docker inspect container_name | grep IPAddress
```

#### help

```
docker images
```

```
docker rm
docker rmi
```

## Images

## Creating Containers

## Running Applications or shells

```
docker rm `docker ps -aq`
```

## Port Forwarding

## Volumes

## In Conclusion 


