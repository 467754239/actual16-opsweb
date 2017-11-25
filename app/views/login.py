

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
from flask_mail import Message

from app import mail
from app.common.auth import authentication


mod = Blueprint('login', __name__)


@mod.route('/login', methods=['GET', 'POST'])
def login():

    msg = Message("Hello", sender="13260071987@163.com", recipients=["467754239@qq.com"])
    mail.send(msg)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authentication(username, password):
            session['sign'] = username
            return redirect("/")
        else:
            errmsg = "Incorrect username or password."
            return render_template('login.html', errmsg=errmsg)
    else:
        return render_template('login.html')
