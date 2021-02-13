title: Corona Virus Diary, Part 101
date: 2021-02-13
category: News

Today I decided to try to make some old computers I have talk to each other.

The first thing I did was spin up a local web server. This gave me a website
viewable over my local network.

Python web server
----------------

Using an old laptop running Linux (Manjaro), I ran

```bash
python3 -m http.server 8000
```

I found my ip address with `ip address`.  It was something like
`192.168.1.NNN`, where `N` is some integer.  I am just doing stuff on a
wireless network, so I looked for my ethernet card thing.

I went onto a browser on another computer (a "normal" Windows machine) on this
same network.  I typed in the URL bar, `192.168.1.NNN:8000`.

My files were visible! Web server started successfully! I have created my own
little digital kingdom!

SSH server
----------

Craving unlimited power, I followed a tutorial by [Austin G.
Walters](https://austingwalters.com/configure-ssh-on-an-arch-linux-server/) on
setting up an SSH server.

Basically this means, I can log into my Linux machine from another computer
(terminal).

Meta Posting
------------

This post is authored using the Linux machine from a Windows machine. Wow!

Motivation
----------

What I'm trying to do is learn more about technology by using many of the tools
already available to me. There are many trends in tech I don't really
like&mdash;e.g.  the "mobile-first" approach and bloated web apps everywhere.
But clearly the Internet can be a very useful tool. So, by looking at networks
and more "backend" type stuff I hope to get the skills to actively work on
engineering the sort of Internet I would prefer. 

