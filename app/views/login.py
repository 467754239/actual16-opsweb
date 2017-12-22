
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
@app.before_request
def before_request():
    remote_addr = request.remote_addr
    app.logger.debug("Remote address:%s." % remote_addr)
    #if remote_addr in app.config['PERMISSION_POOL']:
    #    abort(403)
    #return jsonify({'ip': remote_addr}), 404 
    # if 'logged_in' not in session and request.endpoint != 'login':
    #    return redirect(url_for('login'))
    # print "--------endpoint: ", request.endpoint 

    # http://flask.pocoo.org/docs/0.12/api/#flask.session.permanent
    # https://www.jordanbonser.com/flask-session-timeout.html
    session.permanent = True  # False
    app.permanent_session_lifetime = datetime.timedelta(minutes=30)	# default 31days
    session.modified = True


@app.after_request
def after_request(response):
    #print request.endpoint
    #print request.host_url
    #print request.headers
    url = request.url
    app.logger.debug("After_request, session:%s." % session)
    if session.has_key("sign"):
        username = session['sign']['username']
    else:
        username = None
    app.logger.debug("After_request, url:%s, username:%s." % (url, username))
    return response


@mod.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        loginInfo, dbok = authentication(username, password)
        github_loginInfo, github_ok = github_auth(username, password)
        app.logger.info('login info:%s, ok:%s' % (loginInfo, dbok))

        if dbok or github_ok:
            role, cn_name = get_role_from_username(username)
            if role:
                session['sign'] = { 'username' : username, 'role' : role, 'cn_name' : cn_name }
            else:
                session['sign'] = { 'username' : username, 'role' : None, 'cn_name' : 'cn_name'}
            return jsonify({"code" : 0, 'errmsg' : None})
        else:
            return jsonify({"code" : -1, 'message' : loginInfo})
    else:
        return render_template('login.html')



@mod.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    session.clear()
    return redirect('/login')
