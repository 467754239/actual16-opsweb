
from app import app
from app import db

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
    


class AuthUser(db.Model):
    __tablename__ = 'auth_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    ## v1
    #def __init__(self, **kwargs):
    #    super(AuthUser, self).__init__(**kwargs)

    # v2
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<AuthUser %r>' % self.username

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
