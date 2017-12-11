#--*--coding: utf-8--*--


from flask import Blueprint, jsonify, request



from app import app
from app.common.assets import get_assets_count
from app.common.users import get_users_count 
from app.common.users import get_uid_from_username
from app.common.tokeybase import Token

from app.common.auth import login_required
from app.common.auth import authentication 
from app.common.auth import verify_token 

mod = Blueprint('api', __name__, url_prefix='/api/v1')


@mod.route('/users/count')
@login_required
def api_v1_users_count():
    #print dir(request)
    #print dir(request.headers)
    #print request.headers.get("token")
    tup = get_users_count()
    response = {'data' : tup[0], 'message' : None, 'code' : 0}
    return jsonify(response)


@mod.route('/assets/count')
#@login_required
def api_v1_assets_count():
    tup = get_assets_count()
    response = {'data' : tup[0], 'message' : None, 'code' : 0}
    return jsonify(response)


@mod.route('/token')
def get_token():
    username = request.args.get('username', None)
    password = request.args.get('password', None)
    auth_info, ok = authentication(username, password)
    if ok:
        uid, _ = get_uid_from_username(username)
        token = app.config['token'].generate_auth_token(uid)
        app.logger.info('Get token uid:%s, generate token:%s.' % (uid, token))
    else:
        token = "invalid token."
    return jsonify({ 'token' : token.decode('ascii') })


@mod.route('/hello')
@verify_token
def hello():
    return 'token sucess.' 


@mod.route('/assets', methods=['POST'])
@verify_token
def auto_collect_assets():
    '''
        1. parse json data
        2. add data to assets
    '''
    return 'token sucess.' 
