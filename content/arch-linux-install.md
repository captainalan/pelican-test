title: Arch Linux Install for n00bs
date: 2019-06-02
category: Linux

In this tutorial, I will go through installing Arch Linux. These instructions
were tried out on both a virtual machine and an old laptop. We will do a base
installation of Arch Linux and then run [Luke Smith's](https://lukesmith.xyz)
[LARBS](https://larbs.xyz/) script to get an awesome i3 tiling window manager
setup from the outset.

I'm assuming similar steps would apply for installing Arch Linux on
a real machine, but I haven't tested these instructions out IRL yet.

I am closely following [Full Arch Linux Install (SAVAGE Edition!)
Linux](https://www.youtube.com/watch?v=4PBqpX0_UOc) by Luke Smith (March 8,
2018) to get started.

## Prerequisites

This tutorial is aimed at people with some exposure to Linux and/or command
line tools (e.g. using `brew` under MacOS), but who would like to gain
greater control of their current computing setups. Here, I honor the maxim
that *knowledge is power* and seek to empower you by getting you started
using Arch Linux and understanding the tools that you are using.

(Vim stuff)

## Installation Medium

Download the latest Arch linux ISO. The easiest thing to do is probably to
download from an HTTP mirror near your (physical) location and then install by CD, DVD, or USB.

From Windows, creating your installation medium is easy. Right click on the
downloaded `.iso` file and select "Burn disc image" to create CD or DVD to
create a your installation medium.

(**TODO**: UEFI? Using USB? Add details later...)

## Booting with the installation medium

Restart your computer. You may have to go into your system BIOS to make sure you can boot from your installation medium.

### Get an internet connection

If you are already connected to the Internet via an ethernet cable, there is
nothing to think about. If you are connecting via Wi-Fi, run:

```bash
wifi-menu
```

I can't help you anymore if you are connecting from McDonald's wifi... But on
a home network, you will be prompted for your Wi-Fi network's password.
Once you go through the options `wifi-menu`, try out your network connection
with something like `ping google.com`. Type `ctrl-c` to exit when you are
done.

### Time and date stuff

Run `timedatectl set-ntp true`.

(**TODO**: Insert more details on what this means)

## Partitioning your drive(s)

Now, let's partition our disks. **Note**: I am assuming you are installing
Arch Linux on a computer you are OK with deleting all data on.

Before you do anything else, run `lsblk` to "list all block devices".

### Creating new partitions

From `lsblk`, you can identify the drive you want to install Arch Linux on.
This will probably be `/dev/sda` if you are installing onto an old computer.

To begin, type `fdisk /dev/sda`, where '"`sda`" of course is the drive you
wish to create a new partition table on. You will now be sent to a new prompt
that looks something like:

    Command (m for help):

If there are existing partitions you may need to type `d` to delete them.
Type `p` to print partitions. Once you are done deleting existing stuff, type
`n` at the prompt to make a new partition.

We will now create the following partitions:

- Boot partition (200MB)
- SWAP partition (how much RAM you have, times 1.5)
- Root (25 GB or more)
- Home (everything else)

After typing `n`, you will be be prompted with a number of options. To create
the Boot partition, accept the first default option (`p`) to create a new
primary partition. Accept `1` as the default partition number. Accept the
default "First sector" location. For the "Last sector", enter `+200M`. This means will be the *boot* partition which we are allocating 200 MB for.

Next, we will craete a **swap partition**. Type `n` again to get started.
Standard practice is to create a swap partition of about 1.5-2 times the
amount of RAM you have. I'll be using 4 GB for this. Accept the default
partion number (probably 2), default first sector, and for the last sector do
`+4G` (where you replace "4" with however much memory you select for your
swap partition).

We will now create a **root partition** where all your programs will be
installed. A reasonable starting size for this is around 25 GB, though you
may need more if you like to install a lot of programs. I'll be using 64 GB.
Typing `n` (and then pressing Enter), I accept the default for the partiton
number and the starting sector and then select `+64G` for the last sector.

Finally, we need to create a **home partition** which will take up the rest
of your disk. Do `n` for a new partition and then selct `p` (rather than `e`)
to create a new primary partition. Then, accept all the defaults that follow.

We have now created four nice partitions using `fdisk`. However, these are
not "commited" to disk yet. Write `w` at the `Command (m for help):` prompt
to write your partitions to your disk. Note that this will wipe everything on the disk.

**Note** since we partitioned our disk, you can easily install a different linux distribution if you wanted; just re-write the `root` partition and all your `home` files will still be there.

Type `lsblk` to see how `fdisk` changed your harddirve.

## Making filesystems

We just partitioned our disks, but we need to set **filesystems** to our
partitions.

The `boot`, `root`, and `home` partition (`sda1`, `sda3`, and `sda4` if you
have been following the tutorial for) should be formatted to `ext4`, a Linux
standard.

Do `mkfs.ext4 /dev/sda1`, `mkfs.ext4 /dev/sda3`, and `mkfs.ext4 /dev/sda4` to
set these partitions' filesystems.

Now, for the swap partition do `mkswap /dev/sda2`.

## Mounting stuff

Now that we have created partitions with appropriate filesystems, we need to
**mount** things.

First, do `mount /dev/sda3 /mnt` to mount your root partition.

**Note** at any point during this tutorial you may want to run `lsblk` to see
*how your disks currently look.

Type `ls /mnt`. You should see something like `lost+found` there.

Let's make make some new directories to mount stuff. First do
`mkdir /mnt/boot` create a mount point for our boot partition. Then, run
`mount /dev/sda1 /mnt/boot` to do the actual mounting.

Finally, do `mkdir /mnt/home`. Run `mount /dev/sda4 /mnt/home` to mount your
home partition.

## Installing the base system

We now have all of our partitions and have mounted these partitions on our
file systems. Mounting allows us to modify the data on these partitions,
which means we can install softare (like Arch Linux!).

Run `lsblk` to see that all is as it should be.

### The fun starts with `pacstrap`

Run `pacstrap /mnt base base-devel` to install the base package and basic
development tools. If you want more things, add them like so to this command.

```bash
pacstrap /mnt base base-devel vim emacs
```
Running this command might take a while because it is installing an entire
base system.

## Making an `fstab` file

Earlier, we mounted a bunch of partitions manually. An `fstab` file tells
Linux what to try to load (see `etc/fstab`). Run `genfstab /mnt`. This will
generate an `fstab` file based on how `mnt` looks. Running this command will
just output a bunch of stuff.

We need to save these things to a file. Run
`genfstab -U /mnt >> /mnt/etc/fstab`.

Now Arch Linux will know what goes where.

## Making our installation bootable

Run `arch-chroot /mnt` to change our root. This will change our Arch root to
our new `/mnt` directory! Before, we were running from our installation
medium, now we are running from our actual installation!

### I needs Interwebs

Let's install some stuff. First, let's install `NetworkManager` by typing `pacman -S networkmanager`.

Next, type `systemctl enable NetworkManager` to start `NetworkManager`
whenever you log in.

### GRUB Bootloader

Run `pacman -S grub` to install GRUB, our bootloader. This is important!

After this finishes, run `grub-install --target=i386-pc /dev/sda`.

Once this is done, do `grub-mkconfig -o /boot/grub/grub.cfg` to make a config
file. (This might be done automatically.)

### Setting a password

Run `passwd` to set a root password.

### Setting a locale

Use your text editor (here I use `vim`) to edit `/etc/locale.gen`. I do this
with `vim /etc/locale.gen`. In this huge list of locales I uncommented

    #en_US.UTF-8 UTF-8
    #en_US ISO-8859-1

to...

    en_US.UTF-8 UTF-8
    en_US ISO-8859-1

...in order to set my locale. Note, you can set multiple languages. Save and
exit this file.

Next, run `locale-gen` to read the conf file you just edited and generate a
file.

Let's edit one more file to set our (default) language: `vim
/etc/locale.conf`. I changed the contents of this file to:

    LANG=en_US.UTF-8

### Setting a timezone

By default, in `/etc/localtime`, there are a bunch of time zones. We want to
link `/usr/share/zoneinfo/` with our timezone.

```
ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
```

...where of course you replace `.../America/Los_Angles...` with where you are.

If you travel somewhere else, you will rerun the `ln...` command here to the
timezone of wherever you are going.

### Setting a hostname

Finally, you need to set a name for your computer. Edit `/etc/hostname` to
whatever you like. I will do `vim /etc/hostname` and enter `arch-sama` for a (weeby) hostname.

### Going back to your installation medium...

Type `exit` to go back to your installation medium.

Then, to be safe type `umount -R /mnt` to unmount your Arch installation (on
your harddrive).

### Reboot!

Type `reboot`. Remove your installation medium. You should boot to your new
installation.

## LARBS

Here is the easy part. To get a pretty cool configuration right away, use
Luke Smith's [LARBS](https://larbs.xyz) setup.

Booting your new Arch setup, login as `root`. You'll be prompted for your
password.

Next, run

```bash
curl -LO larbs.xyz/larbs.sh  # Download the script
bash larbs.sh                # Run the script you just downloaded!
```

### Logging in

Login with the username and password you set in LARBS. To modify your system,
you'll probably need to use `su` and the password you set for root in the
Arch install.

### Troubleshooting

If you aren't connected to the Internet, this step can be a pain in the ass.
Search the Arch Wiki for wisdom.
