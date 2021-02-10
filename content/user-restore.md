title: Restoring a user, practical Linux
date: 2021-02-10
category: Linux

I am no Linux guru, but usually if I went to get something done I am
able to. In this post, I will document how I solved a particular
problem in a fast and easy way.

Problem: I really broke my system
---------------------------------

I had a pretty old computer running Arch Linux. I was using Gnome as a
Desktop Environment and stuff was getting pretty slow. I tried to have
a boring, stable setup, but I ended up having a system that got hung
up a lot. So I wanted to remove Gnome and use a lighter-weight desktop
environment thing like LXDE or XFCE. Unfortunately, when uninstalling
Gnome, I did some reckless commands that also uninstalled a bunch of
important packages. So I ended up with a system that couldn't even
connect to the Internet to re-install those packages.

Solution
--------

My solution to this issue was to reinstall my base operating system
but leave my home directory intact. This way I could fix all the
things I wanted to fix and not have to go through some complicated
restoration procedure. While nothing super-important (or not already
backed up online) was on this computer, having to manually re-do a
bunch of configurations and stuff would be no fun, so it was
preferable to repair my existing system rather than starting anew.

### Partitions helped

Fortunately, I had my system set up such that I had a separate root
(`/`) and home (`/home`) partition. So, it would not be too difficult
to isolate those things that needed fixing and those things that did
not.

### Installation

I opted for installing **Manjaro** Linux, an Arch-based distribution.
I downloaded the ISO, used Rufus on a Windows machine to set up a
bootable USB drive, and then entered the graphical installer. I chose
manual partitioning. Doing this, I had to set some "flags" (not sure
on the exact terminology here). Basically I had to tell the installer
where `/`, `/boot` and `/home` were. I reformatted my boot and root
partitions, but left the home partition as it was because I didn't
want to delete my files there.

### User Stuff

That went smoothly. I just used the installer to make a new user. With
that new user, I created a user account for the main user I was using
on my old system using `useradd`. As I didn't want Manjaro to add all
sorts of configuration stuff automatically, I chose to setup this new
user (I'll call it `alan`) from the command line.

I tried logging with `alan` after doing this&mdash;uh-oh! didn't
work. I was returned to Manjaro's login screen thing.

I guessed the problem had to do with permissions. So, I searched up
how to change the permissions of my existing `/home/alan` directory
which was left over from my broken install.

Then, to make sure I could run any command from `alan` via `sudo`, I
needed to edit `/etc/sudoers`. I did this with `sudo visudo
/etc/sudoers` from the account I made with Manjaro. I uncommented the
line giving sudo permissions to the `wheel` group and then I used
`usermod` to add `alan` to the `wheel` group.

### Success

I successfully logged on with `alan`, installed some software, and
wrote this blog post. All my files and stuff are there.

Lessons
-------

The specifics of how to do something in Linux can be mind-numbing. For
this reason, I don't even try to do lots of things&mdash;like dealing
with audio and video issues. However, if you have a basic idea of what
you want to accomplish, doling common tasks like dealing with
partitions and users can be surprisingly easy.

Search engines are good for solving technical problems. If you know
exactly what you want to search for, search engines are very good at
returning you relevant results. Fortunately, Linux problems often
involve weird strings (e.g. program names) that aren't confused with
non-computer things. Usually adding the word "linux" or "arch" or
something easily narrows a search to relevant stuff too.

Through solving real world problems that come up, you can learn more
about how computers work, software is organized, and so on and so
forth. If you choose a lazy option like using an automatic installer
like I did here, you can avoid looking at many things you don't care
to struggle with too.
