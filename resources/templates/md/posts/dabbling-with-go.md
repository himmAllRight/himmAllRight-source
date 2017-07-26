{:layout :post
:title  "Dabbling with GOlang"
:date "2017-07-27"
:author "Ryan Himmelwright"
:tags ["Dev" "GO"]
:draft? false
}

## What is GO

Wed 26 Jul 2017 06:26:10 AM EDT
## Reasons
I've wanted to try [GO](https://golang.org/) as I find it to be an interesting potential language for myself. I thought about trying go in the past, but ultimately ended up trying out [rust](https://www.rust-lang.org/en-US/) first. Rust is a great language, although it can be quite complicated to learn. Go on the otherhand, is apparently a bit simplier and quick to grasp. When the Solus project announced that it was a language they are trying to fully support and use for build tools, my interest was peaked higher, but I was busy on other projects at the time. This week, Ikey made a patreon post talking about the new repo manager he's been writting... in go. So, my interest is yet again peaked.

## Installing
I first went to the golan [install page](https://golang.org/doc/install) to figure out if there was any odd things to install. It didn't appear so. I was on my NixOS laptop at the itme, so I installed go with the command: 

```
nix-env -i go
```

On Alakazam, it was

```
sudo dnf install golang
```

I then walked through the [test your install](https://golang.org/doc/install#testing) steps, and built a simple "hello world" app to make sure it was working properly. This was especially important, given that I was on nixOS which can sometimes be picky with system paths and such. Luckily, everything worked fine.


## First Steps
After confirming my install, I went back and looked at the [Learning Go section](https://golang.org/doc/#learning) of the documentation. The first item was [A Tour of Go](https://tour.golang.org/welcome/1) so I started there (Although I am really interested to eventually get to the [effective go](https://golang.org/doc/effective_go.html) documentation)
