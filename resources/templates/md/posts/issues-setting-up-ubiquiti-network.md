{:layout :post
:title  "Encountered Issues Setting Up Ubiquiti Network"
:date "2017-06-28"
:author "Ryan Himmelwright"
:tags ["Homelab" "Network" "ubiquiti" "wifi"]
:draft? false
}

So today I setup the ubiquiti network. It actually ended up taking the majority
of my day, but that is because I ran into a few issues. Unfortunately these
issues were mostly due to me just being stupid. It was a good day and I learned
a lot :). The basic setup of it all seems to be running great and I am excited
to dig deeper into it all. I'm just going to quickly jot down the major issues I
had so that I can remember then when I go to write about them.

## Trouble connecting to edgerouter-x 
I had the internet connected to eth0, and I was connecting my computer to
eth1. During the initial setup though, you need to connect the laptop/computer
directly to eth0, and configure the laptop to have some static ip (ex:
192.168.1.2). Then I was able to connect.

## Issues connecting AP/POE
I mostly messed this up because I wasn't paying attention and was plugging
them in wrong. I also tried to have the POE adaptor between the router and the
AP because I wasn't sure if it could power both. But then I found a guide and it
confirmed that I could. Once I swapped that that all around, I was able to go
into the router configuration and enable the POE for eth4, and the AP lit up.

```
Modem  --
        |
         --> POE Adaptor --> (*eth0*)  edgerouter-x  (*eth4*) --> AP Lite
        |
Power  --
```
Digram describing the correct link up


## Issues linking/configuring the AP
This was the one I had the biggest issue with. I knew I had to setup the
configuration software, but it was only set for Ubuntu, and I have been running
Solus. So, I spun up a few VMs to try it out. However, I was being dumb and over
looked the fact that they are on a different subnet. I assumed because I was
connecting to them from my host, that was connected directly to the switch It
should be okay, and that the VM should be able to see the AP because it could
see everything else on the network. However... the AP couldn't see the VM which
was the issue, as the AP wasn't being detected. I went on a trail thinking I
needed to change my inform URL, but that wasn't helping.

Eventually, I realized it was likely due to the 192.168.122.* ip that the VMs
are assigned. I realized it earlier, but didn't want to admit that was the
issue...

By this point, I also had learned that the software, is more of a server program
than desktop application on Ubuntu, so I decided to spin up a VM on my server
for it. I thought this might fix my issue because those VMs automatically get
configured on the correct subnet, and I didn't feel like editing my laptop VM.
This made more sense too, because I can run the AP controller as full time
server so I can always connect to it when needed.



That's it for now on notes. I'll eventually clean this up into a quick post 
