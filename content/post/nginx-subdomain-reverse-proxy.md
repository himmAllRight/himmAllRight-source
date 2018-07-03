+++
title   = "Nginx as a Reverse Proxy to Forward Sub-Domains"
date    = "2018-07-03"
author  = "Ryan Himmelwright"
image   = "img/header-images/foster-street-farmers-market1.jpg"
caption = "Farmers Market, Foster Street, Durham NC"
tags    = ["Linux", "Homelab", "Network", "Nginx", "Website"]
draft   = "True"
Comments = "True"
+++

Last month, Rebecca and I moved to Durham, North Carolina and as a
result I've had to re-setup our network. I used to configure a Virtual
Machine running Nginx as a reverse-proxy on the network (Tangela), and
I decided I wanted to do that again on the new network. While it's a
simple process, it's one that other people often ask me about (and I
forget about). So, this time... I'm taking notes!

<!--more-->

## Why?

The purpose of this reverse proxy is to direct outside traffic to the
appropriate host internally, by looking at the subdomain of the url
request. For example, I may have servers for both
`website.himmelwright.net` and `dashboard.himmelwright.net` running
internally internally on my network, but they will have the same
public IP. Using Nginx, I can point all of my web traffic to
*tangela*, and if it sees that the incoming request is for
`website.himmelwright.net`, it will forward that traffic to the
website server. On the other hand, if the request is for
`dashboard.himmelwright.net`, it will direct it to the dasboard
server.

<a href="../../img/posts/nginx-reverse-proxy/tangela.png"><img
src="../../img/posts/nginx-reverse-proxy/tangela.png" style="max-width:
50%; float: right; margin: 0px 0px 0px 0px;" alt="Example snippet of
my org-babel config.org file" /></a> 

## Setup Server



To get started, configure a server/container/droplet that will host
Nginx. I'm using a Centos 7 minimal install VM on
[Nintales](http://ryan.himmelwright.net/pages/homelab/#ninetales) (my
home server). I don't have a bunch of traffic (well, I *shouldn't*), so I'm
just giving it 1 core and 512MB RAM.




### Setup Nginx

Next, it's time to setup and install Nginx. 

*NOTE: The rest of the post will be focused on using a Centos 7 base,
since that is what I am using.*

Add the nginx repo, and install it:

```bash
sudo rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
sudo yum -y install nginx
```
Tell the firewall to allow http trafffic...

```bash
sudo firewall-cmd --permanent --add-service=http
sudo systemctl reload firewalld
```

Start and enable nginx to automatically start:

```bash 
sudo systemctl start nginx
sudo systemctl enable nginx
```

## Configure Nginx

Look at the config file, just to check that everything looks
good.

```bash
vim /etc/nginx/nginx.conf
```

Specifically, we want to ensure that the following line exists before
proceding:

```bash 
include /etc/nginx/conf.d/*.conf;
```
That line basically says that any *.conf file inside the `/etc/nginx/conf.d/`
directory will also be loaded and used by nginx. This allows us to add our own configuration file in the next step. 

## Configure Proxy

I created a `reverse-proxies.config` (it can be named anything with a
`.config` extension) file in `/etc/nginx/conf.d/` to contain all of
the reverse proxy definations. These are just server block
entries. For example:

```bash
server {
        listen 80;
        server_name website.himmelwright.net;
        location / {
                proxy_pass      http://192.168.1.198:8080;
        }
}

server {
        listen 80;
        server_name dashboard.himmelwright.net;
        location / {
                proxy_pass      http://192.168.1.200:80;
        }
}
```
Restart nginx for the changes to take effect:

```bash
sudo systemctl restart nginx
```

#### Side Note:
For some applications, you may need to add the url to the
`/etc/hosts` file, and use that for nginx. I have experienced this in
the past with [Gitlab](https://about.gitlab.com/). So, for example:


```bash
/etc/hosts
---
192.168.1.201  git.himmelwright.net
```

and then in the config file:

```bash
/etc/nginx/config.d/reverse-proxies.config
---
server {
        listen 80;
        server_name git.himmelwright.net;
        location / {
                proxy_pass      http://git.himmelwright.net:80;
        }
}
```

## SElinux Fixes

At this point, you may be done. I however was having issues getting
nginx to forward some of my ports... until I rembered I was on Centos
and it was probably an issue with selinux. It was.

One "*fix*" is to just disable selinux. A *better* solution is to use
setools to allow the http connections:

```bash 
sudo yum install -y setools
setsebool -P httpd_can_network_connect true
```

## Conclusion

Besides having to configure your router to forward http traffic to the
server, that really it. This is a real basic configuration, but it was
worked well for me over the years. If I start doing something more
complex, I may write about it. Until then, enjoy!
