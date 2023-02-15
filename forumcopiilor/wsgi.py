import os
import sys

try:
  sys.path.remove('/usr/lib/python3/dist-packages')
except:
  pass

sys.path.append('/home/c/cf30363/public_html/forumcopiilor/')
sys.path.append('/home/c/cf30363/venv/lib/python3.6/site-packages/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forumcopiilor.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()