#--*--coding: utf-8--*--

import datetime

from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort


from app.common.assets import add_asset
from app.common.assets import get_assets 

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
        print assets
        return render_template('assets/assets.html', objs=assets)

    elif request.method == 'POST':
        data = request.form.to_dict()
        data.update({'update_time' : datetime.datetime.now()})
        app.logger.info('data:%s' % data)

        print add_asset(data)
        return jsonify('')

