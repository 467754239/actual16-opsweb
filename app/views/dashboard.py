

from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort



mod = Blueprint('dashboard', __name__)


@mod.route('/')
def index():
    return render_template('dashboard/index.html')
