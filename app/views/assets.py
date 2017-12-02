#--*--coding: utf-8--*--

import datetime

from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort
from flask import make_response

from app.common.assets import add_asset
from app.common.assets import get_assets 
from app.common.assets import get_assets_count 
from app.common.assets import assetDel 

from app import app
from app.common.auth import login_required 

from flask.ext import excel


mod = Blueprint('assets', __name__)



'''
    1. GET  查看用户信息
    2. POST 增加用户
'''
@mod.route('/assets', methods=['GET', 'POST'])
#@login_required
def assets():

    if request.method == 'GET':
        assets = get_assets()
        return render_template('assets/assets.html', objs=assets)

    elif request.method == 'POST':
        data = request.form.to_dict()
 
        cur_time = datetime.datetime.now()
        data.update({'update_time' : cur_time, 'create_time' : cur_time})
        app.logger.info('data:%s' % data)

        effect_line = add_asset(data)
        if effect_line == 1:
            retdata = {'code' : 0, 'data' : None, 'message' : 'add asset sucess.'}
        else:
            retdata = {'code' : 0, 'data' : None, 'message' : 'add asset failed.'}
        return jsonify(retdata)


@mod.route('/asset/csv', methods=['GET'])
@login_required
def export_csv():
    filename = "actual16-reboot"
    data = [[1, 2], [3, 4]]
    return excel.make_response_from_array(data, "csv", file_name=filename)

@mod.route('/asset/del', methods=['GET', 'POST'])
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


'''API 统计主机数量
'''
@mod.route('/api/v1/assets/count')
@login_required
def api_v1_assets_count():
    tup = get_assets_count()
    response = {'data' : tup[0], 'message' : None, 'code' : 0}
    return jsonify(response)
