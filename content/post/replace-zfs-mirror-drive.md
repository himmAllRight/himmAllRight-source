+++
title  = "Replacing a Drive in my ZFS Mirror"
date   = "2019-01-15"
author = "Ryan Himmelwright"
image  = "img/header-images/hdd-replace.jpg"
caption= "My Desk, Durham, NC"
tags   = ["Linux", "Homelab", "filesystems", "ZFS",]
draft  = "True"
Comments = "True"
+++

Sometime right before the Holidays, one of the data hard drives in my servers
started get noisy... very noisy. Fearing the worst, [did a
backup](../zfs-backups-to-luks-external) and shutdown the server until I have
time to investigate further, and likely, replace the drive. That time came this
past week.

<!--more-->

### Verifying the drive failed


Before throwing money at the problem, I wanted to verify if ZFS was
detecting any issues. When I ran a `zpool status` on my `Data` pool, it
did warn me that one of my devices has experienced an error, but I have not
(yet) encountered any data errors. Time to buy a new drive.

```bash
λ ninetales ~ → zpool status Data
  pool: Data
 state: ONLINE
status: One or more devices has experienced an unrecoverable error.  An
	attempt was made to correct the error.  Applications are unaffected.
action: Determine if the device needs to be replaced, and clear the errors
	using 'zpool clear' or replace the device with 'zpool replace'.
   see: http://zfsonlinux.org/msg/ZFS-8000-9P
  scan: resilvered 1.14M in 0h0m with 0 errors on Sat Jan 12 10:49:31 2019
config:

	NAME                                  STATE     READ WRITE CKSUM
	Data                                  ONLINE       0     0     0
	  mirror-0                            ONLINE       0     0     0
	    ata-TOSHIBA_DT01ACA300_365XDT3KS  ONLINE       0     0     2
	    ata-TOSHIBA_DT01ACA300_365XDR5KS  ONLINE       0     0     0

errors: No known data errors
```

### Ordering a New Drive

