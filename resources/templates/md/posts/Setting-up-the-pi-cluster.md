{:layout :post
:title  "Setting Up the Pi Cluster"
:date "2017-05-05"
:author "Ryan Himmelwright"
:tags ["Homelab" "Linux" "Cluster" "Pi"]
:draft? false
}

I have a Raspberry Pi 2 and Raspberry Pi 3, and a Banana Pi. Some time ago, I constructed a small tower to house my pi devices. Since then, I have additionally acquired a USB charger to properly power them, and some CAT6 cable to connect them all up to a switch. I hope to use them as a mini cluster environment, where I can play and test some of the "Devops" technologies out there. This post will briefly explain the initial setup of [my cluster](../../pages/homelab/#cluster).

<!-- more -->

## Obtaining the OS Images
Before doing anything with the hardware, I had to setup the "hard drives" (micro SD cards) of the pi's so they could boot. 

### Ubuntu for Raspberry PI

After mucking around with Rapsbian and Hypriot for a bit, I decided to just go with just a plain Ubuntu image for the Raspberry Pis. I didn't have anything against these specific OSes, but I am mostly setting up this cluster to simulate what I would do on a real system. For me, that often means using a straight OS like Ubuntu.

Luckily, Canonical makes specific [Ubuntu ARM images](https://wiki.ubuntu.com/ARM/RaspberryPi) for the Raspberry Pi's. I download the 16.04 server version for both the [raspberry pi 2](http://cdimage.ubuntu.com/ubuntu/releases/16.04/release/ubuntu-16.04.2-preinstalled-server-armhf+raspi2.img.xz) and [raspberry pi 3](http://www.finnie.org/software/raspberrypi/ubuntu-rpi3/ubuntu-16.04-preinstalled-server-armhf+raspi3.img.xz). Writting these images is slightly different from other ISOs I've used in the past. It still uses `dd`, but the image is piped through `xzcat`. I imaged the rpi 2 & 3 SD cards using the following commands, respectively:

```
xzcat ubuntu-16.04.2-preinstalled-server-armhf+raspi2.img.xz | sudo dd bs=4M of=/dev/mmcblk0
xzcat ubuntu-16.04-preinstalled-server-armhf+raspi3.img.xz   | sudo dd bs=4M of=/dev/mmcblk0
```

### Armbian

The one issue that I have with my Banana Pi compared to the Raspberry Pis, is that it commonly supported. It is hard to find a bananna pi specific image, and the raspberry pi ones usually do not work. For example, while Canonical linked to Raspberry Pi images, it did not mention the banana pie.  This is where [Armbian](https://www.armbian.com/) comes in.

Armbian is a lightweight Debian and Ubuntu based distribution, that provides builds for various ARM devices. Thus the name, *ARM-bian*. One of these many supported devices... is the [banana pi](https://www.armbian.com/banana-pi/).

### Imaging the Disks

### Hardware Setup

### Bootup and Connecting via SSH

### Adding A Sudo User



