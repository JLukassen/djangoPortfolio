import sys
import os

# Activate the virtual environment
activate_env = os.path.expanduser('/home/jonlzvml/virtualenv/public_html/jonlukassen_resume/3.9/bin/activate_this.py')
with open(activate_env) as f:
    exec(f.read(), {'__file__': activate_env})

# Add the project directory to the sys.path
sys.path.append('/home/jonlzvml/public_html/jonlukassen_resume')

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'jonlukassen_resume.settings'

# Import the application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
