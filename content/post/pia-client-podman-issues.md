+++
title   = "PIA Interfering with Podman Containers"
date    = "2020-08-23"
author  = "Ryan Himmelwright"
image   = "img/posts/pia-client-podman-issues/grass_jamesville_mirror.jpeg"
caption = "U.S. Route 64, Jamesville, NC"
tags    = ["linux", "network", "containers", "fedora",]
draft   = "True"
Comments = "True"
+++

Several weeks ago, I woke up and tried to start working on my [previous
post](/post/pytest-parallel-website-tests/), but quickly hit some issues. For
some reason, I was unable to start the
[toolbox](https://docs.fedoraproject.org/en-US/fedora-silverblue/toolbox/)
container I run `hugo` in while working on my website. In fact, I wasn't able
to run *any* of my podman containers.

<!--more-->

## Podman Broken?

Specifically, when I tried to start a container, I encountered this error
message:

```sh
podman start website
Error: unable to start container "f8ab31d42b9d04d051b23c65604e19748a9496f17bd3baab8e6f947eee8f3692": creating cgroup directory `/sys/fs/cgroup/net_cls/user.slice/user-1000.slice/user@1000.service/user.slice/libpod-f8ab31d42b9d04d051b23c65604e19748a9496f17bd3baab8e6f947eee8f3692.scope/container`: No such file or directory: OCI runtime command not found error
```

So I tried podman on a different computer. It worked fine. So, I looked at the
versions and noticed the second computer had a newer version of podman. I
figured it was a bug that must have been fixed, so I waited a day for the
update to hit my desktop (it wasn't available on that machine yet for some
reason.

After a day or so when I ran my updates, the new `podman` was installed, which
I thought would surely fix my issue. It didn't. (ಠ_ಠ)


## The Issue

So, I started to scour the internet again to look for new solutions.
Eventually, I found [this reddit
post](https://www.reddit.com/r/Fedora/comments/hqbo34/podman_cgroup_issues_on_f32/).
While reading it, the poster's issues sounded *very* similar to my own. After
seeing some of the comments linking the [PIA] client to the origonal poster's
issues, I suddenly remembered... I installed PIA client on my machine earlier
that week!

Sure enough, when I checked the ownership of my `net_cls` files (as suggested
in the thread), it looked like `piavpn` was messing with the ownership:

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

Some commenters in the thread stated that they had experienced the same issue,
and that it went away after removing the PIA client.

## Removing PIA Client

So, I decided to remove the PIA client. It wasn't a big loss for me, as I
hadn't used it in months. I only installed it to double check
if it was a service I actually wanted before it renewed itself later in the
month.

At first, I couldn't find the *un*-install option, but eventually found it deep
in the settings. After removing the client the `piavpn` group went away... sort
of. It still had a `1004` gid, which I'm guessing *was* the `piavpn`.

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

Whatever the case... it still didn't work.

## ... Don't forget to Reboot!

I was furious. After calming down, I reasoned it probably wasn't working due to
cruft from the client lingering on my system (like the `1004` group for
example), so I rebooted my syetem... and it worked!

## Conclusion

In conclusion... why did I write this post? This issue was a huge pain to
troubleshoot.
It was only by chance that I stumbled on that reddit post, and would have had
an even *harder* time figuring out the problem without it. I figured having at
least *one* more page stating that podman and the PIA client don't play nice
might help others that hit this issue find the solution quicker.

<center>
![Frustation meme](https://media.giphy.com/media/3rgXBBaVvhPXk3NSnK/giphy.gif)
</center>

It is worth nothing that some people report loading the PIA openvpn profiles
and using them to connect to the VPN works without issue. It's just the client
that breaks the containers. So if you want to still use PIA (I let mine expire.
I just didn't use it anymore), give it a try!
