import sys
import site
import os

site.addsitedir('/var/www/kundeservice/env/lib/python3.13/site-packages')

sys.path.insert(0, '/var/www/kundeservice')

os.chdir('/var/www/kundeservice')

os.environ['VIRTUAL_ENV'] = '/var/www/kundeservice/env'
os.environ['PATH'] = '/var/www/kundeservice/env/bin:' + os.environ['PATH']

from app import app as application
