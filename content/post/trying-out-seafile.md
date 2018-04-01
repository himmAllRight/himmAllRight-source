+++
title  = "Trying Out Seafile"
date   = "2018-03-24"
author = "Ryan Himmelwright"
image  = "img/header-images/obx-houses.jpg"
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

While they are an "*enterprise* file hosting platform", there is a Community
Edition that is *Free & Open Source*, which is exactly how I like my software.
Lets get started.

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
100%; float: right; margin: 0px 0px 0px 0px;" alt="Seafile Desktop Client" /></a>

So I have been using seafile as a syncing mechanism for the past few weeks and
after the initial setup, it has been rather uneventful. Which is a good thing.
It just keeps running in the background, and I really don't think about it.
Which is exactly what you want with a syncing solution...

That being said, I haven't fully dug into all of the features and details of the
application yet. So, if I critique something due to my own ignorance that simply
isn't true, I apologize in advance.

### What I Like

- **Desktop Client** - The desktop client is simple. It responds quickly, and is
a nice little command center where I can see how seafile is configured on each
individual system.

- **Select *which* Libraries to sync** - Seafile libraries allow me to not sync
everything on each machine, but only what I need. Nextcloud had this feature,
but it was used a little differently. I had to go to the `Nextcloud` folder in
the client UI, and then check/uncheck all of the sub-folders I wanted to sync on
my machine.

- **Pick *where* libraries sync** - Even better than being able to pick *which*
  libraries to sync, is having the power to choose *where* each on will sync.
  While seafile generates a default `seafile` directory, the location of each
  library is completely independent. For example, I can sync my `work` library
  to `~/Documents/Work/`, my `Music` to `~/Music`, and `emacs` to
  `~/Documents/Programming/Editors/why/so/many/diectories/emacs/`. I love this.
  It lets seafile *integrate* with my workflow, rather than forcing me to make
  *it be* my workflow.

- **Encrypted Libraries** - When creating a new library, it is possible to
  generate an [encrypted
  one](https://www.seafile.com/en/help/encrypted_libraries/). These libraries
  use client-sidem end-to-end encryption and require a password. The file
  *contents* (Note: note directory or file *names*) are encrypted on the client
  side and not on the server, so even the server admin cannot access the file
  contents. This is a feature I'd like to see in more applications.

<a href="../../img/posts/trying-out-seafile/encrypt-library.png"><img
src="../../img/posts/trying-out-seafile/encrypt-library.png" style="max-width:
100%; align: center; float: center; margin: 0px 0px 0px 0px;" alt="Docker ps" /></a>
<div class="caption">When syncing an encrypted library, a password must be entered.</div>

- **Fast Sync** - I only have anecdotal evidence, but the syncing in seafile has
  *felt fast*. Files seem to pull down very quickly, and setting up my libraries
  on a new device doesn't take a very long time. I might have to get some
  numbers to actually measure if it's any better than something like nextcloud,
  but if I'm happy... does it really *matter*?

### What I Don't Like

- **No Folders/Nested libraries** - As far as I can tell, I don't think it is
  possible to organize seafile libraries with folders, or even a nested library
  structure. However, this is one of those areas that I haven't had to look into
  yet. However, as I start to increase my seafile usage and the number of my
  libraries increases, I could see this being a feature I'd really enjoy.

- **Phone Sync Tricky** - The phone sync (specifically auto photo upload) was
  tricky to get working at first. After setting it up, it didn't seem to work,
  or at least not as promptly as nextcloud does. I took a few photos to test it
  out today, it seemed to work *okay*, but I don't think it started syncing
  right away. Right now, I just don't 100% trust it to work without me thinking
  about it. Hopefully this improves with time.


### Future Plans

To summarize, I have been loving seafile, and I think I have only scratched the
surface. I haven't even tried playing with features like [History and
Snapshots](https://www.seafile.com/en/help/snapshot/), [Full Text File
Search](https://www.seafile.com/en/help/search/), [Sharing
File](https://www.seafile.com/en/help/share/), or [Locking
Files](https://www.seafile.com/en/help/file_lock/) yet. My plan right now is to
continue to experiment a bit more, and then switch to it for my main syncing
device when I redo my main server setup in a couple of weeks. I definately
recommend giving seafile a shot, if you haven't already.
