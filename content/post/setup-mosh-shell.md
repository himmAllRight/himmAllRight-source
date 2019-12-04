+++
title  = "Setup Mosh"
date   = "2019-11-27"
author = "Ryan Himmelwright"
image  = "img/posts/setup-mosh/north-buchanan-boulevard.jpeg"
caption= "North Buchanan Boulevard, Durham, NC"
tags   = ["linux", "homelab", "ssh", "shell"]
draft  = "True"
Comments = "True"
+++

Ever since I [built my desktop](/post/charmeleon-desktop-design/), whenever I
am working on another, more portable machine, I find myself `ssh` back to the
desktop to work on it remotely. It has the power, and much of my work flow is
in a terminal window, so why not? The only issue I have with `ssh` is that if I
have a spotty internet connection, or if I sleep/suspend my computer while
moving around, my `ssh` session is terminated.
[Tmux](/post/scripting-tmux-workspaces/) and
[tmuxinator](/post/setting-up-tmuxinator/) make this not too much of an issue,
since I can re-attach my session, but I still wish my remote session could be a
bit more seamless. They can be... by using `mosh`.


#### Mosh

<a href="/img/posts/setup-mosh/ponyta-mosh.png">
<img alt="Using mosh to conenct to a server" src="/img/posts/setup-mosh/ponyta-mosh.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">Using `mosh` to connect to one of my servers</div>

[Mosh](https://mosh.org) is a more robust replacement for interactive ssh
terminals. It automatically roams and continues to work even as the computer
switches networks or is put to sleep. It also responds to typing, even on a bad
connection which cuts down on lag. Lastly, it's free and open source software,
licenced under the GPLv3.


#### Mosh Install

Mosh should be in most Linux repos, and is also available on macos or Windows.
For more information on how to install it on your platform, just head over to
the [getting mosh](https://mosh.org/#getting) page. For me, it was a simple
`dnf`/`yum` install to get it on both my laptop and server:

```
sudo dnf install mosh
```

*Note: My centos server required me to first enable the epel repos to get
access to `mosh`. Fedora might also, but I already had it enabled on my
desktop.

```
sudo yum install epel-release -y
sudo yum install mosh -y
```


#### Open Firewall Ports

After I installing `mosh`... it might not work. If so, it is likely due to
needing to first open the required ports. Mosh uses UDP ports 60000-61000 for it's
connections.

*Note: If you want to connect from outside the network, remember to also
forward these ports on the network.*


#### Connect

We should now be able to connect to the server with mosh. Typical connections
look very similar to `ssh`:

```
mosh ryan@centos-server
```

If a specific mosh UDP needs to be specified (for port-forwarding, for example)
use the `-p` flag:

```
mosh -p 1234 ryan@centos-server
```


#### SSH Options

Occasionally, particular ssh options might be required for a mosh connection.
For example, I typically `ssh` home on a particular port, so that my router
knows which VM to transfer me to. Options like this can be passed to `mosh`
using the `--ssh` flag:

```
mosh --ssh="ssh -p 1234" ryan@centos-network
```


#### Conclusion

That's really it. There is a bunch of cool [technical
stuff](https://mosh.org/#techinfo) going on under the hood of mosh, but on the
surface... it is simply useful. To showcase it, I'll leave with two clips
showcasing what happens when I temporary disconnect the network on a ssh vs
mosh session. Enjoy!

