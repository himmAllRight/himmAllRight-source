{:layout :post
:title  "Encountered Issues Setting Up Ubiquiti Network"
:date "2017-06-28"
:author "Ryan Himmelwright"
:tags ["Homelab" "Network" "ubiquiti" "wifi"]
:draft? false
}

This past weekend, I setup the ubiquiti network. It actually ended up taking a
good portion of Sunday, but that is because I ran into a few issues.
Fortunately/Unfortunately these issues were mostly due to it being my first time
configuring this type of setup, so there was a lot of trial and error. The basic
setup of is now all configuring and running great. It was a good day and I
learned a lot :). In fact, I am confident that if I had to start over from
scratch, the process would take me about 10-15 minutes. Just to be sure, I'm
just going to quickly jot down the major pain points I had during my first time
setup.

<!-- more -->

## Trouble Connecting to EdgeRouter-x for Initial Setup
<center>
<img alt="During initial setup, I was connecting the router wrong" src="../../img/posts/ubiquiti-setup-issues/wrong-router-connection.png" width="90%">
</center>
<div id="caption">During initial setup, I was connecting the router wrong</div>

The edgerouter needs to be directly connected to a computer during initial setup
so that the EdgeOS configuration screen can be accessed. The instructions stated
to connect and ethernet cable from my laptop to the `eth0/POE` port on the
edgerouter, but I guess I didn't believe it.


Instead, I plugged the ethernet cable from modem into `eth0`, and I was connected
my computer to `eth1`. That didn't work. However, once I properly connected the
devices, and manually set a static IP on my laptop (ex: `192.168.1.2`), I was
able to access the configuration page in my browser via `https://192.168.1.1`
(don't for get the *s* in *https*). Lesson Learned: manuals are (*usually*) not
out to get you.

## Issues connecting AP/POE
This was not actually an issue I encountered, but rather me not being sure what
the best way to setup the [POE](https://en.wikipedia.org/wiki/Power_over_Ethernet) 
was. At first, I had the POE adaptor connected between the edgerouter and the
AP, because I wasn't sure if it could power both devices with it. I eventually 
found a 
[great guide](https://www.youtube.com/watch?v=f7FeYsJqotc&list=PLDBkup9c8YMgZaE50hAjP7rbbVriTlyQf&index=1)  that confirmed that I could.

<p>
```
Modem  --
        |
         --> POE Adaptor --> (*eth0*)  edgerouter-x  (*eth4*) --> AP Lite
        |
Power  --
```
<div id="caption">Digram describing the correct link up</div>
</p>

Once I swapped that that all around, I just had to go into the router
configuration and enable the POE for eth4, and the AP lit up, indicating that it
was connected and being powered.

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

<center>
<img alt="During initial setup, I was connecting the router wrong" src="../../img/posts/ubiquiti-setup-issues/ubuntu.png" width="45%">
<img alt="During initial setup, I was connecting the router wrong" src="../../img/posts/ubiquiti-setup-issues/venomoth.png" width="35%">
</center>
<div id="caption">I spun up a new Ubuntu VM (Venomoth) to host the Ubifi controller</div>

By this point, I also had learned that the software, is more of a server program
than desktop application on Ubuntu, so I decided to spin up a VM on my server
for it. I thought this might fix my issue because those VMs automatically get
configured on the correct subnet, and I didn't feel like editing my laptop VM.
This made more sense too, because I can run the AP controller as full time
server so I can always connect to it when needed.



That's it for now on notes. I'll eventually clean this up into a quick post 
