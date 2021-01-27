+++
title   = "Automatically Create and Run a Podman Container Using Systemd"
date    = "2021-01-30"
author  = "Ryan Himmelwright"
image   = "img/posts/auto-podman-run-systemd/mosstree2.jpeg"
caption = "Emerald Outback, Beech Mountain, NC"
tags    = ["linux", "podman", "containers", "systemd"]
draft   = "True"
Comments = "True"
+++

No, this isn't the same thing as the [last
post](/post/create-podman-systemd-services/), although it does build off of
it. While that basic solution demonstrated in that post works for many
cases... it didn't for my jellyfin server. So, I made a small tweak that
seems to be working a bit better.

<!--more-->

## The Issue

Essentially, the issue was that the container work, but then
occasionally break. Something would just get messed up and it would make more
sense to blow away the container and start a new one. By itself, that's fine.
containers are designed to be ephemeral and arguably *should* be blown away
and instantiated again. However, the problem was that creating a new
container resulted in having to edit the container uuids in the service file,
otherwise the service would break... which seemed to sometimes mess with the
container. 

*Example of the the issue or something??? Need a visual here to break up the text/ balance the examples*

So I would have to *disable* the service, blow-away and make the new
container, update the service file, and then finally start the service. This
wasn't a great method for what I needed.

##  A Different Approach

I started to think about how I could better the process. I knew the container
worked each time if it was *newly* created, as I used the `--rm` flag when
starting it manually. From there, I wondered if I could write *my own*
systemd service file using the *podman run* command instead. This command
would both create and kick off a *new* container after boot, instead of
starting a persistent one.


## Another Shortened Post...

To just test out the theory, I decided to edit the file I generated in the
previous post using `podman generate` command, and go from there. So, I
opened the service file (`~/.config/systemd/user/jellyfin.service`) in my
editor and changed the following line under the `[Service]` section:

```ini
ExecStart=/usr/bin/podman start 2ba0f86b0fc53cb2fe43abb20215680982800c1bf53421e1a3a90855fa79f030
```

To instead use my manual `podman run` command, with a `--rm` flag:

```ini
ExecStart=/usr/bin/podman run --name jellyfin --rm -d -v /home/ryan/Network/jellyfin/config:/config -v /home/ryan/Network/jellyfin/cache:/cache -v /home/ryan/Music:/media/music:ro -v /home/ryan/Videos:/media/videos:ro --net=host --privileged jellyfin/jellyfin:latest
```

I also edited the `ExecStop` and `ExecStopPost` commands:


```ini
ExecStop=/usr/bin/podman stop -t 10 2ba0f86b0fc53cb2fe43abb20215680982800c1bf53421e1a3a90855fa79f030
ExecStopPost=/usr/bin/podman stop -t 10 2ba0f86b0fc53cb2fe43abb20215680982800c1bf53421e1a3a90855fa79f030
```

To use the container name (`jellyfin`) instead of the uuids:

```ini
ExecStop=/usr/bin/podman stop -t 10 jellyfin
ExecStopPost=/usr/bin/podman stop -t jellyfin
```

After saving the changes, I removed my old jellyfin container, reloaded the
unit files (as described in the previous post), and restarted to machine to
figure out what needed to be modified for my service file.

However, I never made my own service file, or even edited the generated one
again. It appears to work just fine after making those few tweaks. So, this
has been my second post that ended up having a much smaller scope than
expected, thanks to the tooling around `podman`.


## Conclusion

While the solution still isn't 100% *perfect* (containers sometimes don't
destroy themselves, and I still have to login for the service to auto start
up) it has been working great for me. Using `run --rm` to start new
containers every time, and destroy themselves at shutdown, means I no longer
have to worry about uuids. When I encounter an issue, I just stop the
container, and it kills itself, allowing the service to bring up a fresh one
online. Simple.