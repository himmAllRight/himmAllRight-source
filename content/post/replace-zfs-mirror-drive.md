+++
title  = "Replacing a Drive in my ZFS Mirror"
date   = "2019-01-15"
author = "Ryan Himmelwright"
image  = "img/header-images/ww1-park-x230.jpg"
caption= "World War I Memorial Park, North Attleboro, MA"
tags   = ["Linux", "Homelab", "ZFS",]
draft  = "True"
Comments = "True"
+++


```
λ ninetales ~ → zpool status
  pool: Backups
 state: ONLINE
  scan: scrub repaired 0B in 0h52m with 0 errors on Tue Nov 20 00:23:13 2018
config:

	NAME                        STATE     READ WRITE CKSUM
	Backups                     ONLINE       0     0     0
	  mirror-0                  ONLINE       0     0     0
	    wwn-0x50014ee002299cbf  ONLINE       0     0     0
	    wwn-0x50014ee20902b0c2  ONLINE       0     0     0

errors: No known data errors

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

  pool: default
 state: ONLINE
  scan: scrub repaired 0B in 0h0m with 0 errors on Sun Nov 11 00:24:08 2018
config:

	NAME                              STATE     READ WRITE CKSUM
	default                           ONLINE       0     0     0
	  /var/lib/lxd/disks/default.img  ONLINE       0     0     0

errors: No known data errors
```




--------------------------------------------------------------------------------
Which drive is which

`lsblk`

`sudo hdparm -I /dev/sdd`
`sudo hdparm -I /dev/sdc`




--------------------------------------------------------------------------------
Which drive am I replacing?


```
λ ninetales by-uuid → zdb
Backups:
    version: 5000
    name: 'Backups'
    state: 0
    txg: 10885152
    pool_guid: 4108246424462889343
    errata: 0
    hostname: 'ninetales'
    com.delphix:has_per_vdev_zaps
    vdev_children: 1
    vdev_tree:
        type: 'root'
        id: 0
        guid: 4108246424462889343
        children[0]:
            type: 'mirror'
            id: 0
            guid: 2747801777241697193
            metaslab_array: 34
            metaslab_shift: 33
            ashift: 12
            asize: 1000189984768
            is_log: 0
            create_txg: 4
            com.delphix:vdev_zap_top: 50
            children[0]:
                type: 'disk'
                id: 0
                guid: 1816192614509453370
                path: '/dev/disk/by-id/wwn-0x50014ee002299cbf-part1'
                whole_disk: 1
                DTL: 47
                create_txg: 4
                com.delphix:vdev_zap_leaf: 61
            children[1]:
                type: 'disk'
                id: 1
                guid: 7388959194879004915
                path: '/dev/disk/by-id/wwn-0x50014ee20902b0c2-part1'
                whole_disk: 1
                DTL: 46
                create_txg: 4
                com.delphix:vdev_zap_leaf: 106
    features_for_read:
        com.delphix:hole_birth
        com.delphix:embedded_data
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
default:
    version: 5000
    name: 'default'
    state: 0
    txg: 2348788
    pool_guid: 13410195935159583570
    errata: 0
    hostname: 'ninetales'
    com.delphix:has_per_vdev_zaps
    vdev_children: 1
    vdev_tree:
        type: 'root'
        id: 0
        guid: 13410195935159583570
        create_txg: 4
        children[0]:
            type: 'file'
            id: 0
            guid: 2539842071018542623
            path: '/var/lib/lxd/disks/default.img'
            metaslab_array: 131
            metaslab_shift: 28
            ashift: 9
            asize: 49387405312
            is_log: 0
            DTL: 266
            create_txg: 4
            com.delphix:vdev_zap_leaf: 129
            com.delphix:vdev_zap_top: 130
    features_for_read:
        com.delphix:hole_birth
        com.delphix:embedded_data
```


--------------------------------------------------------------------------------
Repalcing the drive


`sudo zpool replace Data 4676737554230074290 /dev/sdd`




```
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




Better Time:

```
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
