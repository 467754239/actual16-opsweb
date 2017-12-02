
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
from flask_mail import Message

from app import mail
from app import app
from app.common.auth import login_required 
from app.common.auth import github_auth 
from app.common.auth import authentication
from app.common.users import get_role_from_username


mod = Blueprint('login', __name__)


# https://stackoverflow.com/questions/14367991/flask-before-request-add-exception-for-specific-route
#@app.before_request
#def before_request():
#    #if 'logged_in' not in session and request.endpoint != 'login':
#    #    return redirect(url_for('login'))
#    print "--------endpoint: ", request.endpoint 

@mod.route('/login', methods=['GET', 'POST'])
def login():

    #msg = Message("Hello", sender="13260071987@163.com", recipients=["467754239@qq.com"])
    #mail.send(msg)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        loginInfo, ok = authentication(username, password)
        github_loginInfo, github_ok = github_auth(username, password)
        app.logger.info('login info:%s, ok:%s' % (loginInfo, ok))
        if ok or github_ok:
            role = get_role_from_username(username)
            if role:
                session['sign'] = { 'username' : username, 'role' : role[0] }
            else:
                session['sign'] = { 'username' : username, 'role' : None }
            #session['expires'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
            #session.permanent = True
            return redirect("/")
        else:
            return render_template('login.html', errmsg=loginInfo)
    else:
        return render_template('login.html')



@mod.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    session.clear()
    return redirect('/login')
