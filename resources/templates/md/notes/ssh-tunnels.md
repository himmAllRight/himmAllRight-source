I think I will write a quick post about using reverse ssh tunnels. They were always hard to grasp, but now I have them down and use them to connect to my home network. 

I want to do some research to see if this method is actually secure, and how it compares to having open ports/port forwarding. As I start to experiment with my tunnel app, I might include that as well...


Doing some reading, it looks like the golang ssh libraries do not do hostkey checking at this time? At least according to [this article](https://bridge.grumpy-troll.org/2017/04/golang-ssh-security/). That might dampening the security aspects of using Go for the tunnel...

I have start to work on the TunnelBeacon project again. I am doing it in C. Go was a pain to do the GUI stuff, and I also do need a project that uses a real C backend, and maybe a QT C++ frontend. I am reading trough [this really awesome post and example](https://marianafranco.github.io/2017/03/10/libssh2-tunnel/) about how to setup reverse tunnels using the libssh2 library. I got it basically working, but I am having issues fully getting it to work using just keu auth. Also, I would like to be able to supply a hostname (instead of ip) and have it work. It's getting there though and the post does a great job of breaking it down, and I can easily follow it.

I found a [post](http://www.binarytides.com/hostname-to-ip-address-c-sockets-linux/) that helped show how to convert a hostname to an ip. I think it should work for this. I'll just convert the inputs before passing to the backend. If you give it an ip, it just converts it to itself, so it should still work.
