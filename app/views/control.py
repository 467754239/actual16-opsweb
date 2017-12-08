#--*--coding: utf-8--*--

import os

from flask import Blueprint
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for
from flask import request
from flask import jsonify
from flask import abort
from flask import g
from flask import flash
from werkzeug import secure_filename


from app import app
from app.common.auth import login_required 
from app.common.ssh import execute_command_for_password
from app.common.ssh import execute_upload_for_passwd 


mod = Blueprint('control', __name__, url_prefix='/control')



@mod.route('/', methods=['GET'])
@login_required
def control_index():
    return render_template('control/control.html')


@mod.route('/cmd', methods=['POST'])
@login_required
def cmd():
    cmd = request.form.get("cmd")
    hostgroup = request.form.getlist('cmd_hostgroup[]')
    app.logger.info("cmd:%s, hostgroup:%s." % (cmd, hostgroup) )
    output = []
    for host in hostgroup:
        stdout =  execute_command_for_password(host, 'wangkang', '123456', cmd)
        stdout = "## %s\n" % host + stdout
        output.append(stdout)
    return jsonify({"code" : '0', "data" : '\n'.join(output)})


@mod.route('/upload', methods=['POST'])
@login_required
def upload():
    target = request.form.get('target')
    hostgroup = request.form.getlist('upload_hostgroup')

    file_handler = request.files['file']
    filename = secure_filename(file_handler.filename)
    localFile = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file_handler.save(localFile)

    # scp file to remote server.
    output = []
    for host in hostgroup:
        targetFile = os.path.join(target, filename)
        try:
            execute_upload_for_passwd(host, 'wangkang', '123456', localFile, targetFile)
        except Exception as e:
            stderr = "## %s\n%s" % (host, e.args)
            output.append(stderr)
        else:
            stdout = "## %s\n%s" % (host, 'sucess.')
            output.append(stdout)
    return jsonify({"code" : '0', 'data' : '\n'.join(output)})
