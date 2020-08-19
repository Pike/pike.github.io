#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Axel Hecht'
SITENAME = 'Axel Hecht'
SITEURL = ''

PATH = 'content'

THEME = 'attila'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

# Blogroll
LINKS = tuple()

# Social widget
SOCIAL = (
    ("Twitter", "https://twitter.com/axelhecht"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True