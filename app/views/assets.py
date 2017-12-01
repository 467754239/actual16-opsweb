#--*--coding: utf-8--*--

import datetime

from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort


from app.common.assets import add_asset
from app.common.assets import get_assets 
from app.common.assets import assetDel 

from app import app
from app.common.auth import login_required 



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
        data.update({'update_time' : datetime.datetime.now()})
        app.logger.info('data:%s' % data)

        effect_line = add_asset(data)
        if effect_line == 1:
            retdata = {'code' : 0, 'data' : None, 'message' : 'add asset sucess.'}
        else:
            retdata = {'code' : 0, 'data' : None, 'message' : 'add asset failed.'}
        return jsonify(retdata)



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
