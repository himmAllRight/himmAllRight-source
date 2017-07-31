{:layout :post
:title  "Dabbling with GO"
:date "2017-07-29"
:author "Ryan Himmelwright"
:tags ["Dev" "GO" "Programming"]
:draft? false
}

After spending most of this month's dedicated learning time working on [system](../solus-to-fedora/), [server](../creating-a-git-remote/), and [network](../issues-setting-up-ubiquiti-network/) activities,  I have been itching to start some home programming again. To motiviate myself, I even considered dabbling with a new programming language...  with very little internal debate, I decided to just [Gopher](https://golang.org) it (I'm so sorry).

<!-- more -->

## What is GO
<img src="../../img/posts/dabbling-with-go/gopher.png" style="width: 30%; float: right; margin: 0px 10px 0px 10px;"/)

Go (sometimes referred to as "golang") is an open source programming language, developed in 2007 by a team at Google (Robert Griesemer, Rob Pike, and Ken Thompson). Distributed under a [BSD-like license](https://golang.org/LICENSE), Go is also maintained and developed by open source volunteers all over the world. 


Like C, it is a compiled and statically typed language. Unlike C, Go includes garbage collection and memory safety features, as well as other design aspects that are more reminiscent of modern dynamic languages like python (ex: type inference and package `import` statements). Lastly, Go has a concurrent programming implementation that utilizes what are known as '[goroutines](https://tour.golang.org/concurrency/1)'. Goroutines are special light-weight "threads" that enable many concurrent taks to run. All of these features work togeather to form an extremely relevant language for modern computing.

Like the programming language itself, the Go project summarizes all of this in a nice and consice statement on their [documentation page](https://golang.org/doc/):

> The Go programming language is an open source project to make programmers more productive.
>Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of garbage collection and the power of run-time reflection. It's a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language. 

## Motivation to Try

I've wanted to try [GO](https://golang.org/) for a long time now. A couple of months ago, I was trying to decide if I should persue learning Rust or GO. At the time, I ultimately ended up experimenting with [Rust](https://www.rust-lang.org/en-US/). I was toying with the idea of creating an experimental lisp, and Rust's feature set makes it great language for writting compiliers and interpreters. However, while Rust is a great language, it can be quite complicated to learn. Go on the otherhand, is apparently simplier and quick to grasp, which is [why it was created](https://golang.org/doc/faq#creating_a_new_language) in the first place.

When the Solus team [announced](https://solus-project.com/forums/viewtopic.php?f=13&t=2634) that it making Go a first class language of the project, my interest peaked higher. [Solbuild](https://github.com/solus-project/solbuild), the Solus package build system was written in Go. In the announcement, the project stated that they intentded to use Go for building tools. True to that statement, this past week, Ikey (the creator of Solus) published a patreon post detailing the new repo manager ([ferryd](https://github.com/solus-project/ferryd)) he's been working on... again in Go. Time for me to give it a Go (again, very sorry).


## Installing

I first went to the golan [install page](https://golang.org/doc/install) to figure out if there was any odd things to install. It didn't appear so. I should also point out that if you just want to try out go, they have an little embded GO editor on the homepage of the website. Beyond that, they have an amazing [Go tour](https://tour.golang.org/welcome/1) that can be completed entirely in a web browser. After playing online for a bit, I decided I wanted to install it on my system.

I was on my NixOS laptop at the itme, so I installed go with the command: 

```
nix-env -i go
```

On Alakazam, it was

```
sudo dnf install golang
```

*(... and then when I jumped back to Solus on Alakazam, it was `sudo eopkg it golang`... but more on that later...)*

I then walked through the [test your install](https://golang.org/doc/install#testing) steps, and built a simple "hello world" app to make sure it was working properly. This was especially important, given that I was on nixOS which can sometimes be picky with system paths and such. Luckily, everything worked fine. If I continue down the go path, I might write a "Getting" started post detailing how to setup a proper Go environment on Linux.


## First Steps
After confirming my install, I went back and looked at the [Learning Go section](https://golang.org/doc/#learning) of the documentation. The first item was [A Tour of Go](https://tour.golang.org/welcome/1) so I started there (Although I am really interested to eventually get to the [effective go](https://golang.org/doc/effective_go.html) documentation).

After working on the tutorial for awhile, I started around with the language own.  Below is a snippet of code I wrote while fooling around. It really is easy to pick up the basics and get going. I am excited to learn more.

```
package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Printf("hello, world\n")
	getOS()
	fmt.Printf("\n") // I know this is dumb

	x, y := 74, 83
	sum := sumInts(x, y)
	fsum := factorial(sum)

	fmt.Printf("sum: %v\n", sum)
	fmt.Printf("Factorial of sum(%v): %v\n", sum, fsum)
}

func sumInts(x int, y int) int {
	sum := x + y
	return sum
}

func factorial(n int) int {
	if n <= 1 {
		return 1
	} else {
		return n + factorial(n-1)
	}
}

func getOS() {
	os := runtime.GOOS
	fmt.Printf("OS: %v\n", os) // impure
}

```
