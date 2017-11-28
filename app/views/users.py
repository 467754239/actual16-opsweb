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



mod = Blueprint('users', __name__)



'''
    1. GET  查看用户信息
    2. POST 增加用户
'''
@mod.route('/users', methods=['GET', 'POST'])
@login_required
def users():

    if request.method == 'GET':
        search_value = request.args.get("search")
        app.logger.info('search_value:%s' % search_value)
        if search_value:
            users = get_user(search_value)
        else:
            users = get_users()
        return render_template('users/users.html', users=users)

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



'''获取指定用户 或者 所有用户信息
'''
@mod.route('/users/info', methods=['GET'])
@login_required
def users_info():
    app.logger.info(request.args)
    retdata = []
    uid = request.args.get('uid', None)
    if uid:
        userinfo = get_user_from_uid(uid)
        app.logger.info(userinfo)
        if userinfo:
            retdata = {'code' : 0, 'data' : userinfo, 'message' : None}
        else:
            retdata = {'code' : -1, 'data' : None, 'message' : 'not found.'}
    else:
        pass
    return jsonify(retdata)



'''删除用户
'''
@mod.route('/users/del', methods=['GET'])
@login_required
def usersDel():
    app.logger.info( request.args  )

    uid = request.args.get('uid', None)
    effect_record = userDel(uid)
    app.logger.info('delete user result:%s, type:%s' % (effect_record, type(effect_record)) )

    if effect_record:
        retdata = {'code' : 0, 'data' : None, 'message' : "delete sucess."}
    else:
        retdata = {'code' : -1, 'data' : None, 'message' : 'not found.'}
   
    return jsonify(retdata)



'''修改用户
'''
@mod.route('/users/edit', methods=['POST'])
@login_required
def usersEdit():

    app.logger.info( request.form )
    data = request.form.to_dict()
    effect_record = updateUserinfo(data) 
    app.logger.info( effect_record )

    if effect_record:
        retdata = {'code' : 0, 'data' : None, 'message' : "update sucess."}
    else:
        retdata = {'code' : -1, 'data' : None, 'message' : 'not found.'}
   
    return jsonify(retdata)
