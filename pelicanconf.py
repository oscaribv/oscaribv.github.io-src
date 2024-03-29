# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Oscar Barragán'
SITENAME = "Oscar Barragán's web page"
SITEURL = 'https://oscaribv.github.io'
SITETITLE = 'Oscar Barragán'
SITESUBTITLE = 'Ph.D. in Physics and Astrophysics'
FAVICON = 'https://raw.githubusercontent.com/oscaribv/oscaribv.github.io/master/images/io.jpg'
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True

THEME = '/home/barraganl/Dropbox/Projects/flex'

COPYRIGHT_NAME = 'Oscar Barragán'

PATH = 'content'
ARTICLE_PATHS = ['astroaventuras','tutorials','exoplanets']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

OUTPUT_PATH = '../oscaribv.github.io'

GOOGLE_ANALYTICS = 'UA-108009879-1'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

## Enable i18n plugin.
#PLUGIN_PATHS = ['/home/barraganl/Projects/pelican-plugins', ]
#PLUGINS = ['i18n_subsites', ]
#JINJA_ENVIRONMENT = {
#    'extensions': ['jinja2.ext.i18n'],
#}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#Items to appear in top menu
MENUITEMS = (('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)
# Blogroll
LINKS = ( ('Publications','https://bit.ly/3uSSLO7'),
          ('ORCID','https://orcid.org/0000-0003-0563-0493'))

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/oscaribv'),
          ('github', 'http://github.com/oscaribv'),
          ('linkedin', 'https://www.linkedin.com/in/oscaribv/'),
          ('flickr', 'https://www.flickr.com/photos/oscaribv/'),
          )

DEFAULT_PAGINATION = 10

THEME_COLOR = 'light'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = 'vim'
#PYGMENTS_STYLE_DARK = 'monokai'

#Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
