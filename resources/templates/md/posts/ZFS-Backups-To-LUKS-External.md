{:layout :post
:title  "ZFS Snapshot Backups to an External Drive with LUKS"
:date "2017-04-19"
:author "Ryan Himmelwright"
:tags ["Homelab" "ZFS" "Linux"]
:draft? false
}

I have had [my server](../../pages/homelab/) running [zfs](https://en.wikipedia.org/wiki/ZFS) data pools to store my data for some time now. However, I am ashamed to admit that I do not have a *true* backup system in place. I attempted to setup this system in the past, but had an issue and let it drift to the side. That changes now.

<!-- more -->

![Server and External Drives](../../img/posts/ZFS-Backups-To-LUKS-External/drives.png")

***Screenshot of current zfs Pools list?***

***Picture of Ninetale's Drive Caddies?***

Currently, my server is configured with 2 main zfs mirrored pools.  The first one, `Data`, is a 2.72 TB usable pool housed on 2 x 3TB hard drives,  and contains all of my wife's and my data, organized into sub-catigory pools (ex: `Data/Music`, `Data/Pictures`, `Data/ryan`, etc). The second, `Backups`, is a 928 GB usable pool on the 2 x 1TB hard drives from my old desktop. It stores the automatic backups of some of the VMs and LXC containers on the server.

Back before I even had my 3TB drives, I bought a 2TB external hard drive to backup the 1TB drives to. While it isn't as large as the total usable space on my server, it is enough to store my data backups to, for the time being.

My plan is to setup a zfs pool on the external drive so, that I can send bi-weekly incremental snapshots to it using zfs's send & receive functions. When I am not running the backups, I want to store the drive at an off-site location. Storing the external drive elsewhere, I want to make sure the data is protected, so I will be encrypting the drive with [LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup), the Linux disk encryption software.

### Setting up LUKS

[LUKS](https://gitlab.com/cryptsetup/cryptsetup/blob/master/README.md) (Linux Unified Key Setup) is the standard for Linux disk encryption. I will use it to encrypt the external drive, and then present the LUKS mapper devices to ZFS as a block device. To do this, we need to first install `cryptsetup` with `sudo apt-get install cryptsetup` (Assuming you are on a Debian-based operating system). Once that is installed, we can setup LUKS on the drive.

The cryptsetup tool has a plethora of settings and options. After researching around, I decided use the options the author of [this post](http://www.makethenmakeinstall.com/2014/10/zfs-on-linux-with-luks-encrypted-disks/) used, because they did something very similar to what I want to do. I setup LUKS on my external drive using the following command:


```
cryptsetup luksFormat --cipher aes-xts-plain64 --key-size 512 --iter-time 10000 --use-random -y /dev/sdf
```
`--cipher aex-xts-plain64`and `--key-size 512` refer to the algorithm and key size used to encrypt the data. In general, the larger the key, the harder the encryption is to crack.

`--iter-time 10000` and `--use-random -y` are additional precautions to make it more difficult to crack the encryption. The `--iter-time 10000` means it will spend at least 10 seconds processing the passphrase each time the disk is unlocked. This makes it much harder to brute-force the passphrase. 

Once the device is encrypted, we need to unlock it and map it as a device. This is done using the command:

```
sudo cryptsetup luksOpen /dev/sdf sdf-enc
```

`/dev/sdf` is the external disk, and `sdf-enc` is whatever you want to name the unlocked device. This is the name that what will be used to when referring to the unlocked device. Now that the drive is encrypted and unlocked, it's time for some ZFS.

### Creating a ZFS Pool


### Taking & Sending a Snapshot

![Taking a ZFS snapshot](../../img/posts/ZFS-Backups-To-LUKS-External/snapshot.gif)

The first time I did this, it had only copied my `Data` snapshot, and not any of the children ones (`Data/Music`, `Data/Pictures`, etc). After some digging around in the docs and online I found that I needed to add the `-R` to my `zfs send` command.

### Incremental Backups
note: So I got this working. The first thing was that I remembered that the `zfs send` `-i` (and `-I`) tag needs two items following it: the starting snapshot, and the one it is increment to.

The second issue I got was that it said my destination had been changed since last snapshot. I looked this up and sometimes just looking around the pool can change files, so I set my backup pool to be read only. Not sure if this will help in the future or not, but we'll see.

```sudo zfs set readonly=on externalBackup```

I still had the error, so I added the `-F` flag to the `zfs recv` command. We'll see if that works. I also thought about rolling back to the snapshot, and then copying which is likely a safer method. I'll let this finish and then write about it...

### Summary
