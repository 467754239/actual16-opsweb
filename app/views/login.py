

from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort


from app.common.auth import authentication


mod = Blueprint('login', __name__)


@mod.route('/login', methods=['GET', 'POST'])
def login():
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