When I started shopping for drives, I decided to replace my broken 7200 RPM drive
a 5400 RPM one. I'd rather have the drives last longer and run quieter than
whatever marginal speed difference the faster spinning drives may provide. I
decided to go with a [3TB Western Digital RED
drive](https://www.amazon.com/dp/B008JJLW4M/ref=twister_B07GXT9HNH?_encoding=UTF8&psc=1)
this time, even tough it's a bit more expensive... mostly just to try it out.

### Replacing the Drive

<center>
<a href="../../img/posts/replace-zfs-mirror-drive/hdd-swap.jpg"><img alt="Swapping the two hard drives" src= "../../img/posts/replace-zfs-mirror-drive/hdd-swap.jpg" style="max-width: 100%;"/></a>
<div class="caption">Swapping the hot-swap caddy from the broken hard drive (left) with my new WD Red drive (right)</div>
</center>

Physically swapping the hard drives was a breeze. I could easily tell which
drive was the defective one (the one causing the entire server to rumble), so I
slid it out. I love hot-swap drive bays. Next, I simply unscrewed the drive
from the caddy, and screwed in the new drive. Lastly, I slide the caddy back
into the server and booted it up.


#### Figuring out which drive to replace

While figuring out which *physical* drive was the broken one, determining which
disk the new one was replacing was a bit more difficult. Im order to add the
new drive to my `Data` pool, I needed to tell ZFS which drive I had *replaced*.
This was made more complicated by the fact that previously, the two drives in
the mirror were the same and both showed up as
`/dev/disk/by-id/ata-TOSHIBA_DT01ACA300_365XDR5KS`. I needed to get the `guid`
for each drive, which would differ between them. I used the command `zdb` to
spit out the information of each of my pools:


```bash
λ ninetales ~ → zdb
... (just Data pool output)...
Data:
    version: 5000
    name: 'Data'
    state: 0
    txg: 15996848
    pool_guid: 2285339125999939520
    errata: 0
    comment: 'iocage'
    hostname: 'ninetales'
    com.delphix:has_per_vdev_zaps
    vdev_children: 1
    vdev_tree:
        type: 'root'
        id: 0
        guid: 2285339125999939520
        children[0]:
            type: 'mirror'
            id: 0
            guid: 15171243251753521949
            metaslab_array: 34
            metaslab_shift: 34
            ashift: 12
            asize: 3000588042240
            is_log: 0
            create_txg: 4
            com.delphix:vdev_zap_top: 125
            children[0]:
                type: 'disk'
                id: 0
                guid: 4676737554230074290
                path: '/dev/disk/by-id/ata-TOSHIBA_DT01ACA300_365XDT3KS'
                phys_path: '/dev/ada1'
                whole_disk: 1
                not_present: 1
                DTL: 123
                create_txg: 4
                com.delphix:vdev_zap_leaf: 126
            children[1]:
                type: 'disk'
                id: 1
                guid: 13442522248687181242
                path: '/dev/disk/by-id/ata-TOSHIBA_DT01ACA300_365XDR5KS'
                phys_path: '/dev/ada3'
                whole_disk: 1
                DTL: 122
                create_txg: 4
                com.delphix:vdev_zap_leaf: 159
    features_for_read:
        com.delphix:hole_birth
        com.delphix:embedded_data
...
```

At first, I still didn't know drive which was which. However, after looking at
the output closer, I noticed that one of the listed Toshiba drives had the
line `not_present: 1`... indicating it was the broken drive I removed!

#### Replacing the drive

With the `guid` of the broken drive, I was able to start the process to
replacing it in the pool with my new one. I issued the following `zpool
replace` command:

```bash
sudo zpool replace Data 4676737554230074290 /dev/sdd
```

The `zpool replace` command requires three arguments:

* the name of the pool (`Data`),

* the `guid` of the previous drive (`4676737554230074290`), and

* the path to my new drive (`/dev/sdd`).

Afterwards, the resilvering process started (rebuilding the mirror by copying
the data from the one drive to the new one). I was able to check the status of
the process using `zpool status Data`.

```bash
λ ninetales by-uuid → zpool status Data
  pool: Data
 state: DEGRADED
status: One or more devices is currently being resilvered.  The pool will
	continue to function, possibly in a degraded state.
action: Wait for the resilver to complete.
  scan: resilver in progress since Sat Jan 12 11:29:36 2019
	72.6M scanned out of 1.03T at 2.42M/s, 123h32m to go
	72.2M resilvered, 0.01% done
config:

	NAME                                  STATE     READ WRITE CKSUM
	Data                                  DEGRADED     0     0     0
	  mirror-0                            DEGRADED     0     0     0
	    replacing-0                       DEGRADED     0     0     0
	      4676737554230074290             UNAVAIL      0     0     0  was /dev/disk/by-id/ata-TOSHIBA_DT01ACA300_365XDT3KS
	      sdd                             ONLINE       0     0     0  (resilvering)
	    ata-TOSHIBA_DT01ACA300_365XDR5KS  ONLINE       0     0     0

errors: No known data errors
```

Resilvering can take a *long* time. Luckily, I only had about ~1 TB~ of data to
rebuild, so I hoped it wouldn't *actually* take the 123.5 hours the first
`status` told me! Regardless, while waiting  for the pool to rebuild, the only
thing to do is wait (*and hope that the other drive doesn't break in the
process!*).


#### Resilver Complete

In just over 4 hours, my pool had rebuilt and was back online.

```bash
λ ninetales ~ → zpool status Data
  pool: Data
 state: ONLINE
  scan: resilvered 1.03T in 4h8m with 0 errors on Sat Jan 12 15:38:26 2019
config:

	NAME                                  STATE     READ WRITE CKSUM
	Data                                  ONLINE       0     0     0
	  mirror-0                            ONLINE       0     0     0
	    sdd                               ONLINE       0     0     0
	    ata-TOSHIBA_DT01ACA300_365XDR5KS  ONLINE       0     0     0

errors: No known data errors
```

Looking at this output now, I realize I probably should have added the new
drive by `uuid`, and not pathname...hmmm...

Oh well. That is a post for another day. For now... at least my broken drive
has finally been replaced!
