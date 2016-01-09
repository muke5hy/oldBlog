#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mukesh'
SITENAME = u'Learning the hard way!'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

PAGINATION_PATTERNS = (
     (1, '{name}/', '{name}/index.html'),
     (2, '{name}/page/{number}/', '{name}/page/{number}/index.html'),
)

TAG_URL = 'tag/{name}/index.html'
CATEGORY_URL = 'category/{name}/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-themes/pure-single"
THEME = "pelican-themes/medius"
# THEME = "pelican-themes/pelican-mediumfox"


STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'gravatar']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}



# Settings for theme pure-singl
SOCIAL = (
    ('github', 'https://github.com/ingenioustechie/'),
    ('twitter-square', 'https://twitter.com/ingenioustechie'),
)
COVER_IMG_URL = "https://pbs.twimg.com/profile_banners/16581688/1428780057/web_retina"
PROFILE_IMG_URL = "https://pbs.twimg.com/profile_images/616609810369368064/NPSrjbIh_bigger.jpg"
DISQUS_SITENAME = 'ingenioustechie'
DISQUS_ON_PAGES = True

DISPLAY_CATEGORIES_ON_MENU = False