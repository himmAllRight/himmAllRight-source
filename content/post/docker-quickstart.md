+++
title  = "Quick Start to Docker"
date   = "2018-02-10"
author = "Ryan Himmelwright"
image  = "img/header-images/baltimore-dock-gray.jpg"
tags   = ["DevOps", "Homelab", "Linux", "Containers",]
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

```
docker ps -a
```

```
docker rm `docker ps -aq`
```
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

## Port Forwarding

## Volumes

## In Conclusion 


