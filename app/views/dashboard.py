

from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort

from app.common.auth import login_required

mod = Blueprint('dashboard', __name__, url_prefix='/')


@mod.route('/')
@login_required
def index():
    return render_template('dashboard/index.html')
