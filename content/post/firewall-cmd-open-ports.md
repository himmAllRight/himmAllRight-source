+++
title   = "Opening Ports with firewall-cmd"
date    = "2020-11-30"
author  = "Ryan Himmelwright"
image   = "img/posts/firewall-cmd-open-ports/emerald-outback-log-header.jpeg"
caption = "Emerald Outback, Beech Mountain, NC"
tags    = ["fedora", "linux", "Homelab", "network",]
draft   = "True"
Comments = "True"
+++

I host more and more containerized services like
[jellyfin](https://jellyfin.org/) and [minecraft
servers](https://github.com/itzg/docker-minecraft-server) on my workstation.
Many of these self-hosted applications require ports to be open to work. I
often forget this. I am getting better about remembering to open the ports...
but now I sometimes forget how. But I am about to fix that too, because after
today, I will have this post to refer to.

<!--more-->

### The Problem

<a href="../../img/posts/firewall-cmd-open-ports/unable_to_connect.png"><img alt="Firefox unable to connect to a page" src="../../img/posts/firewall-cmd-open-ports/unable_to_connect.png" style="max-width:
100%;"/></a>
<div class="caption">Firefox unable to connect to a page</div>

This is a minor issue that isn't complicated at all. Often, I will launch a
service on my Fedora worksation and try to view it remotely and will be
unable to to connect. For example, this often occurs when running `hugo serve`
while working of posts for this website.

The problem is simple. The service need a port opened but my firewall is
blocking it. The solution is just as simple: ~~disable the firewall~~ open the port.

### Determine Zones

Before opening the port, lets first figure out what [firewalld
zone](https://www.linuxjournal.com/content/understanding-firewalld-multi-zone-configurations)
to apply the change to. The following command can be used to show all active
zones and which devices are tied to each one:

```bash
sudo firewall-cmd --get-active-zones
```

I also like to use this command to help me figure out what zone I'm using as my
default.
```bash
sudo firewall-cmd --list-all
```

It's usually `public`.

*Note: the `--list-all` command will also show which ports are already opened
in the `ports` section.*

### Open the Port

<a href="../../img/posts/firewall-cmd-open-ports/hugo_connected.png"><img alt="Firefox connected to a page" src="../../img/posts/firewall-cmd-open-ports/hugo_connected.png" style="max-width:
100%;"/></a>
<div class="caption">Connected to Hugo after opening the port</div>

Now that we know what zone we are in, and that our port isn't opened already,
we can open it with the following command: (change `1313` to your desired port
number)

```bash
sudo firewall-cmd --zone=public --add-port=1313/tcp
```

List ports to check that it was opened:

```bash
firewall-cmd –-list-ports
```

Also, try connecting to the service again. If not, it's possible it might need
additional (or different) ports opened.

### Make it Persistant

If everything work, it can be made persistent by running the same command
again, but using the `--permanent` flag:

```bash
sudo firewall-cmd --zone=public --permanent --add-port=1313/tcp
```

### Reload

If running the command with the `--permanent` flag from the start, the changes
might not take affect until firewalld is reloaded:

```bash
sudo firewall-cmd --reload
```

### Conclusion

That's it. It's a short post, but it's one that I know at least I might get
some use out of. I'm trying to be better person and not rage `sudo systemctl
stop firewalld` anymore. It's not worth it.
