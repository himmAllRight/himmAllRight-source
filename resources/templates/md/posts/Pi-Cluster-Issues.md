{:layout :post
:title  "Random Issues with Pi Cluster"
:date "2017-05-30"
:author "Ryan Himmelwright"
:tags ["Homelab" "Cluster" "Pi" "DevOps" "Ansible"]
:draft? true
}

*5/29/17*
So I've encountered some issues with my pi cluster. It started with me not being able to ssh into one of the nodes, so I pulled it down and went to figure it out and make sure the keys and everything. But then it had an issue where it was hanging on the boot.

So I started looking at the other pi, and after a little while, it two was havinging issues. I couldn't get them to both work so I reset them both. After reseting them, they start to show the issues again during setup. The issues looked like it would fail loading modules, and then it was trying to do some sort of pxe boot. Eventually, it also notice it was hanging because during the pxe boot it was looking for a missing file.

One of the things I though *might* be adding to the issues was if my router was setting them to the same ip or something with the reserved DHCP addresses. So, I disabled that and it seems to be working. I did a fresh start and setup them up and I have sshed into one of the nodes after "re-racking" them, but I haven't connected to the other one yet. This may just be because I haven't found it's ip yet (I haven't spent too much time looking at my nmap printout yet). I am hoping it too hasn't failed again...

I should often note all of these issues were with the two raspberry pi nodes. The bananna pi, (hopefully I don't jynx myself here) is still groing strong.

Hopefully it is working now though...


*5/30/17*
Some updates since last night. So I could notfine the second rpi to show on the network, and I assume it is having some of the hanging issues as before. So I decided to just continue with the two nodes for now. However, I wasn't able run ansible with the pi, because generic python needs to be installed. I keep hitting issues with installs failing, and I noticed the updates are giving werird errors with what appears to be kernel related packages. I noticed there is a linux-headers update, so I am running a full `apt dist-upgrade` to see if that fixes anything, although that is also displaying those errors. I think it is a fuckup in a config file...

That seemed to at least get the python problem fixed. I should do a reboot to make sure things didn't get screwed up during the dist-upgrade...
