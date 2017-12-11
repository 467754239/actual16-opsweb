
from app import app

from app.common.fmt import fmt_db_data 

import MySQLdb as mdb

def execute_sql(sql):
    return app.config['cursor'].execute(sql)

def select_all_result(sql):
    app.config['cursor'].execute(sql)
    return app.config['cursor'].fetchall()

def select_result(sql):
    app.config['cursor'].execute(sql)
    return app.config['cursor'].fetchone()


# orm 
def db_insert(table_name, data):
    fields, values = fmt_db_data(data)
    sql = '''INSERT INTO %s (%s) VALUES (%s);''' % (table_name, fields, values)
    print sql
    return execute_sql(sql)


def db_all_select(table_name):
    sql = '''SELECT * FROM %s;''' % table_name
    return select_all_result(sql)


def close_db():
    app.config['cursor'].close()
    app.config['conn'].close()
    
