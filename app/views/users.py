#--*--coding: utf-8--*--

from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort


from app.common.auth import authentication
from app.common.users import get_user
from app.common.users import get_users
from app.common.users import get_users_count 
from app.common.users import userDel
from app.common.users import registerUser 
from app.common.users import get_user_from_uid 
from app.common.users import updateUserinfo 
from app.common.users import validate_user_exists

from app import app
from app.common.auth import login_required 


mod = Blueprint('users', __name__, url_prefix='/users')



'''
    1. GET  查看用户信息
    2. POST 增加用户
'''
@mod.route('/', methods=['GET', 'POST'])
@login_required
def users():

    if request.method == 'GET':
        return render_template('users/users.html', users=get_users())

    elif request.method == 'POST':
        data = request.form.to_dict()

        # 删除不必要的字段
        data.pop('rpassword', None)
        app.logger.info('add user, data:%s' % data)

        # 验证用户是否存在
        username = data.get('username')
        valid_info, valid_status = validate_user_exists( username )
        app.logger.debug("valid_info:%s, valid_status:%s." % (valid_info, valid_status))
        if valid_status:
            response = {'data' : None, 'message' : valid_info, 'code' : -1}
            return jsonify(response)

        effect_record = registerUser(data)
        app.logger.info('register user result:%s, type:%s' % (effect_record, type(effect_record)) )
        if effect_record == 1:
            response = {'data' : None, 'message' : 'add user sucess.', 'code' : 0}
        else:
            response = {'data' : None, 'message' : 'add user failed.', 'code' : -1}
        return jsonify(response)



'''获取指定用户 或者 所有用户信息
'''
@mod.route('/info', methods=['GET'])
@login_required
def users_info():
    app.logger.info(request.args)

    uid = request.args.get('uid', None)
    if not uid:
        response = {'data' : None, 'message' : valid_info, 'code' : -1}
        return jsonify(response)

    userinfo = get_user_from_uid(uid)
    app.logger.info(userinfo)
    if userinfo:
        response = {'data' : userinfo, 'message' : None, 'code' : 0}
    else:
        response = {'data' : "uid:%s not found." % uid, 'message' : None, 'code' : -1}
    return jsonify(response)



'''删除用户
'''
@mod.route('/del', methods=['GET'])
@login_required
def usersDel():
    app.logger.info( request.args  )

    uid = request.args.get('uid', None)
    effect_record = userDel(uid)
    if effect_record == 1:
        response = {'data' : None, 'message' : 'delete user sucess.', 'code' : 0}
    else:
        response = {'data' : None, 'message' : 'delete user failed.', 'code' : -1}
    return jsonify(response)


'''修改用户
'''
@mod.route('/edit', methods=['POST'])
@login_required
def usersEdit():
    data = request.form.to_dict()
    app.logger.info( "data:%s" % data )

    data.pop('rpassword', None)
    uid = data.pop('uid', None)
    app.logger.info( "fmt data:%s" % data )

    app.logger.info( "Update user, data:%s." % data )
    effect_record = updateUserinfo(data, uid) 
    if effect_record == 1:
        response = {'data' : None, 'message' : 'update user sucess.', 'code' : 0}
    else:
        response = {'data' : None, 'message' : 'Username:%s modify failed.' % data['cn_name'], 'code' : -1}
    return jsonify(response)


''' User Profile
'''
@mod.route('/profile', methods=['GET'])
@login_required
def user_profile():
    app.logger.debug("user profile")
    return render_template("users/user_profile.html")

''' User Group
'''
@mod.route('/group', methods=['GET'])
@login_required
def user_group():
    app.logger.debug("user Group")
    return render_template("users/user_group.html")


