+++
title    = "Nginx as a Reverse Proxy to Forward Sub-Domains"
date     = "2018-07-03"
author   = "Ryan Himmelwright"
image    = "img/header-images/foster-street-farmers-market1.jpg"
caption  = "Farmers Market, Foster Street, Durham NC"
tags     = ["Linux", "Homelab", "Network", "Nginx", "Website"]
Comments = "True"
draft    = "True"
+++

Last month, Rebecca and I moved to Durham, North Carolina. As a
result, I've had to re-setup our home network. In years past, I setup
a virtual machine running [Nginx](https://www.nginx.com/) as a
reverse-proxy (Tangela), and I decided to do that again on the new
network. While it is a simple process, it is one that other people often
ask me about. So, this time... I'm taking notes!

<!--more-->

## Why?

The purpose of this reverse proxy is to direct outside traffic to the
appropriate host internally, by looking at the sub-domain of the URL
request. For example, I may have servers for both
`website.himmelwright.net` and `dashboard.himmelwright.net` running
internally on my network, but they will have the same public IP. Using
nginx, I can point all of my web traffic to *tangela*, my
reverse-proxy. If tangela sees that the incoming request is for
`website.himmelwright.net`, it will forward that traffic to the
website server. On the other hand, if the request is for
`dashboard.himmelwright.net`, it will direct it to the dashboard
server. A reverse-proxy expands what can be accomplished on a single network,
and is a cleaner (and possibly safer) method than doing everything through
port-forwarding.

<a href="../../img/posts/nginx-reverse-proxy/tangela.png"><img
src="../../img/posts/nginx-reverse-proxy/tangela.png" style="max-width:
50%; float: right; margin: 0px 0px 0px 0px;" alt="Example snippet of
my org-babel config.org file" /></a> 

## Setup Server



To get started, configure a server/container/droplet that will host
nginx. I'm using a CentOS 7 minimal install VM on
[Nintales](http://ryan.himmelwright.net/pages/homelab/#ninetales) (my
home server). I don't have a bunch of traffic (well, I *shouldn't*), so I'm
just giving it 1 core and 512MB RAM.




### Setup Nginx

Next, it's time to setup and install Nginx.  

*Note*: the rest of the post will be focused on using a CentOS 7 base,
since that is what I am using. Adjust for your distro accordingly.

Add the nginx repo, and install it:

```bash
sudo rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
sudo yum -y install nginx
```
Tell the firewall to allow http traffic:

```bash
sudo firewall-cmd --permanent --add-service=http
sudo systemctl reload firewalld
```

Start and enable nginx:

```bash 
sudo systemctl start nginx
sudo systemctl enable nginx
```

## Configure Nginx

Examine the config file, just to check that everything looks alright.

```bash
vim /etc/nginx/nginx.conf
```

Specifically, we want to ensure that the following line exists before
proceeding:

```bash
include /etc/nginx/conf.d/*.conf;
```
That line basically states that any *.conf file inside the `/etc/nginx/conf.d/`
directory will also be loaded and used by nginx. This allows us to add our own configuration file in the next step. 

## Configure Proxy

I created a `reverse-proxies.config` (it can be named anything with a
`.config` extension) file in `/etc/nginx/conf.d/` to contain all of
the reverse proxy definitions. These are just server block
entries. For example:

```bash
server {
        listen 80;
        server_name website.himmelwright.net;
        location / {
                proxy_pass      http://192.168.1.198:80;
        }
}

server {
        listen 80;
        server_name dashboard.himmelwright.net;
        location / {
                proxy_pass      http://192.168.1.200:8080;
        }
}
```
Restart nginx for the changes to take effect:

```bash
sudo systemctl restart nginx
```

#### Side Note:
For some applications, you may need to add the URL to the `/etc/hosts`
file, and use that for nginx. I have experienced this in the past with
[Gitlab](https://about.gitlab.com/). For example:


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

## SELinux Fixes

At this point, you may be done. However, I was having issues getting
nginx to forward some of my ports... until I remembered that I was on
CentOS and it may be an issue with SELinux. It was.

One "*fix*" is to just disable SELinux. A *better* solution is to use
setools to allow the http connections:

```bash 
sudo yum install -y setools
setsebool -P httpd_can_network_connect true
```

## Conclusion

Besides having to configure your router to forward http traffic to the
server, that is really it. This is a real basic configuration, but it
has worked well for me over the years. If I start doing something more
complex, I may write provide an update. Until then, enjoy!
