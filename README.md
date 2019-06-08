# Getting Started with Pelican (Static Site Generator)

See this site deployed on [GitHub
Pages](https://captainalan.github.io/pelican-test/).

## Setting up

시작이 빈이다  
"Starting is half the battle"

### Pre-requisites

All instructions below assume you are working with WSL under Windows.
Similar steps probably work on all UNIX based systems, including MacOS.

I will assume basic working knowledge of Python, Markdown, HTML/CSS and client
side JavaScript.

### Installing things

You need a working installation of Python (3) and `pip` to use Pelican. In the
[official Pelican docs](http://docs.getpelican.com/en/3.6.3/install.html) there
are some instructions for setting up a virtual environment:

    virtualenv ~/virtualenvs/pelican
    cd ~/virtualenvs/pelican
    source bin/activate

This way of going about things is good because you can just activate this same
virtual environment when working with any of your Pelican projects.
Next, do

    pip install pelican
    pip install Markdown
    pip install ghp-import

You can now run `make github` to build the site.

(Depending on your installation(s) of Python, you may have to do something like
`python3 -m virtualenv ~/virtualenvs/pelican` to explicitly call `virtualenv` as
a module using a particular version of Python)

To get GitHub Pages to work, you need to install `ghp-import`.
Then, just run `make github`.
