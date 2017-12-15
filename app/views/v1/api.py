#--*--coding: utf-8--*--


from flask import Blueprint, jsonify, request



from app import app
from app.common.assets import get_assets_count
from app.common.users import get_users_count 
from app.common.users import get_uid_from_username
from app.common.tokeybase import Token

from app.common.log import parse
from app.common.log import parseStatusCount 
from app.common.http import get_point_from_ip

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



@mod.route('/log/nginx/count')
@login_required
def api_v1_log_nginx():
    retdata = {'data' : [], 'fields' : []}
    log_results = parseStatusCount(app.config['NGINXLOG'])
    for status_code, count in log_results.items():
        dicTmp = {'name' : status_code, 'value' : count}
        retdata['data'].append(dicTmp)
        retdata['fields'].append(status_code)
    return jsonify(retdata)



@mod.route('/log/nginx/map')
@login_required
def api_v1_log_nginx_map():
    retdata = {'data' : [], 'geo' : {}}
    log_results = parse(app.config['NGINXLOG'])
    app.logger.debug('parse file finish.')
    for ip_status, count in log_results.items():
        ip, status = ip_status[0], ip_status[1]
        try:
            xy, _ = get_point_from_ip(ip)
        except Exception as e:
            app.logger.error("parse ip:%s error:%s." % (ip, e.args))
        else:
            #x, y = round((float(xy['x']) % 180),2), round((float(xy['y']) % 90), 2)
            x, y, city = xy[0], xy[1], xy[2]
            key = '%s-%s' % (ip, city)
            app.logger.debug("ip:%s, status:%s, count:%s, x:%s, y:%s." % (ip, status, count, x, y))
            retdata['data'].append({'name' : key, 'value' : count})
            retdata['geo'][key] = [x, y]
        
    return jsonify(retdata)
