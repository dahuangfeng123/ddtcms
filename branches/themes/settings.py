# Django settings for ddtcms project.
import os
from datetime import datetime
ROOTDIR = os.path.abspath(os.path.dirname(__file__))
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
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'China/Hubei'

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
MEDIA_ROOT = './media/'

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/media/'


STATIC_PATH='./media/'


STATIC_FILE_UPLOAD_DIR        =STATIC_PATH+'upload/'
STATIC_FILE_UPLOAD_TEMP_DIR   =STATIC_PATH+'upload/tmp/'
STATIC_STYLE                  =STATIC_PATH+'styles/'
STATIC_SCRIPT                 =STATIC_PATH+'scripts/'
STATIC_IMAGE                  =STATIC_PATH+'images/'
PHOTOLOGUE_DIR                ='upload/photo/%s/' % datetime.now().strftime("%Y/%m/%d")

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$pjbv(g)*a5#d*hwppus!m0f=fjslg*4r*$!q6=tzu8zvbv0j('
SESSION_COOKIE_NAME = 'sessionid.ddtcms'


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
"userprofile.context_processors.site",
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

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    './templates/',
    './forum/templates/',
    './blog/templates/',
    './news/templates/',
    './photo/templates/',
    './wiki/templates/',
    './faq/templates/',
    './todo/templates/',
    './polls/templates/',
    './link/templates/',
    './registration/templates/',
    './notice/templates/',
    './life/templates/',
    './navbar/templates/',
    './photologue/templates/',
    './userprofile/templates/',
)


LOCALE_PATHS =(
    './userprofile/locale/',
    './locale/',
    
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
    'ddtcms.category',
    'ddtcms.home',
    'ddtcms.wiki',
    'ddtcms.blog',
    'ddtcms.photo',
    'ddtcms.notice',
    'ddtcms.news',
    'ddtcms.polls',
    'ddtcms.forum',
    'ddtcms.faq',
    'ddtcms.todo',
    'ddtcms.member',
    'ddtcms.captcha',
    'ddtcms.link',
   #'diario',
    'registration',
    'photologue',
    'navbar',
    'userprofile',
    'pressroom',
    'tagging',
    


)


AUTH_PROFILE_MODULE='member.profile'
#LOGIN_URL = '/member/login/'
#LOGOUT_URL = '/member/logout/'
#LOGIN_REDIRECT_URL = '/member/profile/'


ACCOUNT_ACTIVATION_DAYS=10

LISTITEM_PER_PAGE=10

#navbar settings BEGIN
NAVBAR_TREE_MAX_DEPTH = 3
NAVBAR_TREE_SHOW_DEPTH = 0
NAVBAR_TREE_MARK_SELECTED = True

NAVBAR_MAX_DEPTH=3
NAVBAR_MARK_SELECTED=True
NAVBAR_SHOW_DEPTH=0
#navbar settings END


# START of django-profile specific options

I18N_URLS = False
DEFAULT_AVATAR_WIDTH = 96
DEFAULT_AVATAR = os.path.join(MEDIA_ROOT, 'userprofile/avatars/', 'generic.jpg')

AVATAR_WEBSEARCH = False
# 127.0.0.1:8000 Google Maps API Key
GOOGLE_MAPS_API_KEY = "ABQIAAAA06IJoYHDPFMx4u3hTtaghxTpH3CbXHjuCVmaTc5MkkU4wO1RRhST5bKY_U7dUG1ZGu1S-n-ukXGNjQ"
REQUIRE_EMAIL_CONFIRMATION = False
#GEOIP_PATH = "%s/db/" % PROJECT_PATH
# END of django-profile specific options





# django-diario settings

# Number of latest itens on archive_index view. Default: 10.
DIARIO_NUM_LATEST = 8

# Markup language for blog entries. Options: 'rest', 'textile',
# 'markdown' or 'raw' for raw text.
# Default: 'raw'.
DIARIO_DEFAULT_MARKUP_LANG = 'raw'