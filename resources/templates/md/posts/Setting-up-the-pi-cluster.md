{:layout :post
:title  "Setting Up the Pi Cluster"
:date "2017-05-05"
:author "Ryan Himmelwright"
:tags ["Homelab" "Linux" "Cluster" "Devops" "Pi"]
:draft? true
}

Some time ago, I constructed a small tower to house my pi devices. I have a Raspberry Pi 2 and 3, and a Banana Pi. Over the months, I have also acquired a USB charger to power them properly, and some ethernet cable to hook them all up to a switch. I hope to use them as a mini cluster environment, where I can play with and test some of the "Devops" technologies out there.

<!-- more -->

## Installing the OS(s)
### Ubuntu for Raspberry PI
After mucking around with Rapsbian and Hypriot for a bit, I decided to just go with just a plain Ubuntu image for the Raspberry Pis. I didn't have anything against these specific OSes, but I am mostly setting up this cluster to simulate what I would do on a real system. For me, that often means using a straight OS like Ubuntu.

Luckily, Canonical makes specific Ubuntu images for the Raspberry Pi 3 & 2.

### Armbian
The one issues I have with my Banana Pi compared to the Raspberry Pis, is that it does not have the full support they do with OS images. This is where Armbian comes in.




-- I will likely break this post into several as a series --

## Management
### Ansible?


## Glusterfs?