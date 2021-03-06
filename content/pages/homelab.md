---
title: "Homelab"
date: 2021-02-17
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

<a href="../../img/homelab/charmeleon_inside.jpeg"><img alt="My Workstation" src="../../img/homelab/charmeleon_inside.jpeg" width=100%></a>
<div class="caption">My workstation, Charmeleon</div>

#### - Charmeleon (Linux Workstation/VM Host/Gaming Computer)
```
Ryzen 9 3900x [3.8 GHz (4.6GHz Boost), 12 Cores, 24 Threads)
Noctua NH-U14s CPU Cooler
Aorus Elite Wifi x570 Motherboard
96 GB (2x16GB, 2x32GB) DDR4-3200 Mhz, CL 16 RAM?
Sapphire Radeon Pulse RX 580 8GB GPU (VM Passthrough GPU)
Sapphire Radeon Pulse RX 550 4GB GPU (Host GPU)
500 GB Samsung 970 EVO NVME SSD (Linux Host Install)
2 TB Samsung 850 EVO SATA SSD (Linux /Data drive)
500 GB Samsung 850 EVO SATA SSD (Windows VM Install)
EVGA SuperNOVA G4 650w 80+ Gold, fully modular PSU
Fractal Design Meshify C Dark TG ATX Mid Tower Case
2 x Noctua NF-A14 PWM 140mm Fans
1 x Noctua NF-F12 PWM 120mm Fan
Fedora 33 (KDE Plasma)
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
Fedora 33 (KDE Plasma)
*Can Connect to Periphery devices via Thunderbolt 3 Dongle
```
### Apple Hardware
<a name="Venusaur"></a>
#### - Venusaur (MacBook)
```
2020 Macbook Air
M1 (8 CPU Cores [4 efficiency, 4 performance], 8 gpu cores)
16 GB RAM
512 GB SSD
13.3" 2560x1600 400 nit IPS "Retina" Display
Fan-less
macOS Big Sur
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
Ergodox EZ Glow w/ Cherry MX Brown Switches
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

#### Vileplume (Macbook)
```
Macbook Pro 13" (2020)
1.4GHz quad‑core 8th‑gen Intel Core i5, Turbo Boost up to 3.9GHz
8 GB 2133MHz DDR3 RAM
256 GB PCIe Flash HD
Intel Iris Plug Graphics 645
13.3” 2560x1600 IPS LED Display (1440x900 scaled)
3.1 Lbs and ~0.6” thick
Apple Magic Keyboard
Mac OS Catalina
```

#### Gloom (Tablet)
```
iPad (6th Gen)
* Can be used as a secondary display for Vileplume
```

#### Oddish (Phone)
```
iPhone 8 Plus
```

#### - Weepinbell (Desktop Laptop)
```
Thinkpad T450s
Intel i5-5300u [2.3 GHz (2.90 GHz Turbo), 2 Cores, 4 Threads]
12 GB RAM
256 GB SSD
14" 1600x900 LED Display
6-Cell Battery
CloudReady (a chromiumos spin)
* Ususally docked to be used as a desktop
```

#### - Periphery
```
Thinkpad Ultra Dock 40A2 (to connect to periphery devices below)
LG 32QK500W, 32" 2560x1440 IPS Monitor
Apple Air Pod Pros
Bose AE2 Headphones
Apple Watch 5
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

