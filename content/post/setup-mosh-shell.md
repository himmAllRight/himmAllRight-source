+++
title  = "Setup Mosh"
date   = "2019-12-04"
author = "Ryan Himmelwright"
image  = "img/posts/setup-mosh/north-buchanan-boulevard.jpeg"
caption= "North Buchanan Boulevard, Durham, NC"
tags   = ["linux", "homelab", "ssh", "shell"]
draft  = "False"
Comments = "True"
+++

Since [builing my desktop](/post/charmeleon-desktop-design/), whenever I work
on another machine, I usually end up ssh'ing back to it to work remotely. It
has my files, more power, and much of my work flow is done from a terminal
window anyway, so why not?  The only issue I have with `ssh` is that if I have
a spotty internet connection, or if I sleep/suspend my laptop while moving
around, the `ssh` session will occasionally time out.  [Tmux](/post/scripting-tmux-workspaces/)
and [tmuxinator](/post/setting-up-tmuxinator/) make this less of an issue,
since I can re-attach my session, but I still wish my remote sessions were a
bit more seamless. They can be... using `mosh`.


#### Mosh

<a href="/img/posts/setup-mosh/ponyta-mosh.png">
<img alt="Using mosh to conenct to a server" src="/img/posts/setup-mosh/ponyta-mosh.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">Using `mosh` to connect to one of my servers</div>

[Mosh](https://mosh.org) is a more robust replacement for interactive ssh
terminals. It automatically roams and continues to work even as the computer
switches networks or is put to sleep. It also responds to typing, even on a bad
connection, which cuts down on lag. Lastly, it's free and open source software,
licenced under the GPLv3.


#### Mosh Install

Mosh should be in most Linux repos, and is also available on BSD, Mac, Windows,
and basically everything else.  For more information on how to install it on
your platform, head over to the [getting mosh](https://mosh.org/#getting)
page.  For me, it was a simple `dnf`/`yum` install to get it on both my laptop
and
server:

```
sudo dnf install mosh
```

*Note: My centos server required me to first enable the epel repos to get
access to `mosh`. Fedora might also, but I already had it enabled on my
laptop.

```
sudo yum install -y epel-release
sudo yum install -y mosh
```


#### Open Firewall Ports

After installing `mosh`... it might not immediately work. If so, it is likely
due to not having the required ports open. Mosh uses UDP ports 60000-61000 for
it's connections. Enable these ports and optionally restart the firewall,
before trying mosh again.

*Note: If you want to connect from outside the network, remember to also
forward these ports on the network.*


#### Connect

We should now be able to connect to the server using mosh. Typical connections
look very similar to `ssh`:

```
mosh ryan@centos-server
```

If a specific mosh UDP port needs to be specified (for port-forwarding, for example)
use the `-p` flag:

```
mosh -p 1234 ryan@centos-server
```


#### SSH Options

Mosh uses ssh for the initial connection. Occasionally, particular ssh options
might be required in order for mosh to initialize a connection.  For
example, I typically `ssh` home on a particular port, so that my router knows
which VM to transfer me to.  Options like this can be passed to `mosh` using
the `--ssh` flag:

```
mosh --ssh="ssh -p 1234" ryan@centos-network
```


#### Conclusion

That's really it. There is a bunch of cool [technical
stuff](https://mosh.org/#techinfo) going on under the hood of mosh, but on the
surface... it is simply useful. For an even *better* experience with mosh, be
sure to check out tmux. Enjoy!

