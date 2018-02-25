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

<a href="../../img/posts/docker-quickstart/docker-ps.png"><img src="../../img/posts/docker-quickstart/docker-ps.png" style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;" alt="Docker ps" /></a>


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


#### docker inspect

<a href="../../img/posts/docker-quickstart/docker-inspect.png"><img src="../../img/posts/docker-quickstart/docker-inspect.png" style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;" alt="Docker Search output" /></a>

Another useful command to know when working with docker containers is `docker
inspect`.

``` bash
docker inspect container_name
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

<a href="../../img/posts/docker-quickstart/docker-help.png"><img src="../../img/posts/docker-quickstart/docker-help.png" style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;" alt="Docker help" /></a>

Last but not least, don't forget about the `help` command. To see all the
different docker commands, just run `docker help`. Each command 


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

<a href="../../img/posts/docker-quickstart/docker-images.png"><img src="../../img/posts/docker-quickstart/docker-images.png" style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;" alt="docker images and docker rmi" /></a>

``` bash
docker image rm image_name
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

Similarly, a container can be stopped with `docekr stop`, or restarted with
`docker restart`.

Instead of using a `docker create` and `docker start` combination, `docker run`
can be used to both instantiate *and* start a container. For example, to create
and start the "web-test" container from the previous section:

```
docker run --name web-test -d nginx:latest
```



#### Cleaning containers

<a href="../../img/posts/docker-quickstart/docker-rm.png"><img src="../../img/posts/docker-quickstart/docker-rm.png" style="max-width: 100%; float: left; width: 95%;" alt="Docker rm all images" /></a>

Over time, old containers may build up in the system. To remove an old (not
running) container, use `docker rm` with either the container name, *or* the id.
Note, to easily delete *all* of the containers on the system, `docker rm` can be
fed the output of `docker ps -aq`, where the `-aq` flag returns a list of all
the container ids. (Note: this doesn't work in my Fish shell).


## Attaching to Containers

After a container is running, it might be necessary on occasion to attach to it,
and poke around inside of a shell. There is the obvious way to do this, `docker
attach`, and sort-of work-around way which I prefer to use, `docker exec`.

<a href="../../img/posts/docker-quickstart/docker-attach.png"><img src="../../img/posts/docker-quickstart/docker-attach.png" style="max-width: 100%; float: left;" alt="Docker attach example" /></a>
<div class="caption">An example using the docker attach command</div>

The attach command works as one would expect. It is a command to "Attach local
standard input, output, and error streams to a running container". This is all
well an great except for one issue: when exiting the attached container, the
*container also* exits.

<a href="../../img/posts/docker-quickstart/docker-exec-bash.png"><img src="../../img/posts/docker-quickstart/docker-exec-bash.png" style="max-width: 100%; float: left;" alt="Docker exec bash example" /></a>
<div class="caption">An example using docker exec with a bash shell, as an alternative to docker attach</div>

A way to get around this is by utilizing the `docker exec` command, which allows
a command to be executed inside a container. Executing a shell program, such as
`bash`, provides a similar experience to attaching the container, with the
benefit that after exiting, just the shell exits, and *not* the entire
container, making it my preferred method.


## Ports & Volumes 

Docker containers can be built and run using many specific commands to tailor
the container and how it interacts with the host system. There are two in
particular I want to just briefly touch in this *quick start* post. Those two
options, are `ports` and `volumes`.

#### Ports

<a href="../../img/posts/docker-quickstart/nginx-firefox-port.png"><img src="../../img/posts/docker-quickstart/nginx-firefox-port.png" style="max-width: 100%; float: center;" alt="Container ports can be forwarded to the host's ports." /></a>
<div class="caption">Container ports can be forwarded to the host's ports.</div>

While it is nice to spin up a web server inside a docker container, it isn't
always very useful to only have it available to the host machine. Using the `-p`
flag when running a container, container ports can be bound to ports on the host
system.

<a href="../../img/posts/docker-quickstart/docker-port.png"><img src="../../img/posts/docker-quickstart/docker-port.png" style="max-width: 100%; float: center;" alt="Creating an nginx container, forwarding port 80 to he host's 8081" /></a>
<div class="caption">Creating an nginx container, forwarding it's port 80 to the host's port 8081</div>

Using `-p` with just a single number, as in `-p 8080`, that port of the
container is exposed. To bind ports to the host use two port numbers seperated
with a `:`. The first number is the host port to bind to, and the second is the
container port to expose and forward.

```
docker run -itd --name webtest -p 8081:80 nginx:latest
```

The above command, for example, runs a nginx container with port 80 forwarded to port
8081 on the host. As a result, any computer connecting to port 8081 of the host
machine will be directed to the container nginx web server.


#### Volumes

<a href="../../img/posts/docker-quickstart/nginx-firefox-volume.png"><img src="../../img/posts/docker-quickstart/nginx-firefox-volume.png" style="max-width: 100%; float: center;" alt="Nginx container with website pages in a volume from the host." /></a>
<div class="caption">Containers can attach volumes from the host system for persistent data.</div>

Lastly, by design docker containers are expendable. They are run, and then
thrown away. It should not be assumed that *any* data inside the container will
be preserved by default. That is, unless
[volumes](https://docs.docker.com/storage/volumes/) are used. 

<a href="../../img/posts/docker-quickstart/docker-volume.png"><img src="../../img/posts/docker-quickstart/docker-volume.png" style="max-width: 100%; float: center;" alt="Creating an nginx container, forwarding port 80 to he host's 8081" /></a>
<div class="caption">Creating an nginx container, forwarding it's port 80 to the host's port 8081</div>

Docker volumes are the preferred mechanism for preserving data across container
runs, and are specified using the `-v` flag. Similar to setting ports, volumes
can be created by providing either a single path, or two separated by a `:`.
When a single path is provided, as in `-v /Data`, docker will create a volume
and bind it to that location within the container. Two locations can be provided
to bind a directory on the host system, to the volume inside to container. 

```
docker run -d --name testsite -v /home/ryan/testsite/:/usr/share/nginx/html nginx:latest
```

In the above command, for example, `-v
/home/ryan/testsite/:/usr/share/nginx/html` will use the `/home/ryan/testsite/`
directory of the host system as a volume located at `/usr/share/nginx/html`,
inside the container. As a result, the website files on the host system, are
server by the containerized nginx web-server.


## In Conclusion 


