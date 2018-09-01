---
title: "Homelab"
date: 2018-09-01
type: homelab
layout: homelab-page
menu: 
  main:
    weight: -100
image: img/homelab/new_monitor1.jpg
---

This is a page where I maintain the status of the computers in my “Homelab”. I will list my current systems here (potentially with screenshots of my current desktop setup for my workstations).

## Computers

### Ryan (Me)

Having recently moved to Durham NC, I built a new standing desk and am
slowly putting my space together. So for now ... don't mind the wires
:P. I'll try to keep updating this page as I progress.

<a href="../../img/homelab/new_monitor2.jpg"><img alt="Ryan's New Desk" src="../../img/homelab/new_monitor2.jpg" width=100%></a>
<div class="caption">My Home Desk</div>

<a href="../../img/homelab/new_monitor3.jpg"><img alt="Ryan's New Desk" src="../../img/homelab/new_monitor3.jpg" width=100%></a>
<div class="caption">My Home Workstation</div>

<a name="kadabra"></a>
#### - Kadabra (Main Laptop)
```
T470 Thinkpad
Intel i5-7200u [2.5 Ghz (3.1 Ghz Turbo), 2 Cores, 4 Threads]
16 GB RAM
500 GB Samsung EVO SSD (LUKS encrypted and using ZFS on the Data partition)
14" 1920x1080 IPS Display 
Fedora 28
```
##### Periphery
```
Thinkpad Ultra Dock 40A2
LG UD4379-b, 43" IPS UHD (3840x2160 px) Monitor
Happy Hacking Keyboard Pro2 
Audioengine A2+ Speakers & Stands
Bose AE2 Headphones
Logitech HD Pro Webcam c920 Widescreen
Blue Yeti Microphone - Backout Edition
Inateck USB 3.0 to SATA Dual-Bay Hard Drive Docking Station
```

<a name="x230"></a>
#### - Abra (Secondary Laptop) 
```
Lenovo x230
Intel i5-3320M [2.6 GHz (3.3 GHz Turbo), 3M Cache, 2 Cores, 4 Threads]
8 GB RAM
120 GB SSD
12.5" HD LED 1366x768 Display
9-Cell Battery
Ubuntu Mate/Kubuntu 18.04
```

### Rebecca (Wife)

#### - Bellsprout (2014)
```
Macbook Air
Intel i5 (1.4 GHz (2.7 GHz Turbo), 3M Cache, 2 Cores, 2 Threads) ?
4 GB RAM
128 GB PCIe Flash HD
13.3” 1440x900 LED Display
2.96 Lbs and ~0.7” thick
Mac OS
```

<a name="servers"></a>
### Servers

<a name="ninetales"></a>
#### - Ninetales (VM Host / Home Server)
```
Lenovo ThinkServer 440
Intel Xeon E3-1225 v3 [3.2 GHz (3.6 GHz Turbo), 8M Cache, 4 Cores, 4 Threads]
20 GB ECC RAM
250 GB Samsung EVO SSD (OS + LVM Virtual Disk Drive)
2 x 1TB WD 7200 RPM HDD (ZFS Mirror, for Backups) (Hotswap)
2 x 3TB TOSHIBA 7200 RPM HDD (ZFS Mirror, for Storage) (Hotswap)
Ubuntu Server 18.04
```

#### - CyberPower 1500VA/900W UPS

#### - Xbox One

<a name="cluster"></a>
### PI Cluster
<img alt="PI Cluster" src="../../img/homelab/pi-cluster.png" width=100%>

#### Node 1
```
BROKEN
Raspberry Pi 3
ARM v8 CPU (1.2 GHz, 4 Cores, 4 Threads)
1 GB RAM
MicroSD card for HD
Ubuntu 16.04 ARM
```

#### Node 2
```
Raspberry Pi 2
ARM Coretx-A7 (900 MHz, 4 Cores, 4 Threads)
1 GB RAM
MicroSD card for HD
Ubuntu 16.04 ARM
```
#### Node 3
```
Banana Pi M1
A20 ARM Cortex-A7 Dual Core (2 Cores, 2 Threads)
1 GB RAM
10/100/1000 Ethernet
MicroSD card for HD
Armbian (Ubuntu 16.04 version)
```


### Digital Ocean Droplets

#### Pidgey (Nextcloud/Test Cloud Server)

    Digital Ocean KVM Droplet
    1 Core
    512 MB RAM
    20 GB SSD
    Ubuntu 16.04 OS

### AWS

*I have also started playing with AWS, but don't have any persistent servers with it yet.*
