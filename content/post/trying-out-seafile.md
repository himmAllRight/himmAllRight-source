+++
title  = "Trying Out Seafile"
date   = "2018-03-24"
author = "Ryan Himmelwright"
image  = "img/header-images/container-building-umich.jpg"
tags   = ["Homelab", "Linux", "Database",]
draft  = true
+++

When I was in college, I mostly used Dropbox to handle all of my file syncing
needs. As I approached graduation, I setup an Owncloud droplet (which is now a
Nextcloud instance) to replace my Dropbox usage. While it has worked fairly well
over the years, I've been watching [seafile](https://www.seafile.com/en/home/)
out of the corner of my eye the last few years, but haven't taken the time to
try it out. I have now, and I like it.


<!--more-->

## Seafile

<a href="../../img/posts/trying-out-seafile/seafilelogo.png"><img src="../../img/posts/trying-out-seafile/seafilelogo.png" style="max-width: 95%; float: left; margin: 0px 15px 0px 0px;" alt="Docker ps" /></a>
<div class="caption">The Seafile Logo</div>

As stated on their website:

>Seafile is an enterprise file hosting platform with high reliability and
>performance. Put files on your own server. Sync and share files across
>different devices, or access all the files as a virtual disk.


## Setup

Like a nextcloud setup, to get seafile up and running, you need to configure a
server, and then clients to connect to it. However it isn't difficult.

### Server

The countless number of ways seafile can be configured may make setting up the
server component for the first time a bit intimidating. There are several
database back-ends (SQLite, MySQL...), web servers (Nginx, Apache), as well as
advanced options (Memcached, LDAP, etc) it can be configured with. However, the
seafile developers *do* provide an [installation
script](https://github.com/haiwen/seafile-server-installer) to easily install
both the Pro and Community editions under Linux. This is what I used to test it
out for now. 

#### Download

The first step is to download the server application which can found on [partway
down the download page](https://www.seafile.com/en/download/#server). After
Downloading, extract the contents of the package.

``` bash
wget https://download.seadrive.org/seafile-server_6.2.5_x86-64.tar.gz
tar xf seafile-server*.tar.gz
```

Inside the extracted directory, there are several `setup-seafile-*.sh*` scripts.
I just used the basic `setup-seafile.sh` one.

#### Dependencies

<a href="../../img/posts/trying-out-seafile/ubuntu-logo.jpg"><img
src="../../img/posts/trying-out-seafile/ubuntu-logo.jpg" style="max-width:
100%; float: right; margin: 5px 10px 10px 10px;" alt="Ubuntu Logo" /></a>

Depending on what setup script it being used, and the state of the computer it
is used one, there may be some missing dependencies. While I am sure there is a
nice list of the required dependencies posted somewhere... I didn't look for it.
If I am being completely honest... I just kept repeatedly running the script,
installing whatever package it yelled at me for each time until it worked. For
my rather fresh install of Ubuntu 16.04 server, this meant installing:

- python-setuptools
- python-imaging
- sqlite3

So, on an Ubuntu 16.04 system, a simple `sudo apt install python-setuptools
python-imaging sqlite3` should do the trick...

#### Install Script

With the dependencies installed, the script should run through without screaming
for anymore packages. However, it *will* ask for a few pieces of information
including *server-name*, *server-ip/domain*, *data-dir*, and *fileserver port*
to install the fileserver component.

<a href="../../img/posts/trying-out-seafile/seahub-web.png"><img src="../../img/posts/trying-out-seafile/seahub-web.png" style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;" alt="Docker ps" /></a>
<div class="caption">The Seafile Web Client, Seahub</div>

After configuring the fileserver, the script will flow right into configuring
[Seahub](https://github.com/haiwen/seahub), which is the web interface that sits
on top of the fileserver. This part is less needy and will only require a
simpler *[Enter]* press to continue.

At the end, the script should display useful information about how to
start/stop/reset the servers, as well as what ports each part is running on.

#### Run & Start



Starting the servers is done by simply doing what the script says... running the
following commands:

``` bash
./seafile.sh start
./seahub.sh start
```

With the servers running, it may be necessary to configure the firewall to allow
their ports. On Ubuntu 16.04:

``` bash
sudo ufw allow 8000/tcp
sudo ufw allow 8082/tcp
```

That's it. With any luck, clients should be able to connect to the server
(assuming the server is reachable from the client computer... but that's a
lesson for another day).

*Note: The first time seahub is run, it will need to setup an admin acount. So
while it was nice and considerate in the last step... it will insist on being
supplied a username and password for the new admin account. Again, just do what
it says.*



### Client

The seafile desktop client was trivial to install. It was in the Solus repos, so
I just needed to run `sudo eopkg it seafile-client`, and I was done. I also
installed it on my work computers (which unfortunately runs Windows 10), and
even that was simple. I just downloaded and installed the Windows "Desktop
Syncing Client" at the top of the [download
page](https://www.seafile.com/en/download/).


## My Thoughts
<a href="../../img/posts/trying-out-seafile/seafile-client.png"><img
src="../../img/posts/trying-out-seafile/seafile-client.png" style="max-width:
100%; float: right; margin: 0px 0px 0px 0px;" alt="Docker ps" /></a>


The desktop client is simple. It responds quickly, and is a nice
little command center where I can see how seafile is configured on each system.
Seafile libraries allow me to not sync everything on each machine, but only what
I need. Nextcloud had this feature, but it was used a little differently. I had
to go to the `Nextcloud` folder in the client UI, and then check/uncheck all of
the sub-folders I wanted to sync on my machine.

### What I Like



### What I Don't Like

### Future Plans

