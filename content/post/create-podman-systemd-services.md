+++
title   = "Create Podman Systemd Services"
date    = "2021-01-15"
author  = "Ryan Himmelwright"
image   = "img/posts/create-podman-systemd-services/moss_tree_header1.jpeg"
caption = "Emerald Outback, Beech Mountain, NC"
tags    = ["linux", "podman", "containers", "systemd"]
draft   = "False"
Comments = "True"
+++

On my Linux workstation, I have started to host a
[jellyfin](https://jellyfin.org/) server using podman. I have also started to
shutdown my computer when I go to bed, as all of our important services (ex:
home automation) are hosted on my home server. With that said, there is one
remaining problem with this configuration. When I boot up my computer the
next morning, my containers do not automatically start... and I *always*
forget to start them up myself. Let's fix that, using systemd.

<!--more-->

## Create the container

In order to define a systemd service for a container, the container needs to
already be created and running. The `podman run` command is used to start
a new container. For example, to run my jellyfin server, I used the
following command:

```bash
podman run --name jellyfin -d -v /home/ryan/Network/jellyfin/config:/config -v /home/ryan/Network/jellyfin/cache:/cache -v /home/ryan/Music:/media/music:ro -v /home/ryan/Videos:/media/videos:ro --net=host --privileged jellyfin/jellyfin:latest
```

It should be noted, that because we will want the container to persist, even
if it is stopped, the `--rm` flag should *not* be used here. I normally add
this flag to keeps things clean, but had to remove it for the service file.


## Root vs User containers?

Before getting started, I just want to mention user vs. root containers. In my
first attempt to start podman containers with systemd, I hit some errors
and then I realized... *systemd* was running as *root* but the container ran
under my username. For example, running `sudo podman ps -a` didn't list my
container, but `podman ps -a` did.

Once solution could be to switch over and run the container as root using
sudo, but that didn't feel right. A benefit of podman is that it is able to
run rootless, and to not take advantage of that feature would be a shame. So,
I started running the systemd steps as the user, but providing the `--user`
flag and it resolved my issues.


## Creating the Service File

At first, I started creating the systemd service files manually, just as I
have done [in previous
posts](/post/autostarting-application-systemd-service/). Although, after
reading an example in [this
article](https://www.redhat.com/sysadmin/podman-shareable-systemd-services),
I was reminded that there's actually a `podman generate systemd` command.
This command will assemble and output a unit file for a container. I ran
it, and saved the generated service file to my user local systemd location.

```bash
podman generate systemd jellyfin > ~/.config/systemd/user/jellyfin.service
```

Simple! This file could be altered if needed, but after quickly skimming it I
thought it looked good.


## Starting & Enabling the Service

Before starting the service, it is a good idea to have systemd reload the
user unit files:

```bash
systemctl --user daemon-reload
```

Afterwards, I started the service, and checked the status to confirm that the
service started up without issue.

```bash
systemctl --user start jellyfin.service
systemctl --user status jellyfin.service
```

Lastly, I `enabled` the service, again with the `--user` flag so that it
would automatically start on boot:


```bash
systemctl --user enable jellyfin.service
```


## Testing it out

<a href="../../img/posts/create-podman-systemd-services/jellyfin_container.png"><img alt="Auto started Jellyfin serving running in a podman container" src="../../img/posts/create-podman-systemd-services/jellyfin_container.png" style="max-width: 100%;"/></a>
<div class="caption">Jellyfin service running in a podman container auto-started at boot</div>

With the service setup and enabled, I rebooted my computer to test it out.
After booting up, I used `podman ps` to prove that the container was started:

```bash
podman ps -a
```

With the container *running*... I next opened up my web browser to verify that
jellyfin was actually *working*... and it was!


## Caveats

While this solution works for the most part, I did hit two small annoyances:

1. Running as a user service, the service won't start until the
user has logged in. This makes sense, and can be resolved by quickly ssh'ing
into the machine. However, it should be known and worked around if using
something like WOL startup, as sending the magic packet won't be enough to
get the service containers up and running.

2. If something breaks with the container and it has to be reset, the service
file should also be regenerated and replaced. The file references container
`uuid`s, and if that changes, the file needs to reflect that. It's not a big
problem. Containers break and that's okay (remember, they're designed to be
ephemeral). Just remember to remove and regenerate the service file when it
happens.

## Conclusion

When I set out to write this post, I though there would be a bit more to it,
requiring me to create the service file manually. However, I quickly stumbled
on the `podman generate systemd` command and I am glad I did. It is one more
feature to add to the ever-growing list of reasons while I love podman and
the other [container
commandos](https://docs.fedoraproject.org/en-US/fedora-silverblue/_attachments/container-commandos.pdf).
Enjoy!