# My Blog Using Pelican (Static Site Generator)

I started this blog to try out
[Pelican](https://github.com/getpelican/pelican).  As I've made somme
hard links to this blog, I'm decided to keep deploying stuff to the
published site on [GitHub
Pages](https://captainalan.github.io/pelican-test/).

## Pre-requisites

I will assume basic working knowledge of Python, Markdown, HTML/CSS and client
side JavaScript.

## Setting up

시작이 빈이다  
"Starting is half the battle"

### Installing Pelican

You need a working installation of Python (3) and `pip` to use Pelican. In the
[official Pelican docs](http://docs.getpelican.com/en/3.6.3/install.html) there
are some instructions for setting up a virtual environment:

    virtualenv ~/virtualenvs/pelican
    cd ~/virtualenvs/pelican
    source bin/activate

On Ubuntu, which has Python 2 (under the `python` command) by default
the last time I tried it, I had to first install the `python3-pip`
package (via `sudo apt install python3-pip`) and then do `pip3 install
virtualenv`. Only then could I do...

```bash
python3 -m virtualenv ~/virtualenvs/pelican
# etc etc
```

...following the same steps as above. Ughh! Versioning!

### Using your `virtualenv`

When working on any of your Pelican projects, you can use the virtual
enviornment you just made.  Install some packages:

    pip install pelican
    pip install Markdown
    pip install ghp-import

You can now run `make github` to build the site.
On FreeBSD, you may need to use `gmake github`.

### Returning to work

There's probably some indicator in your terminal that you are in a
virtual enviornment (e.g. Ubuntu default theme shows me `(pelican)`)
at the prompt. If you clsoe your window, you're going to have to use
`source bin/activate` from your pelican virtual environment directory
again.

From your project's directory, run `make help` to display some helpful
information for working with pelican.

### Updating software

Make sure your virtual environment is activate. Now enter,

```bash
pip list --outdated
```

...and you will see if you have any outdated packages. You may also
need to update pip itself. As I write this, I just ran,

```bash
python -m pip install --upgrade pip
```

...to upgrade pip.

To upgrade packages, use the `--upgrade` option. Do,

```bash
pip install --upgrade pelican
```

...where `pelican` corresponds to whatever package(s) you want to update.

### Troubleshooting

Using MS Windows you may need to download some extra programs, such as
GNU's `make`. One easy way to do this is to set up a package manager
such as [chocolatey](https://chocolatey.org/). Another alternative is
to use something more UNIX-like such as
[WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) or a
virtual machine running Linux.

Customizing Things
------------------

For themes, check out the
[pelican-themes](https://github.com/getpelican/pelican-themes) Github
repository.
