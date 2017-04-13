{:layout :post
:title  "ZFS Snapshot Backups to an External Drive with LUKS"
:date "2017-04-14"
:author "Ryan Himmelwright"
:tags ["Homelab" "ZFS" "Linux"]
:draft? false
}

I have had [my server](../../pages/homelab/) running [zfs](https://en.wikipedia.org/wiki/ZFS) data pools to store my data for some time now. However, I am ashamed to admit that I do not have a *true* backup system in place. I attempted to setup this system in the past, but had an issue and let it drift to the side. That changes now.

<!-- more -->

***Screenshot of current zfs Pools list?***

***Picture of Ninetale's Drive Caddies?***

Currently, my server is configured with 2 main zfs mirrored pools.  The first one, `Data`, is a 2.72 TB usable pool housed on 2 x 3TB hard drives,  and contains all of my wife's and my data, organized into sub-catigory pools (ex: `Data/Music`, `Data/Pictures`, `Data/ryan`, etc). The second, `Backups`, is a 928 GB usable pool on the 2 x 1TB hard drives from my old desktop. It stores the automatic backups of some of the VMs and LXC containers on the server.

Back before I even had my 3TB drives, I bought a 2TB external hard drive to backup the 1TB drives to. While it isn't as large as the total usable space on my server, it is enough to store my data backups to, for the time being.

My plan is to setup a zfs pool on the external drive so, that I can send bi-weekly incremental snapshots to it using zfs's send & receive functions. When I am not running the backups, I want to store the drive at an off-site location. Storing the external drive elsewhere, I want to make sure the data is protected, so I will be encrypting the drive with [LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup), the Linux disk encryption software.

### Setting up LUKS

### Taking & Sending a Snapshot

The first time I did this, it had only copied my `Data` snapshot, and not any of the children ones (`Data/Music`, `Data/Pictures`, etc). After some digging around in the docs and online I found that I needed to add the `-R` to my `zfs send` command.

### Incremental Backups

### Summary
