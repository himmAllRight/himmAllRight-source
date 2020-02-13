+++
title  = "Switching to a Mesh Network"
date   = "2019-04-01"
author = "Ryan Himmelwright"
image  = "img/posts/switching-to-mesh-network/flower-tree-innovation-train.jpg"
caption= "American Tobacco Campus, Durham NC"
tags   = ["Homelab", "Hardware", "wifi",]
draft  = "False"
Comments = "True"
+++

Not too long ago, I updated our home networking equipment to an Ubiqui
setup. However, we recently moved into a new house and I switched to a
mesh wifi network. No, the switch was not *just* to increase wifi
coverage throughout the entire house. The real motivator
(ironically)... was that I needed a better ethernet connection...

<!--more-->

### History

About two years ago, I [replaced my Linksys wifi
router(s)](/post/upgrading-network-to-ubiquiti/)
with the tiny-but-mighty [Ubiquity Edge Router
X](https://store.ui.com/products/edgerouter-x), paired with an [Ubiqui AP AC
lite](https://www.ui.com/unifi/unifi-ap-ac-lite/) wifi access point. I loved
it. It handled our web traffic flawlessly, and unlike the previous Linksys
routers, I never had to randomly restart it. It just worked for months on end.


<a href="/img/posts/switching-to-mesh-network/google-fiber-box.png"><img alt="The Google Fiber network box" src="/img/posts/switching-to-mesh-network/google-fiber-box.png" style="max-width: 100%;"/></a>
<div class="caption">The Google Fiber "network box".</div>

I enjoyed the setup *so* much in fact, that while I was thrilled to
have a Google Fiber internet connection when we moved to Durham NC
last year, I was a little sad that setting up the edgerouter on the
fiber modem required a little bit of tweaking. I looked into it
but ultimately decided that figuring it out wasn't worth the hassle
for the short period of time which we'd likely live in the
apartment. So, I reluctantly used the Google provided box which worked *okay*.

### We Moved
The Google fiber was indeed short lived, as my wife and I just moved
into a house this past month. When working with Spectrum to setup our
internet (*yea... I know*), we discovered that while there were coax
plugs in both the living room and master bedroom, we couldn't
actually find any hook-ups to connect the house to the external cable/internet
service line.

#### Cable-line in Bedroom
After searching with multiple techs, we decided just to have them
drill a line into the master bedroom (which is at the back of the
house and allows the connection box to be with the other utility
meters). Our house isn't massive, and having the router in the bedroom
works well enough, except for *one* issue.

I have several servers and desktop computers that *require* an
ethernet connection, either because they don't have wifi cards, and/or
because I use Wake-On-Lan with them. This means that I need an
ethernet connection in my office... at the front of the house. Now
that the only ethernet router/switch was in the bedroom, and the rest
of the house relied on wifi...  I needed to figure something out.

#### Power-line Issues
In past apartments, I had used power-line ethernet adapters to extend
ethernet from a router in a different room to my computers. The speeds
weren't great, but then again, neither was our connection so it wasn't
a huge problem. This time though, I ran some tests...


<a href="/img/posts/switching-to-mesh-network/internet-speed-comparison.png">
<img alt="Diagram comparing internet speeds: 1) Plugged directly into Router: 27 ms ping, 231.44 Mbps Download, 11.79 Mbps upload 2) Wifi in Office: 17 ms ping, 178.74 Mbps Download, 11.72 Mbps Upload 3) Powerline Ethernet in Office: 15 ms ping, 17.66 MBps Download, 11.86 Mbps Upload." src="/img/posts/switching-to-mesh-network/internet-speed-comparison.png" style="max-width: 100%;"/></a>

<div class="caption">Different internet Speed test results after hooking up
internet to the house.</div>

So, while it *worked*, this setup wasn't ideal. More importantly, I
found out a few days later there was a massive problem that
*completely prevents* me from being able to use the power-line
adapters. The house's electrical panel is between the master bedroom
and the office, which is the worst case scenario. One day, we turned
on the washing machine and our internet went down. It wasn't just the
power-line connections that were effected... the entire network, wifi
and router was essentially being
[dos'd](https://en.wikipedia.org/wiki/Denial-of-service_attack) by the
washer. When I unplugged the power-line adapters, it worked
again. Power-line was not an option anymore.

#### Mesh Network
I wondered if there was another way to connect ethernet in my office,
beyond having to drop cat6 cable across the house. I looked into wifi
bridges, but most of the devices were designed for large distances,
and ones for home use were not much better than a power-line adapters
when it came to performance/reliability. While looking at wifi
bridges, a thought occurred to me... would a mesh network system work?
If the satellite devices had ethernet ports... maybe.

#### Netgear Orbi

When I started researching wifi mesh networks, the orbi systems were consistently
rated the highest, and people generally reported that they experienced *great*
performance. When I dug further into it, I learned that this high level of performance was
likely due to the orbi's ["tri-band wifi
technology"](https://www.netgear.com/landings/mesh-network/).
Basically, in addition to the normal 2.4 and 5 Ghz network bands, the orbi
system has *a second 5 Ghz band* dedicated to connecting the orbi router and
satilites together. In other words... a dedicated wifi bridge :D.

<a href="/img/posts/switching-to-mesh-network/rbk50.png"><img alt="The RBK50 system comes with 1 router, and 1 satilite
device. Both have 4 etherent ports." src="/img/posts/switching-to-mesh-network/rbk50.png" style="max-width: 100%;"/></a>
<div class="caption">The RBK50 system comes with 1 router, and 1 satilite
device. Both have 4 etherent ports.</div>


I started looking at the orbi hardware and saw that there were several
types of
[satellites](https://www.netgear.com/orbi/products.aspx#filter=.satellites-indoor%2C.satellites%2C.satellites-outdoor%2C.satellites).
Some were just wall plugs, but a few had 2-4 ethernet
ports. Perfect. Realizing this, I ended up ordering the
[RBK50](https://www.netgear.com/orbi/rbk50.aspx) system, which
contained a 4-port orbi router, and a 4-port satellite. My hope was that
I could set up the router in the master bedroom with our modem, and
then put the satellite in my office on the other end of the house.
I could then connect my hardwired devices, or even a network switch, into the
ethernet ports on the satellite. Problem sovled.

#### Conclusion

I have ordered and setup my orbi system, and will write a review post
about it sometime in the future. This post's intention was mostly to
just explain *why* I ended up getting an orbi system.

Many people have started to use home wifi "mesh" systems because they
provide a simple solution to cover an entire house with a strong wifi
connection. While this is a great *bonus* I get from having the mesh
system, as this post demonstrates, my *main* purpose for purchasing
the orbi was to be a solid "ethernet over wifi" system in the new
house. So far... it's working great.
