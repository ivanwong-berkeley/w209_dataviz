import os, sys

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

activate_this = PROJECT_DIR + '/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

sys.path.append(PROJECT_DIR)

from web import routes
from web import app as application
