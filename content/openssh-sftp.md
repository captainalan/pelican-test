title: Easy File Transfer with OpenSSH
date: 2021-02-14
category: Linux

Today I learned that [OpenSSH](https://www.openssh.com) allows you to easily
transfer files on a local network! I've started setting up some home network
stuff to learn how "the cloud" works better and was pleasantly surprised how
easy this was.

Setup
---------

OpenSSH is the de-facto standard for remote access via `ssh`. So if you want to
log in from one computer to another, chances are you're going to be using
OpenSSH in 2021. [^1]

From a Linux machine, make sure you have a **ssh server** set up. See the
section under **Server usage** on the ArchWiki article on
[OpenSSH](https://wiki.archlinux.org/index.php/OpenSSH).

Filezilla
---------

On Windows, I installed [Filezilla](https://filezilla-project.org). I entered
in the IP address of my home (Linux) server, my username and password and
selected the **SFTP** protocol from Filezilla's easy to use GUI.
I could then easily copy files from my client (Windows) machine to my server
through my wireless network.

Alternatives to "the cloud"
---------------------------

Knowing how to do many "cloud computing" tasks yourself is a practical thing to
learn to take control of your data and understand the "magic" behind services
offered by big tech.

[^1]: This very blog post is being written from a Windows computer connected to
  a FreeBSD system via OpenSSH!
