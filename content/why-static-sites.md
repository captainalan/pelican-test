title: Why Static Sites?
date: 2019-05-15 10:13
category: Interwebs

Updated 8/12/2019

After half a year or so of learning all about dynamic websites (using
fancy new technology like Node.js), I've found myself returning to
good old-fashioned static sites for my personal projects. Here I'll go
through some reasons why.

Two approaches 
--------------

Consider two scenarios:

1. You write a program that produces content for that user when a
   user runs it
2. You write a program that produces content; you then distribute that
   content to people that want it

The first approach here is how a lot of *dynamic* websites work. You
write **server side code** in something like JavaScript (Node), PHP,
Python, etc. to produce webpages on the fly for users. To do this,
you may have to go through lots of trials and tribulations to get your
program ('website') up and running.

The second approach is how *static sites* work. The "programming"
involved (if any) is to generate content once. Compare this to
*compiling* a high(er) level programming language into machine
code. Once you produce useful output, it is easy to distribute it
(there are many places, including GitHub pages, that can serve
**static assets** for free).

With dynamic websites, you might worry about hackers sending malicious
inputs into your website and blowing stuff up. With static websites,
this is not an issue. If you were really worried about one server
where your content is hosted, you could easily create **mirror(s)** of
your content. Static sites deploy easily, without special
considerations about what will compile, what will be allowed,
etc. Everything is packaged up nicely and good to go.

Know your needs
---------------

For most people, static sites will do. Don't be pulled in by the buzz
words and hype of fancy platforms if all you need is some hosting for
HTML/CSS files and some images.


### Priorities

Simplifying web development means having more time available to focus
on producing quality content, rather than wrestling with abstractions
and engineering-ish problems. 

Maybe you should write a math or engineering blog if you wanna do
either of those activities, respectively 😡
