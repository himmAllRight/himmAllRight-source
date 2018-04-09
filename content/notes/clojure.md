+++
title  = "Clojure Notes"
date   = "2018-04-20"
author = "Ryan Himmelwright"
image  = "img/header-images/container-building-umich.jpg"
tags   = ["Programming", "Linux", "LISP", "Clojure",]
draft  = true
+++

I have started to get into clojure again. This is just a spot for me to take
notes for now. I *might* eventually form this into a post somehow...

But for now.. it's just my notes as I work through some tutorials.

## Install Clojure

`lein` setup

maybe install Java if not already?

## Configuring and Using Spacemacs Cider


## Language

- Normal lisp syntax, for the most part
  - Parens
  - no `,`
  - Operator followed by operands (prefix**
  - Simple, Nested structure
  
  **NOTE: I'll probably keep comparing clojure to common-lisp... since that's
  what I know and use at my day job.**
  
### Control Flow

#### If

`if` seems to work the same as in common lisp, and has the form:

>(if boolean-form
>    then-form
>    optional-else-form)

So, the first thing provided is the boolean form. If it evalutates to `true` (or
a "truthy" value, just as in Common Lisp), the second form is evaluated and
returned. Otherwise, the second form is evaluated and returned (if provided.
Otherwise, returns `nil`).

```clojure
user> (if true
        "True Condition"
        "False Condition")
=> "True Condition"
user> (if false
        "True Condition"
        "False Condition")
=> "False Condition"
```

Notice that just as in common lisp, both the if and else conditional branches
can only have one form. The way around this in common lisp is to wrap multiple
forms using a function like `progn`, a `let` closure, or to use `if*` instead
(my preferred method recently). In clojure, `do` can be used.

#### do

Do wraps up multiple forms into a single one and evaluates them, returning the
last item, *much* like `progn` in common lisp. As stated above, this is be used
in an `if` to place multiple forms in the *if* or *else* conditional branches:

```clojure
user> (do
        (println "Print this line")
        (println "And also this line...")
        "return this line")
=> Print this line
=> And also this line...
=> "return this line"
```

#### when


