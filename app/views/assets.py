#--*--coding: utf-8--*--

from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort


from app.common.auth import authentication
from app.common.users import get_user
from app.common.users import get_users
from app.common.users import userDel
from app.common.users import registerUser 
from app.common.users import get_user_from_uid 
from app.common.users import updateUserinfo 

from app import app
from app.common.auth import login_required 



mod = Blueprint('assets', __name__)



'''
    1. GET  查看用户信息
    2. POST 增加用户
'''
@mod.route('/assets', methods=['GET', 'POST'])
@login_required
def assets():

    if request.method == 'GET':
        return render_template('assets/assets.html')

    elif request.method == 'POST':
        app.logger.info(request.form)

        data = request.form.to_dict()
        app.logger.info('data:%s' % data)
        effect_record = registerUser(data)

        app.logger.info('register user result:%s, type:%s' % (effect_record, type(effect_record)) )
        if effect_record == 1:
            retdata = {'code' : 0, 'data' : None, 'message' : 'add user sucess.'}
        else:
            retdata = {'code' : -1, 'data' : None, 'message' : 'add user failed.'}
        return jsonify(retdata)

