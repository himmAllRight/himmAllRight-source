{:layout :post
:title  "ZFS Backups to an External Drive with LUKS"
:date "2017-04-14"
:author "Ryan Himmelwright"
:tags ["Homelab" "ZFS" "Linux"]
:draft? false
}

Today (4/12/17), I worked on setting up my system to backup the zpools on Ninetales to a LUKS encrypted external hard drive. I am still copying files over and want to test inceremental sends/etc, but I plan to write a post on the process as I go. This is the template for that

### Setting up LUKS

### Taking & Sending a Snapshot

The first time I did this, it had only copied my `Data` snapshot, and not any of the children ones (`Data/Music`, `Data/Pictures`, etc). After some digging around in the docs and online I found that I needed to add the `-R` to my `zfs send` command.

### Incremental Backups

### Summary
