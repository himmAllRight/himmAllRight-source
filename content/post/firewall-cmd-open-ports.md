+++
title   = "Opening Ports with firewall-cmd"
date    = "2020-11-30"
author  = "Ryan Himmelwright"
image   = "img/posts/firewall-cmd-open-ports/emerald-outback-log-header.jpeg"
caption = "Emerald Outback, Beech Mountain, NC"
tags    = ["fedora", "linux", "Homelab", "network",]
draft   = "False"
Comments = "True"
+++

I use a handful containerized services on my workstation.
[Jellyfin](https://jellyfin.org/) and [minecraft
servers](https://github.com/itzg/docker-minecraft-server) are two examples.  Many of these
self-hosted applications require ports to be opened in order to work. However,
I often forget this. While I am getting better about remembering to *open* the ports...
sometimes I forget *how*. Not anymore.
<!--more-->

### The Problem

<a href="../../img/posts/firewall-cmd-open-ports/unable_to_connect.png"><img alt="Firefox unable to connect to a page" src="../../img/posts/firewall-cmd-open-ports/unable_to_connect.png" style="max-width:
100%;"/></a>
<div class="caption">Firefox unable to connect to my hugo page</div>


To reiterate: The problem is simple. The services need a port opened, but my firewall is
blocking it. The solution is just as simple: ~~disable the firewall~~ open the port.

### Determine Zones

Before opening ports, lets first determine what [firewalld
zone](https://www.linuxjournal.com/content/understanding-firewalld-multi-zone-configurations)
to apply the change to. The following command will show all active
zones, and which devices are in each one:

```bash
sudo firewall-cmd --get-active-zones
```

Additionally, I use the next command to help figure out what zone is
my default.
```bash
sudo firewall-cmd --list-all
```

It is usually `public`. The `--list-all` command will also show which ports are already opened
in the `ports` section, so use it to verify that they aren't already opened.

### Opening the Port

<a href="../../img/posts/firewall-cmd-open-ports/hugo_connected.png"><img alt="Firefox connected to a page" src="../../img/posts/firewall-cmd-open-ports/hugo_connected.png" style="max-width:
100%;"/></a>
<div class="caption">Connected to Hugo after opening the port</div>

Lets open that port. Change the port value in the following command to whatever
you need. I used `1313` here to open a port for `hugo`. Remember to also set
the zone to whatever was found in the previous step:

```bash
sudo firewall-cmd --zone=public --add-port=1313/tcp
```

To verify:

```bash
firewall-cmd –-list-ports
```

Afterwards, try connecting to the service again. If it still does not work, it is
possible that additional or different ports may need to be opened.

### Make it Persistant

If everything *does* work, the change can be made persistent by running the same command
again, but this time using the `--permanent` flag:

```bash
sudo firewall-cmd --zone=public --permanent --add-port=1313/tcp
```

### Reload

When running the command with the `--permanent` flag from the start, the changes
might not take affect until firewalld is reloaded. This command should apply the
changes:

```bash
sudo firewall-cmd --reload
```

### Conclusion

That's it. It's a short post, but it's one I will use. I am trying not rage
`sudo systemctl stop firewalld` anymore. This should help with that.
