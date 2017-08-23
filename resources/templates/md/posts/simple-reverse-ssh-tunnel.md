{:layout :post
:title  "Simple Reverse SSH Tunnels"
:date "2017-08-22"
:author "Ryan Himmelwright"
:tags ["Linux" "SSH" "Homelab" "Network"]
:draft? false
}

This past week, I was on vacation with my family. While I didn't work a *ton* on personal projects, I was able to start up work on my [TunelBeacon](https://github.com/himmAllRight/TunnelBeacon) project again. I will write a full post about that project when I am further along. But basically, it will be a simple GUI to create reverse ssh tunnels, that I can have family and friends startup to provide me support access when they need help. Reverse SSH tunnels are *very* usefull and simple to setup, but can be a bit tricky to figure out at first. So, here's a breif and simple guide on how to easily create reverse tunnels.

<!-- more -->

### SSH Tunnels

A secured shell (SSH) tunnel is an encrypted tunnel, created through a ssh tunnel protocol connection. It can be thought of as a pipe between two computers that data travels through. The pipe is secured, and people outside the pipe can only see that data packages is traveling through it, but cannot read the actual contents of the package. SSH tunnels are used to securely connect between devices, as well as forward ports between devices. For example, if I am hosting a website on port 8081 of my privetly-networked laptop, and I want some friends to temporarily look at it on my private server, I can just forward my port to one on the public server with an ssh tunnel.



### Reverse Tunnels

Reverse tunnels are just like normal ssh tunnels except... well... in reverse. This means I can connect to a remote computer, and have *its* port tunneled to *me*, which can be very handy. I, along with many others, use this mostly for a particular use case: providing easy temporarily ssh access to computers behind a network and/or firewall. For example, lets say I want my internet server to be able to ssh to my laptop. Unless I set up my router to forward ssh traffic to my laptop, I cannot do this. Additionally, I might be at a friends house, office, or other public place where I don't have access to the router controls. So, my laptop doesn't have a public ip, but my server *does*. I can initiate a reverse tunnel from the laptop, which lets the server know how to find the laptop. Once tunneled, I can ssh to a specified local port on the server, and it will tunnel me to the laptop


### Creating The Reverse Tunnel

To create a reverse tunnel, use the `-R` flag. After the flag, provide what I call the "path" of the tunnel. So, the server's port where the tunnel will be found, the host of that port (I almost always use `localhost`), and the port to be tunneled. Lastly, make sure to specifiy the *ip* or *hostname* of the remote computer just like in a typical plain `ssh hostname`.

```
ssh -R remoteport:localhost:localport host
```

```
ssh -R 19999:localhost:22 meowth
```


### Connecting

After setting up the tunnel, the initializing computer can be accessed *from the server* with:

```
ssh -p 19999 localhost
```



### Conclusion