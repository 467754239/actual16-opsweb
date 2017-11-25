

from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort


from app.common.auth import authentication
from app.common.users import get_user
from app.common.users import get_users

from app import app



mod = Blueprint('users', __name__)


@mod.route('/users', methods=['GET', 'POST'])
def users():

    if request.method == 'GET':
        app.logger.info('info log--------------------------')
        if not session.get('sign', None):
            return redirect('/login')
        search_value = request.args.get("search")
        if search_value:
            users = get_user(search_value)
        else:
            users = get_users()
        return render_template('users/users.html', users=users)

    elif request.method == 'POST':
        
        app.logger.info(request.form)
        retdata = {'code' : 0, 'data' : None, 'message' : 'add user sucess.'}
        return jsonify(retdata)
