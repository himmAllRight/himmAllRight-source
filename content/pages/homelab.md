---
title: "Homelab"
date: 2019-12-08
type: homelab
layout: homelab-page
menu:
  main:
    weight: -100
image: /img/homelab/bookshelves.jpeg
---

This is a page where I maintain the status of the computers in my “Homelab”
(basically the tech in our house).

## Ryan (Me)
Don't mind the mess. Still a work in progress, but I noticed my photos were *very* out of
date. I didn't bother to cleanup before taking these pictures. I will when it's closer to
being 'done'.

<a href="../../img/homelab/home-office.jpeg"><img alt="My Desk" src="../../img/homelab/home-office.jpeg" width=100%></a>
<div class="caption">My Home Office</div>

<a href="../../img/homelab/desk.jpeg"><img alt="Home Office" src="../../img/homelab/desk.jpeg" width=100%></a>
<div class="caption">My Desk</div>

<a href="../../img/homelab/home-office-daylight.jpeg"><img alt="My Desk" src="../../img/homelab/home-office-daylight.jpeg" width=100%></a>
<div class="caption">Entrance to  Home Office</div>

### Linux Computers

#### - Charmeleon (Desktop Workstation)
```
Ryzen 5 2600 [3.4 GHz (3.9GHz Turbo), 6 Cores, 12 Threads)
MSI B450 Tomahawk Motherboard
32 GB (2x16GB) DDR4-3200 Mhz RAM
Sapphire 1024 4GB PULSE Radeon RX 560 GPU
500 GB Samsung 970 EVO NVME SSD
250 GB Samsung 850 EVO SATA SSD
Fractal Design Meshify C Dark TG ATX Mid Tower Case
EVGA SuperNOVA G4 650w 80+ Gold, fully modular PSU
Fedora 30 (Multiple Desktops)
*Connected to Periphery devices
```
<a name="kadabra"></a>
#### - Kadabra (Linux Laptop)
```
T470 Thinkpad
Intel i5-7200u [2.5 GHz (3.1 GHz Turbo), 2 Cores, 4 Threads]
16 GB RAM
500 GB Samsung EVO SSD
14" 1920x1080 IPS Display
Fedora 30 SilverBlue
```
### Interface Devices
<a name="Venusaur"></a>
#### - Venusaur (Mac)
```
2019 16" Macbook Pro
Intel i7-9750H (2.6 GHz (4.5 GHz Turbo), 6 Cores, 12 Threads)
16 GB DDR4 2666 MHz RAM
512 GB SSD
Radeon Pro 5300M GPU
16" 3072x1920 500 nit IPS "Retina" Display
macOS Catalina
*Sometimes connected to Periphery devices via usb-c hub
```

<a name="Ivysaur"></a>
#### - Ivysaur (Tablet)
```
10.5" iPad Pro
64 GB Storage
* Can be used as a secondary display for Venusaur
```

<a name="bulbasaur"></a>
#### - bulbasaur (Tablet)
```
iPhone 11
64 GB Storage
```

<a name="periphery"></a>
##### Periphery
```
Dell 27" 2560x1440 IPS Monitor (Dell u2717d)
Happy Hacking Keyboard Pro2
Audioengine A2+ Speakers & Stands
Audio Technica M50x Headphones
Bose AE2 Headphones
Blue Yeti Microphone - Backout Edition
Logitech HD Pro Webcam c920 Widescreen
Inateck USB 3.0 to SATA Dual-Bay Hard Drive Docking Station
```


## Rebecca (Wife)
<a href="../../img/homelab/rebecca_desk.jpg"><img alt="Rebecca's Desk" src="../../img/homelab/rebecca_desk.jpg" width=100%></a>
<div class="caption">Rebecca's Desk (yes, that is my laptop in the dock)</div>

Even though this is my wife's gear... I'm in charge of managing it all. So I
decided to add it here.

#### - Weepinbell
```
Thinkpad T450s
Intel i5-5300u [2.3 GHz (2.90 GHz Turbo), 2 Cores, 4 Threads]
12 GB RAM
256 GB SSD
14" 1600x900 LED Display
6-Cell Battery
CloudReady (a chromiumos spin)

```

#### - Bellsprout
```
Macbook Air (2014)
Intel i5 (1.4 GHz (2.7 GHz Turbo), 3M Cache, 2 Cores, 2 Threads) ?
4 GB RAM
128 GB PCIe Flash HD
13.3” 1440x900 LED Display
2.96 Lbs and ~0.7” thick
Mac OS Catalina
```

#### - Periphery
```
Thinkpad Ultra Dock 40A2 (to connect to periphery devices below)
LG 32QK500W, 32" 2560x1440 IPS Monitor
Apple Air Pod Pros
Bose AE2 Headphones
```

<a name="servers"></a>
## Servers & Networking

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

<a name="x230"></a>
#### - Abra (Test Laptop/"server")
```
Lenovo x230
Intel i5-3320M [2.6 GHz (3.3 GHz Turbo), 3M Cache, 2 Cores, 4 Threads]
8 GB RAM
120 GB SSD
12.5" HD LED 1366x768 Display
9-Cell Battery
Thinkpad Dock
Whatever disto I'm playing with right now...
```


#### - Networking
```
Netgear Orbi RBK50 Router (In Bedroom)
Netgear Orbi RBK50 Satellite (In Office)
```

#### - UPS
```
CyberPower 1500VA/900W UPS
```

#### - Living Room "TV"
```
LG UD4379-b, 43" IPS UHD (3840x2160px) Monitor
4k Fire TV Stick
Nintendo Switch
```



### Digital Ocean Droplets

#### Pidgey (Nextcloud/Test Cloud Server)

    Digital Ocean KVM Droplet
    1 Core
    1 GB RAM
    20 GB SSD
    Ubuntu 16.04 OS

