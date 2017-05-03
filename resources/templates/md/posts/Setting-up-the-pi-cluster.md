{:layout :post
:title  "Setting Up the Pi Cluster"
:date "2017-05-05"
:author "Ryan Himmelwright"
:tags ["Homelab" "Linux" "Cluster" "Devops" "Pi"]
:draft? false
}

I have a Raspberry Pi 2 and Raspberry Pi 3, and a Banana Pi. Some time ago, I constructed a small tower to house my pi devices. Since then, I have additionally acquired a USB charger to properly power them, and some CAT6 cable to connect them all up to a switch. I hope to use them as a mini cluster environment, where I can play and test some of the "Devops" technologies out there. This post will briefly explain the initial setup of [my cluster](../../pages/homelab/#cluster).

<!-- more -->

## Obtaining the OS Images
Before doing anything with the hardware, I had to setup the "hard drives" (micro SD cards) of the pi's so they could boot. 

### Ubuntu for Raspberry PI
After mucking around with Rapsbian and Hypriot for a bit, I decided to just go with just a plain Ubuntu image for the Raspberry Pis. I didn't have anything against these specific OSes, but I am mostly setting up this cluster to simulate what I would do on a real system. For me, that often means using a straight OS like Ubuntu.

Luckily, Canonical makes specific [Ubuntu ARM images](https://wiki.ubuntu.com/ARM/RaspberryPi) for the Raspberry Pi's. I download the 16.04 server version for both the [raspberry pi 2](http://cdimage.ubuntu.com/ubuntu/releases/16.04/release/ubuntu-16.04.2-preinstalled-server-armhf+raspi2.img.xz) and [raspberry pi 3](http://www.finnie.org/software/raspberrypi/ubuntu-rpi3/ubuntu-16.04-preinstalled-server-armhf+raspi3.img.xz). Installing these images is slightly different from other ISOs I've used in the past. It still uses `dd`, but the image is piped from `xzcat`. I imaged the rpi 2 & 3 SD cards using the following commands, respectively:

```
xzcat ubuntu-16.04.2-preinstalled-server-armhf+raspi2.img.xz | sudo dd bs=4M of=/dev/mmcblk0
xzcat ubuntu-16.04-preinstalled-server-armhf+raspi3.img.xz   | sudo dd bs=4M of=/dev/mmcblk0
```

### Armbian
The one issues I have with my Banana Pi compared to the Raspberry Pis, is that it does not have the full support they do with OS images. This is where Armbian comes in.

### Imaging the Disks

### Hardware Setup

### Bootup and Connecting via SSH

### Adding A Sudo User



-- I will likely break this post into several as a series --

# Ansible Post

-- added `ryan` user on rpis, gave sudo permissions     
	- Made ryan able to use sudo without password by adding `ryan ALL=(ALL) NOPASSWD: ALL` to the bottom of my `visudo` file.

-- setup ssh keys

-- install python on rpis (bpi was okay)

-- install on host (was already on solus)


# Ceph Post Notes?