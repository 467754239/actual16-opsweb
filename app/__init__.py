
import logging

import MySQLdb as mdb
from flask import Flask, session, g, render_template
from flask_script import Manager



app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = 'oF\xd3I\x98\xe5\xb4\x1a\xfb\xc77\xe3\xcc,\xc2\xd2\x05\x8b\xa9\x9b\x01\xa0t\x0f\x04\x11\x19\xcd4\x96\x8d\x14'
app.debug = True
manager = Manager(app)


# Logging Handler
handler = logging.FileHandler(app.config['LOGFILE'], encoding='UTF-8')
handler.setLevel(logging.DEBUG)
logging_format = logging.Formatter(
        '[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)


# DB connect
conn = mdb.connect(
          host     = '127.0.0.1',
          user     = 'root',
          passwd   = '123456',
          db       = 'actual16',
          charset  = 'utf8' 
      )

cursor = conn.cursor()
conn.autocommit(1)
app.config['cursor'] = cursor



# view
from app.views import dashboard
from app.views import login 
from app.views import users 



app.register_blueprint(dashboard.mod) 
app.register_blueprint(login.mod) 
app.register_blueprint(users.mod) 

