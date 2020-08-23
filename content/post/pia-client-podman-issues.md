+++
title   = "PIA Client Interfering with Podman Containers"
date    = "2020-08-23"
author  = "Ryan Himmelwright"
image   = "img/posts/pia-client-podman-issues/grass_jamesville_mirror.jpeg"
caption = "U.S. Route 64, Jamesville, NC"
tags    = ["linux", "network", "containers", "fedora",]
draft   = "False"
Comments = "True"
+++

Earlier this month, I woke up and tried to start working on my [previous
post](/post/pytest-parallel-website-tests/), but quickly hit a snag.
I was unable to start the
[toolbox](https://docs.fedoraproject.org/en-US/fedora-silverblue/toolbox/)
container I use while working on my website. In fact, *none* of my podman
containers would start.

<!--more-->

## Was Podman Broken?

Specifically, when I tried to start a container I encountered this error
message:

```sh
podman start website
Error: unable to start container "f8ab31d42b9d04d051b23c65604e19748a9496f17bd3baab8e6f947eee8f3692": creating cgroup directory `/sys/fs/cgroup/net_cls/user.slice/user-1000.slice/user@1000.service/user.slice/libpod-f8ab31d42b9d04d051b23c65604e19748a9496f17bd3baab8e6f947eee8f3692.scope/container`: No such file or directory: OCI runtime command not found error
```

So, I attempted to use  podman on a different computer. It worked fine. I
compared version numbers and noticed that the second computer had a newer
version of podman installed. I figured that I had hit a bug that must now be fixed,
so I waited for the update to reach my desktop (it wasn't available on that
machine yet for some reason).

A day later when I ran my updates, the new version of `podman` was installed, which
I thought would surely fix my problem. It didn't. (ಠ_ಠ)


## The Issue

I started to scour the internet again to look for answers. Eventually, I
found [this reddit
post](https://www.reddit.com/r/Fedora/comments/hqbo34/podman_cgroup_issues_on_f32/).
While reading it, the poster's experience sounded *very* similar to my own.
After reading some of the comments that connected the [private internet
access](https://www.privateinternetaccess.com) client to the original poster's
issues, I suddenly remembered... I had installed the [PIA
client](https://www.privateinternetaccess.com/pages/download) on my machine
earlier that week!

Sure enough, when I checked the ownership of my `net_cls` files (as suggested
in the thread), it looked like `piavpn` was claiming group ownership of the
files:

```shell
➜  ~ ll /sys/fs/cgroup/net_cls
total 0
-rw-r--r--. 1 root piavpn 0 Aug  4 21:21 cgroup.clone_children
-rw-r--r--. 1 root piavpn 0 Aug  4 21:21 cgroup.procs
-r--r--r--. 1 root piavpn 0 Aug  4 21:21 cgroup.sane_behavior
drwxr-xr-x. 6 root root   0 Aug  4 21:21 machine.slice
-rw-r--r--. 1 root piavpn 0 Aug  4 21:21 net_cls.classid
-rw-r--r--. 1 root piavpn 0 Aug  4 21:21 notify_on_release
-rw-r--r--. 1 root piavpn 0 Aug  4 21:21 release_agent
-rw-r--r--. 1 root piavpn 0 Aug  4 21:21 tasks
```

Some commenters in the thread stated that the conflict went away after they
removed the PIA client.

## Removing the PIA Client

As a result, I decided to un-install my PIA client. It wasn't a major loss for
me, as I hadn't used it in months. I only installed it to double check if it
was a service I wanted, or if I should cancel my subscription before it
auto-renewed later that month.

At first, I couldn't find an *un*-install option, but eventually found it deep
in the settings. After removing the client, the `piavpn` group went away... sort
of. It still had a `1004` gid, which I'm guessing *was* the previous `piavpn`
group.

```shell
➜  ~ ll /sys/fs/cgroup/net_cls
total 0
-rw-r--r--. 1 root 1004 0 Aug  4 21:21 cgroup.clone_children
-rw-r--r--. 1 root 1004 0 Aug  4 21:21 cgroup.procs
-r--r--r--. 1 root 1004 0 Aug  4 21:21 cgroup.sane_behavior
drwxr-xr-x. 6 root root 0 Aug  4 21:21 machine.slice
-rw-r--r--. 1 root 1004 0 Aug  4 21:21 net_cls.classid
-rw-r--r--. 1 root 1004 0 Aug  4 21:21 notify_on_release
-rw-r--r--. 1 root 1004 0 Aug  4 21:21 release_agent
-rw-r--r--. 1 root 1004 0 Aug  4 21:21 tasks
```

Whatever the case... podman still didn't work.

## ... Don't forget to Reboot!

I was furious. After calming down, I reasoned it probably still wasn't working
due to cruft from the client lingering on my system (like the `1004` group for
example), so I rebooted my desktop... and it worked!

## Conclusion

In conclusion... why did I write this post? This complication was a huge pain
to troubleshoot.  It was only by chance that I stumbled on that reddit post,
and would have had an even *harder* time without it. I assume having at least
*one* more page on the internet stating that podman and the PIA client don't
play nice, might help others find the solution quicker. Hence, this post.

<center>
![Frustation meme](https://media.giphy.com/media/3rgXBBaVvhPXk3NSnK/giphy.gif)
</center>

Before I end, it is worth nothing that some users reported that configuring the PIA openvpn
profiles and using *them* to connect to the VPN works without issue. It is just
the *client* that breaks containers. So if you want to still use PIA (I let
mine expire. I don't use it enough), give it a try!
