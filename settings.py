# Django settings for ddtcms project.
import os

from datetime import datetime
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
# DEBUG =False
DEBUG =True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS


DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = './data.db'             # Or path to database file if using sqlite3.
#DATABASE_NAME = './examples.db'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.


# e-mail settings
DEFAULT_FROM_EMAIL  = ''
EMAIL_HOST          = ''
EMAIL_HOST_USER     = ''
EMAIL_HOST_PASSWORD = ''

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'zh-CN'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT           = os.path.join(PROJECT_DIR,'media')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/media/'


STATIC_CSS           = os.path.join(MEDIA_ROOT,'css')
STATIC_JS            = os.path.join(MEDIA_ROOT,'js')
STATIC_IMAGE         = os.path.join(MEDIA_ROOT,'images')
STATIC_THEMES        = os.path.join(MEDIA_ROOT,'themes')
STATIC_UPLOAD        = os.path.join(MEDIA_ROOT,'upload')
STATIC_EDITOR        = os.path.join(MEDIA_ROOT,'editor')

PHOTOLOGUE_DIR       = os.path.join(MEDIA_ROOT,'upload','photos','%s' % datetime.now().strftime("%Y/%m/%d"))
ATTACHMENT_DIR       = os.path.join(MEDIA_ROOT,'upload','attachments','%s' % datetime.now().strftime("%Y/%m/%d"))

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$pjbv(g)*a5#d*hwppus!m0f=fjslg*4r*$!q6=tzu8zvbv0j('
SESSION_COOKIE_NAME = 'sessionid.ddtcms'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
'django.core.context_processors.auth',
'django.core.context_processors.debug',
'django.core.context_processors.i18n',
'django.core.context_processors.media',
#'django.core.context_processors.request',
"navbar.context_processors.crumbs",
"navbar.context_processors.navbar",
"navbar.context_processors.navtree",
"navbar.context_processors.navbars",
"member.context_processors.site",
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'ddtcms.urls'

# the theme name ' yaml,'
THEME_NAME = 'yaml'
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR,'templates','themes','%s' % THEME_NAME),
    os.path.join(PROJECT_DIR,'templates'),
)


LOCALE_PATHS =(
    os.path.join(PROJECT_DIR,'locale'),
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.comments',
    'django.contrib.markup',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'ddtcms.home',
    'ddtcms.blog',
    'ddtcms.notice',
    'ddtcms.news',
    'ddtcms.polls',
    'ddtcms.forum',
    'ddtcms.faq',
    'ddtcms.captcha',
    'ddtcms.link',
    'ddtcms.common',
    'ddtcms.member',
    'ddtcms.saying',
    'ddtcms.people',
    'ddtcms.todo',
    'ddtcms.guestbook',
    'photologue',
    'navbar',
    'tagging',
    'attachments',
)


#AUTH_PROFILE_MODULE='userprofile.profile' #2009-3-8 4:35:54
AUTH_PROFILE_MODULE= 'member.profile'
LOGIN_URL          = '/member/login/'
LOGOUT_URL         = '/member/logout/'
LOGIN_REDIRECT_URL = '/member/profile/'


ACCOUNT_ACTIVATION_DAYS=10

LISTITEM_PER_PAGE=10

#navbar settings BEGIN
NAVBAR_TREE_MAX_DEPTH = 3
NAVBAR_TREE_SHOW_DEPTH = 0
NAVBAR_TREE_MARK_SELECTED = True

NAVBAR_MAX_DEPTH = 3
NAVBAR_MARK_SELECTED = True
NAVBAR_SHOW_DEPTH = 0
CRUMBS_HOME = False
NAVBAR_CRUMBS_HOME = 'Home'
#navbar settings END


# START of django-profile specific options

I18N_URLS = False
DEFAULT_AVATAR_WIDTH = 96
DEFAULT_AVATAR = os.path.join(MEDIA_ROOT, 'images','avatars', 'generic.jpg')

AVATAR_WEBSEARCH = False
# 127.0.0.1:8000 Google Maps API Key
GOOGLE_MAPS_API_KEY = "ABQIAAAA06IJoYHDPFMx4u3hTtaghxTpH3CbXHjuCVmaTc5MkkU4wO1RRhST5bKY_U7dUG1ZGu1S-n-ukXGNjQ"
REQUIRE_EMAIL_CONFIRMATION = False
#GEOIP_PATH = "%s/db/" % PROJECT_PATH
# END of django-profile specific options

COMMENTS_ALLOW_PROFANITIES=False
PROFANITIES_LIST=(
                  'Fuck',
                  )

IGNORABLE_404_STARTS = ('/cgi-bin/', '/_vti_bin', '/_vti_inf','/')
IGNORABLE_404_ENDS = ('mail.pl', 'mailform.pl', 'mail.cgi', 'mailform.cgi', 'favicon.ico', '.php')
