
from . import app

import MySQLdb as mdb

def execute_sql(sql):
    return app.config['cursor'].execute(sql)

def select_all_result(sql):
    app.config['cursor'].execute(sql)
    return app.config['cursor'].fetchall()

def select_result(sql):
    app.config['cursor'].execute(sql)
    return app.config['cursor'].fetchone()
