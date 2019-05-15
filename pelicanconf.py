#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alan Wong'
SITENAME = 'Trying out Pelican'
SITEURL = 'https://captainalan.github.io/pelican-test/'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Homepage', 'https://captainalan.github.io/me/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('GitHub', 'https://github.com/captainalan'),
          ('Linked In', 'https://www.linkedin.com/in/alan-wong-bb342569/'),
          ('Facebook', 'https://www.facebook.com/captainalan'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
