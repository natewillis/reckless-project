from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['recklessanalysis.com','www.recklessanalysis.com', '137.184.98.238', 'localhost']

# STATIC FILES
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
