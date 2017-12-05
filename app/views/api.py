#--*--coding: utf-8--*--


from flask import Blueprint, jsonify



from app import app
from app.common.assets import get_assets_count
from app.common.users import get_users_count 

from app.common.auth import login_required

mod = Blueprint('api', __name__, url_prefix='/api')


@mod.route('/v1/users/count')
@login_required
def api_v1_users_count():
    #print dir(request)
    #print dir(request.headers)
    #print request.headers.get("token")
    tup = get_users_count()
    response = {'data' : tup[0], 'message' : None, 'code' : 0}
    return jsonify(response)


@mod.route('/v1/assets/count')
@login_required
def api_v1_assets_count():
    tup = get_assets_count()
    response = {'data' : tup[0], 'message' : None, 'code' : 0}
    return jsonify(response)
