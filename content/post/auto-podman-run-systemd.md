+++
title   = "Automatically Create and Run a Podman Container Using Systemd"
date    = "2021-01-31"
author  = "Ryan Himmelwright"
image   = "img/posts/auto-podman-run-systemd/mosstree2.jpeg"
caption = "Emerald Outback, Beech Mountain, NC"
tags    = ["linux", "podman", "containers", "systemd"]
draft   = "False"
Comments = "True"
+++

No, this is not the *same* as [my last
post](/post/create-podman-systemd-services/), but is a continuation of it.
While the basic `podman generate systemd` generated file works for many
cases... it wasn't a good long-term solution for my jellyfin container. So, I
made a small tweak.

<!--more-->

## The Issue

My issue was that the container initially worked, but would occasionally
break when it grew old. By itself, it isn't a problem. Containers are
designed to be ephemeral, and arguably *should* be blown away before being
instantiated again. The difficulty is that creating a new container
results in having to edit the container uuids in the service file, otherwise
the service breaks... which seems to sometimes then break the *new* container.

<a href="../../img/posts/auto-podman-run-systemd/jellyfin-failed-webpage.png"><img alt="Failed Jellyfin Webpage" src="../../img/posts/auto-podman-run-systemd/jellyfin-failed-webpage.png" style="max-width: 100%;"/></a>

This requires me to then *disable* the service, blow-away and make the new
container, update the service file, and *finally* start the service... again.

##  A Different Approach

I started to think about how I could better the process. I knew that a
*newly* created container seemed to work each time, as I previously used the
`--rm` flag when starting it manually. From there, I wondered if I could
write *my own* systemd service file using the `podman run` command instead.
This would both create and kick off a *new* container after boot, instead of
re-starting a persistent one.

## Testing it out

To test out my plan, I decided to edit the file created by the `podman
generate system` command in the last post and go from there. I opened
the service file (`~/.config/systemd/user/jellyfin.service`) in my editor and
changed the following line under the `[Service]` section:

```ini
ExecStart=/usr/bin/podman start 2ba0f86b0fc53cb2fe43abb20215680982800c1bf53421e1a3a90855fa79f030
```

I swapped `ExecStart` to use my manual `podman run` command, with a `--rm` flag:

```ini
ExecStart=/usr/bin/podman run --name jellyfin --rm -d -v /home/ryan/Network/jellyfin/config:/config -v /home/ryan/Network/jellyfin/cache:/cache -v /home/ryan/Music:/media/music:ro -v /home/ryan/Videos:/media/videos:ro --net=host --privileged jellyfin/jellyfin:latest
```

I also edited the `ExecStop` and `ExecStopPost` values:


```ini
ExecStop=/usr/bin/podman stop -t 10 2ba0f86b0fc53cb2fe43abb20215680982800c1bf53421e1a3a90855fa79f030
ExecStopPost=/usr/bin/podman stop -t 10 2ba0f86b0fc53cb2fe43abb20215680982800c1bf53421e1a3a90855fa79f030
```

I switched them to use the container name (`jellyfin`) instead of uuids:

```ini
ExecStop=/usr/bin/podman stop -t 10 jellyfin
ExecStopPost=/usr/bin/podman stop -t jellyfin
```

After saving the changes, I removed my old jellyfin container, reloaded the
unit files (using `systemctl --user daemon-reload`, as described in the
previous post), and restarted the machine to determine what elements would
need tweaking when writing *my* service file.

## Another Shortened Post...

However, I never made my own service file, or even edited the generated one
again. It appeared to work fine after making those few tweaks. For the
second time in a row, I have a much simpler post than originally intended
due to the tooling around `podman`. I'm okay with that.

## Conclusion

While the solution still isn't 100% *perfect* (containers sometimes don't
destroy themselves, and I still have to login for the service to autostart)
it has overall been working great for me. I no longer have to worry about
uuids. When I encounter an issue, I stop the container, it kills
itself, and then the service starts up a fresh one. Much better.