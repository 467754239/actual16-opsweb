

from app.models import execute_sql
from app.models import select_result
from app.models import select_all_result
from .crypt import encryption


def registerUser(data):
    cry_passwd = encryption(data['password'])
    sql = '''INSERT INTO users(username, email, password, role) values('%s', '%s', '%s', '%s')''' % (data['username'], data['email'], cry_passwd, data['role'])
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
    sql = '''SELECT password FROM users WHERE username = '%s';''' % username
    return select_result(sql)

def updateUserinfo(data):
    sql = '''UPDATE users SET username='%s', email='%s', password='%s', role='%s' WHERE id=%d; ''' % (data['username'], data['email'], data['password'], data['role'], int(data['uid']) )

    print sql
    return execute_sql(sql)


def get_role_from_username(username):
    sql = '''SELECT role FROM users WHERE username = '%s';''' % username
    return select_result(sql)
