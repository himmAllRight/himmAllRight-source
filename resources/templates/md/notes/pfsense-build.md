{:layout :post
:title  "Building a pfsense Router"
:date "2017-06-15"
:author "Ryan Himmelwright"
:tags ["Homelab" "Network" "pfsense" "customization"]
:draft? false
}

While I was away for a week to attend my College Swim team Reunion, and my Brother's high school graduation, the router Rebecca and I were using died. It was a Lynksys ??????. When I got home, I setup our old router as a temporary fix. It's a very basic Lynksys ????. After using it for a day, I remember why I hated it so much. It is terribly slow, and seems to stop working each day (I think it is something with DHCP. It keeps trying to reassign ips to devices, and then doesn't seem to understand how to accept their requests after. It's a stupid piece of shit.), requiring me to unplug and replug it daily. So obviously, the more *temporary* this solution, the better.

If I am revisiting our network setup, I want to do it *correctly* this time, and split out the router from the wireless access point using *good* hardware and software. So my plan is, to build a pfsense router, and pair it with an ubiquiti wireless access point.

<!-- more -->


