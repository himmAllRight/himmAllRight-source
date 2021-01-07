+++
title   = "Create Podman Systemd Services"
date    = "2021-01-07"
author  = "Ryan Himmelwright"
image   = "img/posts/selecting-charmeleon-upgrades/mb_header.jpeg"
caption = "Durham, NC"
tags    = ["linux", "podman", "containers", "systemd"]
draft   = "False"
Comments = "True"
+++

I have started to host some services, like [jellyfin](https://jellyfin.org/)
in podman containers on main Linux workstation. However, as there usually
isn't anything I need the computer to be running over night (I run those
services, like our home automation, on a small server), I have also shutting
my computer down when I go to bed. When I boot my computer up the next
morning however, my containers automatically start up, and I *always* forget
to do it. Let's fix that, using systemd.

<!--more-->

## Create the container

In order to create a service for a container, it needs to already be created
and running. This can be accomplished using the `podman run` command. For example, to startup my jellyfin server, I use the following lengthy command:

```bash
podman run --name jellyfin -d -v /home/ryan/Network/jellyfin/config:/config -v /home/ryan/Network/jellyfin/cache:/cache -v /home/ryan/Music:/media/music:ro -v /home/ryan/Videos:/media/videos:ro --net=host --privileged jellyfin/jellyfin:latest
```

It should be noted, that because we will want the container to persist, even
if it is stopped, that the `--rm` flag should not be used when running the
container (I normally use it to keeps things clean, but had to remove it for
this use case).

## Root vs User containers?

The first attempt at this gave me errors and then I realized... systemd was
running as root but the container runs under my username. Once solution could
be to simply run the container as root, but that doesn't feel right. Podman
runs rootless, so I might as well use it!

## Creating the Service File

Then I read an example from [this web page](https://www.redhat.com/sysadmin/podman-shareable-systemd-services).

It reminded me that there's actually a `podman generate systemd` command that
will generate and spit out a service file for a container, so I ran it as
user to generate a systemd service file, which I saved to my user local
systemd location

```bash
podman generate systemd jellyfin >> ~/.config/systemd/user/jellyfin.service
```


## Starting & Enabling the Service

Afterwards, I was able to start the service using the `--user` flag...

```bash
systemctl --user start jellyfin.service
systemctl --user status jellyfin.service
```

## Caveats 

Running as a user service, it doesn't seem like it will start until the user
has logged in. This makes sense, and can be as simple as quickly ssh'ing into
the machine. However, it should be known and worked around if using something
like a WOL startup, as sending the magic packet won't be enough to get the
services up and running.

## Conclusion