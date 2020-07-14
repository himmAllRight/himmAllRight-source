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

Recently, I've been hosting a [Foundry VTT](http://foundryvtt.com) server (a
nodejs app) in a virtual machine on my home network. I would start the
application inside a
[`tmux`](http://ryan.himmelwright.net/post/setting-up-tmuxinator/) session, by
executing a CLI command which worked... fine.  However, if the VM restarted or
the applications crashed, I had to ssh in and manually run the command again. So,
to better automate this tedious task, I created a unit file to
define the foundry server as a systemd service. Here's how.

<!--more-->

### Unit Files

 With so many distributions utilizing
[systemd](https://en.wikipedia.org/wiki/Systemd), unit files have become a new
standard for auto-starting, or re-starting, applications on Linux. Simply put,
unit files are used to define resources to be managed by systemd. This includes
*services*, so to run FoundryVTT as a service, we need to create a new systemd
`.service` unit file.

### Creating the service file

To create a systemd unit file, I create a file at
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
contents of the `[Unit]` section define some basic information about the unit
file. The variables which define our *service*, are appropriately listed in the
`[Service]` section and include:

- `Environment=NODE_PORT=30000` sets an environment variable
- `Type=simple` states that our service is executing a single command, and is
    "started" when that command runs.
- `User=ryan` tells the service to run under the `ryan` user
- `ExecStart` defines the command to run run when the service is started
    (this is the command I had to manually type in `tmux`)
- `Restart=on-failure` will have the service automatically restart on any
    failures.

### Start and Enable the Service

With the unit file created, the service file can be started:

```bash
sudo systemctl start foundryvtt
```

In addition to starting the service, I also *enabled* it so that it will
automatically start up whenever the system reboots:


```bash
sudo systemctl enable foundryvtt
```

### Stopping, Restarting, and Status

To check that the service is running, use the command `systemctl status foundryvtt`:

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

... *A Bunch of Logs I removed*...
```

The output contains `Active: active (running)`, which means the service is
running. We can also restart or stop the service using the `systemctl restart
foundryvtt` and `systemctl stop foundryvtt` commands, respectively.

For example, I can stop the service and then check the status to verify it is
stopped (*Note the `Active: inactive (dead)` in the status output*).

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
automation to *create* them isn't too difficult either... but I'll show that in
another post. Until then, enjoy!
