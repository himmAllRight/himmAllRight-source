+++
title   = "PIA Interfering with Podman Containers"
<<<<<<< HEAD
date    = "2020-08-23"
author  = "Ryan Himmelwright"
image   = "img/posts/pia-client-podman-issues/grass_jamesville_mirror.jpeg"
caption = "U.S. Route 64, Jamesville, NC"
=======
date    = "2020-08-20"
author  = "Ryan Himmelwright"
image   = "img/posts/pytest-parallel-website-tests/mushroom.jpeg"
caption = "Durham, NC"
>>>>>>> 0d7b72f30efea2c48bce832d1a6580b39f9e5f40
tags    = ["linux", "network", "containers", "fedora",]
draft   = "True"
Comments = "True"
+++

Intro about suddenly not being able to start my podman containers...
- Went to work on previous post
- Toolbox container wouldn't start

<!--more-->

## Podman Broken?

- All podman containers wouldn't start
- It worked fine on my freshly-installed laptop...
    - There was a newer podman version on it, so I waited for the update to hit
        my desktop
    - Didn't fix the problem

```sh
podman start website
Error: unable to start container "f8ab31d42b9d04d051b23c65604e19748a9496f17bd3baab8e6f947eee8f3692": creating cgroup directory `/sys/fs/cgroup/net_cls/user.slice/user-1000.slice/user@1000.service/user.slice/libpod-f8ab31d42b9d04d051b23c65604e19748a9496f17bd3baab8e6f947eee8f3692.scope/container`: No such file or directory: OCI runtime command not found error
```


## The Issue

- Searched all over online for potential issues that sounded similar
- I eventually found [this reddit
post](https://www.reddit.com/r/Fedora/comments/hqbo34/podman_cgroup_issues_on_f32/) which sounded like what I was experencing.
- I *had* installed the PIA client a few days prior, to try it out again to
    determine if it's worth renewing my service.
- Sure enough, it had grabbed ownership of my `net_cls` files:
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


## Removing PIA Client

- I removed the client
- At first I couldn't find the un-install option, but eventually found it
    buried in the settings
- After removing it, the `piavpn` group went away...kinda

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

- ... but it still didn't work!

## ... Don't forget to Reboot!

- I started the machine
- It worked XD

## Conclusion
- That was pain and quite difficult to troubleshoot.
- Some people report loading the openvpn profiles and using those works fine.
    It's just the client that breaks the containers
- Regardless I decided to not renew my subscription. I wasn't using it anymore
    anyway, and this little issue didn't make me want to keep it any more.
