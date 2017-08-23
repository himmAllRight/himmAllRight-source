{:layout :post
:title  "Playing with nixOS"
:date "2017-07-27"
:author "Ryan Himmelwright"
:tags ["Linux" "NixOS" "KDE"]
:draft? true
}



So in my quest to get wifi working on Kadabra, I started playing with nixos again...

<!-- more -->

### Reasons for Trying again


#### Declarative, Functional System

#### ZFS support

#### Server use?

### Issues

#### Virtual Machine Support
Things like virt-manager just don't seem to be working well for me.

#### Anything outside the box

This time I have future potential sights in mind... Apparently nixos runs great with zfs on linux...

So, I have currently setup a VM and am trying to get a good base
nixos-configuration started. Once I have that all nice, I think I might try
running it on Kadabra. There, I want to try out some server functionality and
see how that works. For example, I want to set it up to run kvm/qemu, lxc
containers, and test out how it handles zfs data pools. If all works well, it
might be a contender for my proxmox replacement I want to do. If not, Centos7
(or even Debian) are my fallbacks.

Nixos would be cool though....


Welp... I installed it on Kadabra. Working my way though this...

#### Update

I think I am putting Solus on Kadabra too. Nixos was fun, but I don't think now
is the time for it on my Desktop OS. The zfs stuff worked nice, but I had to be
carefull about messing up my system. I acidently had an issue where my nixos
config was linked to a pool and I had boot issues.

I was also never able to successfully get VMs running. I always hit some sort of
issue. Lastly, the final issue I had was paths and packaging were a pain. 

I still think nixos is great, and I will likely use it for simple server VMs.
Webservers would be perfect with this. I also do think it could be my
workstation OS one day, once I learn a little more about. Unfortunately, right
now it doesn't appear that there is enough documentation or community for that
to be easy to do. The project could deff use a boost in that department.

Welp, I'm off to reformat this computer. I may still turn this into a "my test
run with nixos" post or something.
