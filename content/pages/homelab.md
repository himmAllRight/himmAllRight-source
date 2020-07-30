---
title: "Homelab"
date: 2020-07-30
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

<a href="../../img/homelab/home-office.jpeg"><img alt="My Desk" src="../../img/homelab/home-office.jpeg" width=100%></a>
<div class="caption">My Home Office</div>

<a href="../../img/homelab/desk.jpeg"><img alt="Home Office" src="../../img/homelab/desk.jpeg" width=100%></a>
<div class="caption">My Desk</div>

<a href="../../img/homelab/office-entrance.jpeg"><img alt="My Desk" src="../../img/homelab/office-entrance.jpeg" width=100%></a>
<div class="caption">Entrance to  Home Office</div>

### Linux Computers

<a href="../../img/homelab/charmeleon-guts.jpeg"><img alt="My Desk" src="../../img/homelab/charmeleon-guts.jpeg" width=100%></a>
<div class="caption">My workstation, Charmeleon</div>

#### - Charmeleon (Linux Workstation/VM Host/Gaming Computer)
```
Ryzen 5 2600 [3.4 GHz (3.9GHz Turbo), 6 Cores, 12 Threads)
MSI B450 Tomahawk Motherboard
32 GB (2x16GB) DDR4-3200 Mhz RAM
Sapphire Radeon Pulse RX 580 8GB GPU
500 GB Samsung 970 EVO NVME SSD
500 GB Samsung 850 EVO SATA SSD
EVGA SuperNOVA G4 650w 80+ Gold, fully modular PSU
Fractal Design Meshify C Dark TG ATX Mid Tower Case
2 x Noctua NF-A14 PWM 140mm Fans
1 x Noctua NF-F12 PWM 120mm Fan
Fedora 32 (KDE Plasma)
*Connected to Periphery devices
```
<a name="kadabra"></a>
#### - Kadabra (Linux Laptop)
```
T470 Thinkpad
Intel i5-7200u [2.5 GHz (3.1 GHz Turbo), 2 Cores, 4 Threads]
16 GB RAM
250 GB Samsung EVO SSD
14" 1920x1080 IPS Display
Fedora Silverblue 32
*Can Connect to Periphery devices via Thunderbolt 3 Dongle
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
*Can Connect to Periphery devices via Thunderbolt 3 Dongle
```

<a name="Ivysaur"></a>
#### - Ivysaur (Tablet)
```
10.5" iPad Pro
64 GB Storage
* Can be used as a secondary display for Venusaur
```

<a name="bulbasaur"></a>
#### - Bulbasaur (Phone)
```
iPhone 11
64 GB Storage
```

<a name="periphery"></a>
### Periphery Devices
```
Dell 27" 2560x1440 IPS Monitor (Dell u2717d)
Happy Hacking Keyboard Pro2
Audioengine A2+ Speakers & Stands
Audio Technica M50x Headphones
Blue Yeti Microphone - Backout Edition
Logitech HD Pro Webcam c920 Widescreen
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
HP Micro Server Gen 10
AMD Opteron X3421 APU (4) @ 2.100GHz
8 GB ECC RAM
250 GB Samsung EVO SSD (OS + LVM Virtual Disk Drive)
2 x 1TB WD 7200 RPM HDD (ZFS Mirror, for Backups) (Hotswap)
2 x 3TB TOSHIBA 7200 RPM HDD (ZFS Mirror, for Storage) (Hotswap)
Ubuntu Server 18.04
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

