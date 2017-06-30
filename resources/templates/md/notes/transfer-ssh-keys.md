I am learning how to transfer ssh keys. This way, I can have my fedora VMs using
my same ssh key pair, so I can have access to the fedora stuff from either. This
is desired because I am currently running a VM on Kadabra, but I want to be able
to setup a Fedora work VM on alakazam as well for when I am on that, and Kadabra
isn't powered up or with me.

It also allows me to back them up in case the VM gets messed up.

### Backing up the keys
It looks like (at least on Fedora), the private keys are in `/etc/ssh/`. So,
tar'd them up:

```
mkdir ~/ssh-export
sudo cp /etc/sshd/ssh_host_* ~/ssh-export/
sudo tar cfv ssh-export.tar ssh-export/
sudo rm -r ~/ssh-export/
```

The main thing is to make sure the permissions stay the same, or else it won't
work. So I aggressively threw in some `ls -la`'s to make sure everything
matched. 

### Testing it out
I needed to test it out, so I thought the best way to that would be to setup my
Fedora VM on Alakazam awhile, and try it out.

*Note:* It also turned out that the day I tried this, was [Fedora Upgrade Test Day](https://communityblog.fedoraproject.org/fedora-26-upgrade-test-day-2017-06-30/), so I installed Fedora 25 to test the 26 Upgrade :). Perfect timing.
