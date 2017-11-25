

from app.models import execute_sql
from app.models import select_result
from app.models import select_all_result
from .crypt import encryption


def registerUser(data):
    cry_passwd = encryption(data['password'])
    sql = '''INSERT INTO users(username, email, password) values('%s', '%s', '%s')''' % (data['username'], data['email'], cry_passwd)
    print sql
    return execute_sql(sql)

def get_users():
    sql = '''SELECT * FROM users '''
    return select_all_result(sql)

def get_user(name):
    sql = '''SELECT * FROM users WHERE username = '%s';''' % name
    return select_all_result(sql)

def get_user_from_uid(uid):
    sql = '''SELECT * FROM users WHERE id = '%s';''' % uid 
    return select_result(sql)

def userDel(uid):
    sql = '''DELETE FROM users WHERE id = %s; ''' % uid
    print sql
    return execute_sql(sql)

def get_password_from_username(username):
    sql = '''SELECT PASSWORD FROM users WHERE username = '%s';''' % username
    return select_result(sql)

def updateUserinfo(data):
    sql = '''UPDATE users SET username='%s', email='%s', password='%s' WHERE id='%s'; ''' % (data['username'], data['email'], data['password'], data['uid'])

    print sql
    return execute_sql(sql)
