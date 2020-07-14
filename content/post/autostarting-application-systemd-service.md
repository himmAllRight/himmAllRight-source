+++
title   = "Auto-starting Applications with Systemd Services"
date    = "2020-07-15"
author  = "Ryan Himmelwright"
image   = "img/posts/autostart-application-systemd-service/unc-quad-trees.jpeg"
caption = "UNC-Chapel Hill Campus, Chapel Hill, NC"
tags    = ["Linux", "systemd", "Customization",]
draft   = "True"
Comments = "True"
+++

Recently, I've been hosting a [Foundry VTT](http://foundryvtt.com) server
(nodejs app) in a virtual machine on my home network. Previously, I would
start the application in a `tmux` session, by executing a command in the cli
which worked... fine.  However, if the VM restarted or the applications
crashed, I had to ssh in and manually start it up again. So, I created a
systemd unit file to automate the foundry server as a service. Here's how.

<!--more-->

### Unit Files

Years ago, I used to use `cron` to automate when my applications and scripts
should run. For example, I had `rsync` scripts that would kick off nightly to
backup my hard drive. With many distributions utilizing
[systemd](https://en.wikipedia.org/wiki/Systemd), unit files have also become
a new standard for auto-starting, or re-starting, applications on Linux. Simply
put, unit files are used to define a *service* (among other things) to be
controlled by systemd.

### Creating the service file

To create a systemd unit file for a service, I create a file at
`/lib/systemd/system/foundryvtt.service` and filled it with the following
contents:

```ini
[Unit]
Description=A service to run the Foundry VTT node app
Documentation=https://foundryvtt.com
After=network.target

[Service]
Environment=NODE_PORT=30000
Type=simple
User=ryan
ExecStart=/usr/bin/node /home/user/foundryvtt/resources/app/main.js --dataPath=/home/user/foundrydata
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

This file tells systemd all the information it needs to run the service. The
items that are important for this file in particular are:

- `User=ryan` which tells the service to run under the `ryan` user
- `ExecStart` which defines the command to execute when the service is started
    (this is the command I use to manually type into `tmux`)
- `Restart=on-failure` will have the service automatically restart on any
    failures.

Lastly, we include `Environment=NODE_PORT=30000` to set the environment
variable, `NODE_PORT` to the value of `30000`.


### Start and Enable the Service

With the unit file created, we can start the service:

```bash
sudo systemctl start foundryvtt
```

In addition to starting the service, I also *enabled* it so it will
automatically start up again whenever the system reboots:


```bash
sudo systemctl enable foundryvtt
```

### Stopping, Restarting, and Status

To check that the service is running, the command `systemctl status foundryvtt`
can be used:

```bash
sudo systemctl status foundryvtt
[ryan@magmar dotfiles]$ sudo systemctl status foundryvtt
● foundryvtt.service - A service to run the Foundry VTT node app
     Loaded: loaded (/usr/lib/systemd/system/foundryvtt.service; disabled; vendor preset: disabled)
     Active: active (running) since Sun 2020-07-12 16:34:29 EDT; 2s ago
       Docs: https://foundryvtt.com
   Main PID: 1070 (node)
      Tasks: 11 (limit: 2327)
     Memory: 93.8M
        CPU: 1.227s
     CGroup: /system.slice/foundryvtt.service
             └─1070 /usr/bin/node /home/ryan/foundryvtt/resources/app/main.js --dataPath=/home/ryan/foundrydata

... Logs...
```

In the output, we can see `Active: active (running)`, which means it is
running. We can also restart or stop the service using the `systemctl restart
foundryvtt` and `systemctl stop foundryvtt` commands, respectively.

For example, I can stop the service and then check the status to verify it is
stopped (Note the `Active: inactive (dead)`).

```bash
[ryan@magmar]$ sudo systemctl stop foundryvtt
[ryan@magmar]$ sudo systemctl status foundryvtt
● foundryvtt.service - A service to run the Foundry VTT node app
     Loaded: loaded (/usr/lib/systemd/system/foundryvtt.service; disabled; vendor preset: disabled)
     Active: inactive (dead)
       Docs: https://foundryvtt.com
```

### Conclusion

That's about it. Systemd unit files seem extremely complicated at first, but
after writing one they really aren't bad. Additionally, it turns out that using
automation to create them isn't difficult either... but I'll show that in
another post. Until then, enjoy!
