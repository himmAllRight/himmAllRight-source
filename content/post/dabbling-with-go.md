+++
title = "Dabbling with GO"
date = "2017-07-30"
author = "Ryan Himmelwright"
tags = ["Dev", "GO", "Programming",]
+++

After spending most of this month's dedicated learning time working on [system](http://ryan.himmelwright.net/posts/solus-to-fedora/), [server](http://ryan.himmelwright.net/posts/creating-a-git-remote/), and [network](http://ryan.himmelwright.net/posts/issues-setting-up-ubiquiti-network/) activities,  I have been itching to start some home programming again. To motivate myself, I even considered dabbling with a new programming language... and with very little internal debate, I decided to just [Gopher](https://golang.org) it (I'm so sorry).

<!-- more -->

## What is GO?
<img src="../../img/posts/dabbling-with-go/gopher.png" style="width: 30%; float: right; margin: 0px 10px 0px 10px;"/>

Go (sometimes referred to as "golang") is an open source programming language, developed in 2007 by a team at Google (Robert Griesemer, Rob Pike, and Ken Thompson). Distributed under a [BSD-like license](https://golang.org/LICENSE), Go is also maintained and developed by open source volunteers all over the world. 


Like C, it is a compiled and statically typed language. Unlike C, Go includes garbage collection and memory safety features, as well as other design aspects that are reminiscent of modern dynamic languages like python (ex: type inference and package `import` statements). Lastly, Go has a concurrent programming implementation that utilizes what are known as '[goroutines](https://tour.golang.org/concurrency/1)'. Goroutines are special light-weight "threads" that can process many concurrent tasks. All of these features work together to form an extremely relevant language for modern computing.

Like the programming language itself, the Go project summarizes all of this in a nice and concise statement on their [documentation page](https://golang.org/doc/):

> The Go programming language is an open source project to make programmers more productive.
>Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of garbage collection and the power of run-time reflection. It's a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language. 

<a name="motivation"></a>
## Motivation

I've wanted to try [Go](https://golang.org/) for a long time now. A couple of months ago, I was trying to decide if I should pursue learning Rust or Go. At the time, I ultimately ended up experimenting with [Rust](https://www.rust-lang.org/en-US/). I was toying with the idea of creating an experimental lisp, and Rust's feature set makes it great language for writing compilers and interpreters. However, while Rust is a great language, it can be quite complicated to learn. Go on the other hand, is apparently simpler and quick to grasp, which is [why it was created](https://golang.org/doc/faq#creating_a_new_language) in the first place.

When the Solus team [announced](https://solus-project.com/forums/viewtopic.php?f=13&t=2634) that they were declaring Go a first class citizen language of the project, my interest peaked. [Solbuild](https://github.com/solus-project/solbuild), the Solus package build system was written in Go. In the announcement, the project stated that they intended to use Go for building tools. True to that statement, this past week, Ikey (the creator of Solus) published a patreon post detailing the new repo manager ([ferryd](https://github.com/solus-project/ferryd)) he's been working on... again in Go. After reading that post, I decided it was time for me to give it a Go (again, very sorry).


## Installation

I first went to the Go [install page](https://golang.org/doc/install) to figure out if there were any odd components to install. It didn't appear so. 

*Note:* Before progressing any further, I should point out that if you just want to *try* go, the project has a little embedded editor/compiler on the [home page](https://golang.org) of the website. Beyond that, they have an amazing [Go tour](https://tour.golang.org/welcome/1) that also has an embedded programming environment, and can be completed entirely in a web browser.

After playing with the online editor online for a bit, I decided that I wanted to install Go on my system. I was on my NixOS laptop at the time, so I installed go with the command: 

```
nix-env -i go
```

On Alakazam, it was

```
sudo dnf install golang
```

*(... and then when I jumped back to Solus on Alakazam, it was `sudo eopkg it golang`... but more on that later...)*

Next, I walked through the [test your install](https://golang.org/doc/install#testing) steps, building a simple "hello world" app to make sure everything was working properly. This was especially important, given that I was on nixOS, which can sometimes be picky with system paths and environment variables. Luckily, everything worked fine. If I continue down the Go path, I might write a "Getting started" post to detail how to setup a proper Go environment on Linux.

 
## First Steps

After confirming my install, I went back and continued  [A Tour of Go](https://tour.golang.org/welcome/1) to better learn the language. I am interested to eventually read the [Effective Go](https://golang.org/doc/effective_go.html) documentation. It will be interesting to simply *read* the correct style and conventions for the language, instead of trudging through a holly war to find answers.

After working on the tutorial for awhile, I started playing around with the language on my own.  Below is a snippet of code I wrote while fooling around. It's nothing fancy. I was impressed though with how easy it really was to pick up the basics of the language and get going. I am excited to learn more.
  
```go
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
