#--*--coding: utf-8--*--

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
from flask import make_response
from flask.ext import excel

from app import app
from app.common.auth import login_required 
from app.common.assets import add_asset
from app.common.assets import get_assets 
from app.common.assets import get_assets_count 
from app.common.assets import validate_hostname_unique 
from app.common.assets import assetDel 



import sys
reload(sys)
sys.setdefaultencoding("utf-8")


mod = Blueprint('assets', __name__, url_prefix='/assets')



'''
    1. GET  查看用户信息
    2. POST 增加用户
'''
@mod.route('/', methods=['GET', 'POST'])
@login_required
def assets():

    if request.method == 'GET':
        assets = get_assets()
        return render_template('assets/assets.html', objs=assets)

    elif request.method == 'POST':
        data = request.form.to_dict()
 
        cur_time = datetime.datetime.now()
        data.update({'update_time' : cur_time, 'create_time' : cur_time})
        app.logger.info('data:%s' % data)

        hostname = data['hostname']
        app.logger.debug("hostname:%s." % hostname)
        try:
            err = validate_hostname_unique(str(hostname))
            app.logger.debug("err:%s" % err)
            if err == 1:
                retdata = {'code' : -1, 'data' : None, 'message' : 'hostname:%s already exists.' % hostname}
                return jsonify(retdata)
        except Exception as e:
             app.logger.error(e.args)

        effect_line = add_asset(data)
        if effect_line == 1:
            retdata = {'code' : 0, 'data' : None, 'message' : 'add asset sucess.'}
        else:
            retdata = {'code' : 0, 'data' : None, 'message' : 'add asset failed.'}
        return jsonify(retdata)


@mod.route('/csv', methods=['GET'])
@login_required
def export_csv():
    filename = "actual16-reboot"
    data = [['cpu', 'mem', 'hostname'], ['4', '8', 'monkey-hostname']]
    return excel.make_response_from_array(data, "csv", file_name=filename)


@mod.route('/del', methods=['GET'])
@login_required
def assetsDel():
    app.logger.info( request.args  )

    pk = request.args.get('pk', None)
    effect_record = assetDel(pk)
    app.logger.info( "delete pk:%s, effect_record:%s" % (pk, effect_record)  )
    if effect_record == 1:
        response = {'data' : None, 'message' : 'delete user sucess.', 'code' : 0}
    else:
        response = {'data' : None, 'message' : 'delete user failed.', 'code' : -1}
    return jsonify(response)


