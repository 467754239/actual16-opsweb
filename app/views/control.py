#--*--coding: utf-8--*--

from flask import Blueprint
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for
from flask import request
from flask import jsonify
from flask import abort
from flask import g
from flask import flash


from app import app
from app.common.auth import login_required 


mod = Blueprint('control', __name__, url_prefix='/control')



@mod.route('/', methods=['GET', 'POST'])
@login_required
def control_index():
    return render_template('control/control.html')

