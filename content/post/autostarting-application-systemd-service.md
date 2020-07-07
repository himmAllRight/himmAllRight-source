+++
title   = "Auto-starting Applications with Systemd Services"
date    = "2020-07-15"
author  = "Ryan Himmelwright"
image   = "img/posts/three-required-gnome-extensions/reading-corner.jpeg"
tags    = ["Linux", "systemd", "Customization",]
draft   = "True"
Comments = "True"
+++


<!--more-->

### Intro


#### Cron and Systemd


### Creating the service file

```
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

### Starting the Service


### Stopping, Restarting, and Status


### Conclusion
