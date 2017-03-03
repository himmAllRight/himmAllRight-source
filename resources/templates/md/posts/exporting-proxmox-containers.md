{:layout :post
:title  "Exporting Proxmox Containers"
:date "2017-03-01"
:author "Ryan Himmelwright"
:tags ["Linux" "Proxmox" "lxc"]
:draft? true
}

So the other night when I sat down to finish off some of these posts,
I discovered that for some reason, my Proxmox Web GUI wasn't
loading. I eventually rebooted my server and when it started back up,
I noticed that my VMs and containers hadn't started, and none of the
Proxmox stuff seems to be running. My first concern now is trying to
export my lxc containers. Here is what I did.

<!-- more -->

This will likely be the first post in a series "How I migrated off of
Proxmox".


### Exporting the Container from Proxmox

config file: /var/lib/lxc/###/config
