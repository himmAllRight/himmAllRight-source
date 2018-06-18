+++
title   = "Nginx as a Reverse Proxy to Forward Sub-Domains"
date    = "2018-06-22"
author  = "Ryan Himmelwright"
image   = "img/header-images/roger-williams-park-leaves1.jpg"
caption = "Roger Williams Park, Providence RI"
tags    = ["Linux", "Homelab", "Network", "Nginx", "Website"]
draft   = "True"
+++

Setting up Tangela again, so I think I'll write some notes about it
since I've been asked about it in the past... and didn't remember how
to setup it up myself X-D.

<!--more-->

## Setup Server

Setup a server/container/droplet to host Nginx. I'm just using a
Centos 7 minimal VM install on Nintales for now :). Personally, I'm
just giving it 1 core and 512MB RAM, but I don't have a bunch of
traffic.

### Setup Nginx

Add the nginx repo, and install:

```bash
sudo rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
sudo yum -y install nginx
```
Set firewall to allow http trafffic...

```bash
sudo firewall-cmd --permanent --add-service=http
sudo systemctl reload firewalld
```

Start nginx:

```bash 
sudo systemctl start nginx
```
