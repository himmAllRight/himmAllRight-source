{:layout :post
:title  "Setting Up the Pi Cluster"
:date "2017-05-05"
:author "Ryan Himmelwright"
:tags ["Homelab" "Linux" "Cluster" "Pi"]
:draft? false
}

I have a Raspberry Pi 2 and Raspberry Pi 3, and a Banana Pi. Some time ago, I constructed a small tower to house my pi devices. Since then, I have additionally acquired a USB charger to properly power them, and some CAT6 cable to connect them all up to a switch. I hope to use them as a mini cluster environment, where I can play and test some of the "Devops" technologies out there. This post will briefly explain the initial setup of [my cluster](../../pages/homelab/#cluster).

<!-- more -->

# Setting up the OS Images
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

Armbian is a lightweight Debian and Ubuntu based distribution, that provides builds for various ARM devices. Thus the name, *ARM-bian*. One of these many supported devices... is the [banana pi](https://www.armbian.com/banana-pi/). I downloaded the Ubuntu 16.04 Server flavor of Armbian for the Banana PI, and copied it to my micro SD card with the command:

```
sudo dd if=Armbian_5.25_Bananapi_Ubuntu_xenial_next_4.9.7.img  of=/dev/mmcblk0 bs=1M
```

### Hardware Setup

<img src="../../img/posts/Setting-Up-Pi-Cluster/pi-cluster.png" style="width: 40%; float: right; margin: 0px 10px 0px 10px;"/>

After the operating system images have been copied the SD cards, the hardware can be setup. I started by inserting the SD cards into the PIs, being careful to use the correct card with each device. Unlike the Raspberry PIs, the Bananna PI uses a normal SD card instead of a microSD, so I just left it in the converter I used to connect it to my computer when imaging.

After adding the "hard drives", I connected each PI's ethernet port to my network switch. In the future, I'd like to get the cluster it's own mini switch so that I can have the nodes on their own private network, linked to my main network. For now, this works.

Lastly, plug in the power connectors. Pi devices can be very finicky when not properly powered, so it is a good idea to use an USB charging device. I have had trouble in the past with my devices not working correctly due to power (especially the bpi), and I knew it would be an even greater problem with the cluster because I planned to connect a HD to the bpi with a SATA connector. So, I picked up an [Anker Power Port 5](https://www.amazon.com/Anker-Charger-PowerPort-Multi-Port-Samsung/dp/B00VH8ZW02/ref=sr_1_1?ie=UTF8&qid=1493860165&sr=8-1&keywords=Anker+power+port+5) and it has been working great.

Lastly, once nice feature of the banana pi is that it has a 1 GB ethernet port, *and* a SATA connector with power. So, to get this functionality, and most out of the bpi, I ordered [the appropriate SATA connector](https://www.amazon.com/JBtek-Connectors-Banana-Supply-Terminals/dp/B00ZP0L0VS/ref=sr_1_1?ie=UTF8&qid=1493860481&sr=8-1&keywords=banana+pi+sata) off amazon for a few bucks. When it arrived, I connected it to the SATA and SATA power ports on the pi, and then to an old 300GB laptop HD I had laying around (it was the drive that came with [kadabra](../introducing-kadabra/)). After the drive was connected, running `lsblk` on the bpi showed a `/dev/sda`device, in addition to the typical `mmcblk0` microSD device. I then mounted the drive to a folder using the following command to test it out:

```
sudo mount /dev/sda1 Data
```

After mounting the drive, I was able to browse the contents of all the crap that was still on it. The combination of the GB network and the addition of the HD makes the bpi a great little storage node, which is how I intend to use it.

### Bootup and Connecting via SSH

When the Pis are plugged in, they should automatically boot up. In order to connect to them, I found their IPs from my main computer using `nmap`:

```
sudo nmap -sP 192.168.1.0/24
```
<div id="caption">This command may differ depending on your network setup</div>

The Raspberry PIs have `(Raspberry Pi Foundation)` in the MAC address lines, and my Banana Pi had `bananapi` in the host name. Once I have the IP addresses, I can ssh in using the default usernames and passwords for the images (user/pass should be listed on the sites). After logging in for the first time, each PI prompted prompted me to change the password.

### Adding A Sudo User

When connecting to remote devices, I don't like to be logged in as root, so the first thing I did was to setup a sudo account on the two Raspberry Pis (Armbian actually prompted me through these steps the first time I logged into the Banana pi. Kudos to them).

To add the user, set it's password (important), and then add it to the sudo group, I used the following commands:

```
useradd -m -s /bin/bash ryan
passwd ryan
usermod -a -G sudo ryan
```
<div id="caption">Yes, I know I can add the user to the sudo group in the `useradd` command., but I prefer to do it with `usermod`. Personal Preference.</div>

That's it. At this point, all of my the PIs are minimally set up accessible. The next steps include updating packages, setting up ssh keys, and configuring .... [Ansible](https://www.ansible.com). But that will all be in the *next post*.