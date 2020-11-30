+++
title   = "Opening Ports with firewall-cmd"
date    = "2020-11-30"
author  = "Ryan Himmelwright"
image   = "img/posts/firewall-cmd-open-ports/emerald-outback-log-header.jpeg"
caption = "Beech Mountain, NC"
tags    = ["fedora", "linux", "Homelab", "network",]
draft   = "True"
Comments = "True"
+++

As I host more container servies like [jellyfin] and [minecraft servers] on my workstation, I constantly need to open ports for those services. I use to frequently try to connect to a service from another machine, only to freak out as to why it wouldn't load in browser when I *knew* it is running. But I'm learning. Now, I *know* it's likely due to a port being blocked... but often forget how to propely open it up. Well, today is the day I level up again... by finally documenting my steps.

<!--more-->

### The Problem

*Image of browser I can't connect to?*

### Determine Zones

Show all active zones and which devices are tied to each one:

```bash
sudo firewall-cmd --get-active-zones
```

What I used to see the zone I should actually use?

```bash
sudo firewall-cmd --list-all
```

### Open Port

*Code to open the port*
```bash
sudo firewall-cmd --zone=public --add-port=1313/tcp
```

### Reload?

*code to reload/restart firewall config*

```bash
sudo systemctl restart firewalld
```

### Make it Persistant

```bash
sudo firewall-cmd --zone=public --permanent --add-port=1313/tcp
```

### Conclusion
