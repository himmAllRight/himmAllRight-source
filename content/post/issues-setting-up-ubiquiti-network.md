+++
title = "Encountered Issues Setting Up Ubiquiti Network"
date = "2017-06-29"
author = "Ryan Himmelwright"
image = "img/header-images/flooded-slide.jpg"
tags = ["Homelab", "Network", "ubiquiti", "wifi",]
+++

This past weekend, I setup my new ubiquiti network. It actually took up a good
portion of Sunday, because I ran into a few minor issues.
Fortunately/Unfortunately, these issues were mostly because it my first time
configuring this type of setup, and there was a lot of trial and error. The basic
network is now all configured and has been running great. It was a good day and I
learned a lot :). In fact, I am confident that if I had to start over from
scratch, the process would take me about 10-15 minutes. Just to be sure, I'm
 going to quickly jot down the major pain points I experienced my first time around. 

<!-- more -->

## Trouble Connecting to the EdgeRouter-x for Initial Setup
<center>
<img alt="During initial setup, I was connecting the router wrong" src="../../img/posts/ubiquiti-setup-issues/wrong-router-connection.png" width="90%">
</center>
<div id="caption">During initial setup, I was connecting the router wrong</div>

The edgerouter needed to be directly connected to a computer during its initial
setup, to make the EdgeOS configuration wizard accessible. The
instructions clearly stated to connect an ethernet cable from my laptop to the
`eth0/POE` port on the edgerouter, but I guess I didn't believe them.


Instead, I plugged the ethernet cable from my modem into `eth0`, and my computer
to `eth1`. That didn't work. However, once I *properly* connected the devices (and
manually set a static IP on my laptop, `192.168.1.2` for example), I was able to access
the configuration page in my browser via `https://192.168.1.1` (don't forget
the *s* in *https*). Lesson Learned: manuals are (*usually*) not out to get you.

## Setting up POE and Connecting the AP 
This was not actually an issue I encountered, but rather a confusion. I was unsure what the best setup for 
the [POE](https://en.wikipedia.org/wiki/Power_over_Ethernet) hardware was. At 
first, I had the POE adaptor connected between the edgerouter and the AP, 
because I wasn't sure if it could optimally power both devices. I found 
an 
[informative guide](https://www.youtube.com/watch?v=f7FeYsJqotc&list=PLDBkup9c8YMgZaE50hAjP7rbbVriTlyQf&index=1) that 
indicated that the POE adaptor could indeed power both.

```scheme
Modem  --
        |
         --> POE Adaptor --> (*eth0*)  edgerouter-x  (*eth4*) --> AP Lite
        |
Power  --
```
*Digram describing the correct link up*


Once I swapped the cables all around, I had to go into the router
configuration and enable the POE for `eth4`. Afterwards, the AP lit up,
indicating that it was connected and powered.

## Issues linking/configuring the AP
This was the problem I spent the most time on. I had to install the 
configuration software for the Ubiquiti access point, but the "Linux binary" was 
a .deb, and I didn't feel like extracting the contents of the package so that I 
could install it on Solus (yet). So instead, I spun up a few Ubuntu VMs to try 
it out, but I over-looked the fact that VMs on my laptop use a 
different subnet (192.168.**122**. \*) for the virtual network. I had hoped that 
because the VM's network was routed through my laptop, which was connected 
directly to the edgerouter, it would still be able to see the access point. 
Regardless... the AP couldn't see the VM and vice versa. Finally, I admitted 
that the issues were most likely caused by the 192.168.122.* IP address that the VM was 
assigned.

<center>
<img alt="During initial setup, I was connecting the router wrong" src="../../img/posts/ubiquiti-setup-issues/ubuntu.png" width="45%">
<img alt="During initial setup, I was connecting the router wrong" src="../../img/posts/ubiquiti-setup-issues/venomoth.png" width="35%">
</center>
<div id="caption">I spun up a new Ubuntu VM (Venomoth) to host the Ubifi controller</div>

By this point, I had also learned that the Linux software is more of a server
service, and not a GUI desktop application. So, I concluded that spinning up a
dedicated VM on my server to host the wifi controller was worth it. Virtual
machines hosted on my server automatically get configured on the main
subnet, so it also resolved my issue. I was able to detect and configure the
access point immediately. This setup made more sense anyway, as I can always
connect to the AP controller by going to the VM's IP on my browser,  just like I
can with my router.


Well, that was all of my setup "*issues*". There was nothing I would consider to
be an actual *issue*, just some confusions of an Ubiquiti/POE first-timer. Like
I stated earlier, I am sure I could redo the setup in about 15 minutes without any
issues... 10 now that I recorded everything in the post!
