#--*--coding: utf-8--*--

import time

from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort


from app.common.auth import authentication

from app import app
from app.models import db_insert
from app.models import db_all_select 
from app.common.auth import login_required 
from app.common.fmt import fmt_timestamp_timestr




mod = Blueprint('monitor', __name__)



'''
'''
@mod.route('/monitor', methods=['GET', 'POST'])
@login_required
def monitor():

    if request.method == 'GET':
        return render_template('monitor/mem.html')

    elif request.method == 'POST':
        data = request.form.to_dict()
        response = {'data' : None, 'message' : 'add user failed.', 'code' : -1}
        return jsonify(response)




'''内存监控信息采集 以及数据请求
'''
@mod.route('/api/v1/monitor', methods=['GET', 'POST'])
#@login_required
def api_v1_monitor():
    if request.method == 'GET':

        ctime = request.args.get('time')

        retdata = {}
        response_data = db_all_select("mem_monitor")
        for response in response_data:

            hostname = response[1]
            mem_free = response[2]
            create_time = fmt_timestamp_timestr( int(response[3]) )

            if ctime and ctime >= create_time:
                continue

            if hostname in retdata:
                retdata[hostname]['x'].append(mem_free)
                retdata[hostname]['y'].append(create_time)
                retdata[hostname] = retdata[hostname]
            else:
                retdata[hostname] = {'x' : [mem_free], 'y' : [create_time]}

        # max_time
        response = {'data' : retdata, 'message' : {'next_time' : int(time.time())} , 'code' : 0}
        return jsonify(response) 
    else:
        data = request.form.to_dict()
        effect_record = db_insert('mem_monitor', data)
        if effect_record == 1:
            response = {'data' : None, 'message' : 'add monitor sucess.', 'code' : 0}
        else:
            response = {'data' : None, 'message' : 'add monitor failed.', 'code' : -1}
        return jsonify(response) 


'''
'''
@mod.route('/log/pie', methods=['GET'])
@login_required
def log_pie():
    return render_template('monitor/nginx_log_pie.html')


@mod.route('/log/map', methods=['GET'])
@login_required
def log_map():
    return render_template('monitor/nginx_log_map.html')
