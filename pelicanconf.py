#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = ''
SITENAME = ''
SITETITLE = f'<b> {AUTHOR} </b>'
SITESUBTITLE = ''
RELATIVE_URLS = True
SITEURL = ''
#GOOGLE_ANALYTICS = ""

PATH = 'content'
THEME = 'Flex'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

#Flex Theme
FAVICON = SITEURL + "/images/favicon.png"
SITELOGO = SITEURL + "/images/profile.png"
THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
MAIN_MENU = False

PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()


#Menu off for the work website - use side menu
# MENUITEMS = [
#     ('Home', '/'),
#     ('Archives', [
#         ('Tags', '/tags.html'),
#         ('Categories', '/categories.html'),
#         ('Chronological', '/archives.html'),
#         ]),
#     ('Social', [
#         ('Email', 'mailto: email@email.com'),
#         ('Github', 'http://url-to-github-page'),
#         ('Facebook', 'http://url-to-facebook-page'),
#         ]),
#     ]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
