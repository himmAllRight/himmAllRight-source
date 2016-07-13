{:layout :post
:title  "Trying out snapd on Arch Linux"
:date "2016-07-12"
:author "Ryan Himmelwright"
:tags ["Linux" "Arch Linux" "snapd"]
:draft t}

I've been listening to  all the noise about Ubuntu "snaps", but I recently realized that I haven't tried this new technology yet...

<!-- more -->

### Snapd Install and Setup

I installed snapd on my small netbook (Abra), which is running Arch Linux. So, installing snapd was as easy as running: 

`pacaur -S snapd`

Now, I use pacaur so that I can install packages from Arch Linux's main repos, as well as the AUR. However, because snapd has actually been moved to the community repos, you can install it in normal pacman, without having to go to the aur.

`sudo pacman -S snapd`

After snapd is installed, it needs to be started. To start the snapd service, just use systemd:

`sudo systemctl start snapd`

Additionally, If you want to start the snapd service automatically after a reboot run the command:

`sudo systemctl enable snapd`

### Using snap
Once I had snapd installed and running, I started playing with the snap application. The first thing I should note is that to the extent of my knowledge, you have to run snap as root (at least for now). So this means you need to prepend commands with`sudo`. 

First, I wanted to find a snap package. This can be done using the `snap find` command as follows:

`sudo snap find package-name`  _(where **package-name** is the name of the package to search)_

Just like in any standard package manager search, the potential matches were returned, along with a version number, the developer, and a summary.

Snap has serveral other commands. To see a full list of available snap commands and a description for each one, just type:

`sudo snap help`

### Testing a snap
After learning about the basic snap commands, I wanted

### My Only Issue

### Thoughts

