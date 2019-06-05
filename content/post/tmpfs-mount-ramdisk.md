+++
title  = "Creating a RAM Disk with a tmpfs Mount"
date   = "2019-06-05"
author = "Ryan Himmelwright"
image  = "img/posts/tmpfs-mount-ramdisk/wilmington-riverwalk.jpg"
caption= "Riverwalk, Wilmington NC"
tags   = ["Linux", "Hardware", "Filesystems",]
draft  = "False"
Comments = "True"
+++

RAM is fun. If a computer has *extra* memory, it can be used for fun *beyond*
opening extra chrome tabs, or firing up Slack. Want to mount a partition that
is *fast* and can be entirely wiped out just by rebooting? Or are you just
bored (guilty)?  Regardless of the reason, lets create and mount a RAM-disk!

<!--more-->

### RAM disks and tmpfs

Creating a RAM disk in Linux is actually quite easy. Unlike other OS's, it
doesn't require special third-party software or digging deep into the registry.
This is because RAM-based file systems are already heavily used in a Linux system.
Many root sub-directories are actually mounted
[tmpfs](http://man7.org/linux/man-pages/man5/tmpfs.5.html) objects, most
notably `/tmp`. To see some `tmpfs` mounts on a system, `grep` the `df`
command for `tmpfs`:

```bash
➜  ~ df -h | grep tmpfs
devtmpfs                  16G     0   16G   0% /dev
tmpfs                     16G  299M   16G   2% /dev/shm
tmpfs                     16G  2.0M   16G   1% /run
tmpfs                     16G     0   16G   0% /sys/fs/cgroup
tmpfs                     16G  5.9M   16G   1% /tmp
tmpfs                    3.2G  184K  3.2G   1% /run/user/1000
tmpfs                     12G     0   12G   0% /var/ramdisk
```


All the contents of a `tmpfs` filesystem reside in system memory, typically
RAM. This allows file access that is *fast*.  However, like RAM,
`tmpfs` is also *volatile*, meaning it will all be erased if the computer
restarts or shuts down. So don't store anything important in `tmpfs`!


### fstab

The easiest way to add a new 'RAM disk' to our system is by adding it as a new
mount in the `/etc/fstab` file. I'm currently running [Fedora
Silverblue](https://silverblue.fedoraproject.org/), so I had to place it under
`/var/` because I don't have write access elsewhere, but feel free to place
your mount wherever you want. Just **make sure the location exists**, or the
system won't boot correctly when loading the `fstab`. After adding the following line
to `/etc/fstab`, a 10G `tmpfs` 'device' will be mounted at `/var/ramdisk` during
each boot:

```bash
# /etc/fstab
...
tmpfs      /var/ramdisk       tmpfs   rw,nodev,nosuid,size=10G	0  0
```

By default, Linux allocates half the RAM available on the system to a new
`tmpfs` mount. However, I wanted to specify my disk size, so I used the `size`
argument to allocate 10G.


### Mounting

With the `fstab` edited, it is time to mount everything. [The arch wiki
page](https://wiki.archlinux.org/index.php/Tmpfs) cautions *against* running
`mount -a` to mount the new *tmpfs* disks, but that is because any files that
might already be in the directories will be removed during the mount. While
this may be a concern when editing any of the already "naturally occurring" `tmpfs`
mounts on a system (such as `/tmp` and `/run`), our use case is adding a
*new* one. So, we *should* be safe!

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

With the tmpfs mount, how can we be sure it's actually functioning as a
RAM disk? The simplest way to test it is... move some files over to the mount
location and see if it starts to use up RAM!

For my quick test, I quickly copied two large `iso` files to the new mount:

<a href='../../img/posts/tmpfs-mount-ramdisk/ram-disk-usage.gif'>
<img alt="Copied some iso files to ramdisk" src="../../img/posts/tmpfs-mount-ramdisk/ram-disk-usage.png" onmouseover="this.src='../../img/posts/tmpfs-mount-ramdisk/ram-disk-usage.gif'" onmouseout="this.src='../../img/posts/tmpfs-mount-ramdisk/ram-disk-usage.png'" style="max-width: 100%;"/>
</a>
<div class="caption">When copying files to a tmpfs mount, RAM usages increases
by the amount copied.</div>

```bash
sudo cp -r ./*.iso /var/ramdisk/
```

During the copy, I had the gnome `System Monitor` application opened so I could
see if the RAM usage slowly climbed as the files copied... and it did!
Additionally, when I deleted the copied files, the RAM usage went back down.
Looks like everything worked!

### Conclusion

While RAM disks are less useful these days due to faster and faster
storage, they can still be fun. I've placed a full Linux file system in mine,
 `chroot`'ed into it, and ran a full DE with xorg and everything! It was quite
snappy. I also use it as a 'scratch' disk where I can work on a temporary
project and blow it away when I'm done. The options are endless!
