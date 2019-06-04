+++
title  = "Creating a RAM Disk with a tmpfs Mount"
date   = "2019-06-04"
author = "Ryan Himmelwright"
image  = "img/posts/tmpfs-mount-ramdisk/wilmington-riverwalk.jpg"
caption= "Riverwalk, Wilmington NC"
tags   = ["Linux", "Hardware", "Filesystems",]
draft  = "True"
Comments = "True"
+++

Do you have too much RAM on your computer? Or maybe you just want to mount a
partition that is quite *fast*. Or maybe you are just bored (guilty).
Regardless of the reason, creating a RAM-disk might help. Here's how.

<!--more-->

### RAM disks and tmpfs


### fstab

The easiest way to add a new RAM disk to our system is by adding it as a new
item on the `/etc/fstab` file. I wanted to create a persistant RAM mount at
`/var/ramdisk` that I could use whenever I wanted. I'm currently running
[Fedora Silverblue](https://silverblue.fedoraproject.org/), so I had to place
it under `/var/` because I don't have write access elsewhere. Feel free to
place your mount wherever you want. Just *make sure the location exists*, or
the system won't boot correctly when loading the `fstab`.

```bash
# /etc/fstab
...
tmpfs      /var/ramdisk       tmpfs   rw,nodev,nosuid,size=10G	0  0
```

By default, Linux allocates half the RAM available on the system to a new
`tmpfs` mount. However, I wanted to specifiy my disk size, so I took advantage
of using the `size` arguement:


### Mounting

With the `fstab` edited, it is time to mount everything. While [the arch wiki
page](https://wiki.archlinux.org/index.php/Tmpfs) cautions *against* running
`mount -a` to mount the new RAM disk, that is because it is warning that any
files that might already be in the directories will be removed during the
mount. While this is a concern when editing any of the already "natually
occuring" `tmpfs` mounts on the system (such as `/tmp` and `/run`), our use
case is adding a *new* one. So, we should be safe!

```shell
sudo mount -a
```

To verify that the RAM disk is mounted, check the `df` output. (*Note: It
should be empty since it was just allocated*)

```shell
$ df -h
...
tmpfs                     10G     0   10G   0% /var/ramdisk
...
```

### Testing

So with all of this mounted, how can we be sure it's actually functioning as a
RAM disk? The simplest way to test it is... move some files over to the mount
location and see if it starts to use up RAM!

For my quick test, I quickly copied some `iso` files to the new mount:

<a href='../../img/posts/tmpfs-mount-ramdisk/ram-disk-usage.gif'>
<img alt="Copied some iso files to ramdisk" src="../../img/posts/tmpfs-mount-ramdisk/ram-disk-usage.png" onmouseover="this.src='../../img/posts/tmpfs-mount-ramdisk/ram-disk-usage.gif'" onmouseout="this.src='../../img/posts/tmpfs-mount-ramdisk/ram-disk-usage.png'" style="max-width: 100%;"/>
</a>
<div class="caption">When copying files to a tmpfs mount, RAM usages increases
by the amount copied.</div>

```bash
sudo cp -r ~/Music /var/ramdisk/
```

During the copy, I had the gnome `System Monitor` application opened so I could
see if the RAM usage slowly climbed as the files copied... and it did!
Additionally, when I deleted the copied files, the RAM usage went back down.
Looks like everything worked!
