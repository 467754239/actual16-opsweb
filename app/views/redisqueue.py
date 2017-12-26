#--*--coding: utf-8--*--

import datetime

from flask import Blueprint
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for
from flask import request
from flask import flash
from flask import g
from flask import jsonify
from flask import abort
from flask import make_response
from flask.ext import excel

from app import app
from app.common.auth import login_required 
from app.common.redis_queue import Redis



import sys
reload(sys)
sys.setdefaultencoding("utf-8")


mod = Blueprint('redisqueue', __name__, url_prefix='/queue')



'''
'''
@mod.route('/', methods=['GET', 'POST'])
@login_required
def queue():
    return render_template('queue/redis.html')
