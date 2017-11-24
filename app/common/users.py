

from app.models import execute_sql
from app.models import select_all_result


def register(data):
    sql = '''INSERT INTO users(username, email, password) values('%s', '%s', '%s')''' % (data['username'], data['email'], data['password'])
    print sql
    return execute_sql(sql)

def get_users():
    sql = '''SELECT * FROM users '''
    return select_all_result(sql)

def get_user(name):
    sql = '''SELECT * FROM users WHERE username = '%s';''' % name
    return select_all_result(sql)

def userDel(uid):
    sql = '''DELETE FROM users WHERE id = %s; ''' % uid
    print sql
    return execute_sql(sql)



