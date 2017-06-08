
{:layout :post
:title  "Setting up A Docker Swarm on the Pi Cluster"
:date "2017-04-29"
:author "Ryan Himmelwright"
:tags ["Homelab" "Pi" "Cluster" "Docker" "Linux"]
:draft? true
}

I have been meaning to setup something on my pi cluster. 


<--! more -->

# Raspberry Pis Setup

# Bananna Pi Setup
I often have troubble to getting images to boot on the bananna pi. Hypriot was no exception to this. So, I wanted to at least try to setup docker on it, even if I had to use a different base image.

Tried installing Bananian Linux, and it worked, but it is [end of life](https://www.bananian.org/news#the_end_-_2017-04-02). On their announement, the bananian team recommended the [armbian](https://www.armbian.com) project, so I tried that. I grabbed the Ubuntu version first (becase why not). It booted up wonderfully, and I loved the little setup sequence they put me through my first time ssh'ing. It had me change my root password, and setup a user account (sudo). After setup, I updated the system, and then installed the `docker.io` package. I am not sure if this is the best way to install docker here, but I couldn't find any better way. Systemd coudn't start the service right away, but I enabled the service:

```
sudo systemctl enable docker
```

and rebooted. When the system came back up, docker was running.

Ran some stuff but the services kept failing and the remote terminals to the nodes eventually got all weird. Decided to reset and try setting something else up on the cluster. I will save this post for maybe in the future though.
