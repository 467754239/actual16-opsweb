
import os
import logging

import MySQLdb as mdb
from flask_mail import Mail
from flask import Flask, session, g, render_template
from flask_script import Manager
from flaskext.markdown import Markdown
from flask_debugtoolbar import DebugToolbarExtension
import flask_excel as excel

from app.common.tokeybase import Token

app = Flask(__name__)
app.config.from_object('config')
app.url_map.strict_slashes = False

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'oF\xd3I\x98\xe5\xb4\x1a\xfb\xc77\xe3\xcc,\xc2\xd2\x05\x8b\xa9\x9b\x01\xa0t\x0f\x04\x11\x19\xcd4\x96\x8d\x14'
app.config['SECRET_KEY'] = os.urandom(24) 

#toolbar = DebugToolbarExtension(app)
#app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

#app.config['PERMANENT_SESSION_LIFETIME'] =  datetime.timedelta(minutes=1)

app.config['max_token_age'] = 1800  # second
app.config['token'] = Token(app.config['SECRET_KEY'], app.config['max_token_age'])

Markdown(app)
mail = Mail(app)
manager = Manager(app)

excel.init_excel(app)

# Logging Handler
handler = logging.FileHandler(app.config['LOGFILE'], encoding='UTF-8')
handler.setLevel(logging.DEBUG)
logging_format = logging.Formatter('[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)


# DB connect
conn = mdb.connect(
          host     = app.config['MYSQLHOST'],
          user     = app.config['MYSQLUSER'],
          passwd   = app.config['MYSQLPASS'],
          db       = app.config['MYSQLDB'],
          charset  = app.config['MYSQLCHARSET'] 
      )

cursor = conn.cursor()
conn.autocommit(1)
conn.ping(True)
app.config['conn'] = conn
app.config['cursor'] = cursor



# view
from app.views import dashboard
from app.views import login 
from app.views import users 
from app.views import assets
from app.views import monitor 
from app.views import error 
from app.views import control
from app.views.v1 import api 



app.register_blueprint(dashboard.mod) 
app.register_blueprint(login.mod) 
app.register_blueprint(users.mod) 
app.register_blueprint(assets.mod) 
app.register_blueprint(monitor.mod) 
app.register_blueprint(error.mod) 
app.register_blueprint(control.mod) 
app.register_blueprint(api.mod) 
