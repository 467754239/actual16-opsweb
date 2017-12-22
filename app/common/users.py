

from app.models import execute_sql
from app.models import select_result
from app.models import select_all_result
from .crypt import encryption


def registerUser(data):

    #cry_passwd = encryption(data['password'])
    #sql = '''INSERT INTO users(username, email, password, role) values('%s', '%s', '%s', '%s')''' % (data['username'], data['email'], cry_passwd, data['role'])

    fields, values = fmt_data(data)
    sql = '''INSERT INTO users (%s) VALUES (%s);''' % (fields, values)
    print sql
    return execute_sql(sql)


def validate_user_exists(username):
    sql = '''SELECT * FROM users WHERE username = '%s';''' % username 
    num = select_result(sql)
    if not num:
        return None, False
    return 'username:%s already exists.' % username, True

def validate_uid_exists(uid):
    sql = '''SELECT * FROM users WHERE id = '%s';''' % uid 
    num = select_result(sql)
    if not num:
        return None, False
    return 'username:%s already exists.' % uid , True

def get_users():
    fields = ['id', 'username', 'phone', 'role', 'cn_name', 'position', 'password', 'email']
    sql = '''SELECT %s FROM users; ''' % ','.join(fields)
    print sql
    values = select_all_result(sql)
    retdata = [ dict(zip(fields, value)) for value in values ]
    return retdata 

def get_user(name):
    sql = '''SELECT * FROM users WHERE username = '%s';''' % name
    return select_all_result(sql)

def get_uid_from_username(username):
    sql = '''SELECT id FROM users WHERE username = '%s';''' % username
    uid = select_result(sql)
    if uid:
        return uid[0], True
    return None, False

def get_user_from_uid(uid):
    fields = ['id', 'username', 'phone', 'role', 'cn_name', 'position', 'password', 'email']
    sql = '''SELECT %s FROM users WHERE id = '%s';''' % (','.join(fields), uid )
    print sql
    values = select_result(sql)
    return dict(zip(fields, values))

def userDel(uid):
    sql = '''DELETE FROM users WHERE id = %s; ''' % uid
    print sql
    return execute_sql(sql)

def get_password_from_username(username):
    sql = '''SELECT password FROM users WHERE username = '%s';''' % username
    return select_result(sql)

def updateUserinfo(data, uid):
    #sql = '''UPDATE users SET username='%s', email='%s', password='%s', role='%s' WHERE id=%d; ''' % (data['username'], data['email'], data['password'], data['role'], int(data['uid']) )

    #print sql
    #return execute_sql(sql)

    values = fmt_update_data(data)
    sql = '''UPDATE users SET %s WHERE id = %d; '''  % (values, int(uid))
    print sql
    return execute_sql(sql)


def get_role_from_username(username):
    sql = '''SELECT role, cn_name FROM users WHERE username = '%s';''' % username
    return select_result(sql)


def fmt_data(data):
    fields, values = [], []                                                              
    for k, v in data.items():                                                            
        fields.append(k)                                                     
        if k == 'password':
            values.append("'%s'" % encryption(v) )                                                        
        else:
            values.append("'%s'" % v)                                                        
                                                                                     
    format_fields = ', '.join(fields)                                                    
    format_values = ', '.join(values)

    return format_fields, format_values


def fmt_update_data(data):
    values = []
    for k, v in data.items():                                                            
        values.append("%s='%s'" % (k, v))
    return ', '.join(values)


def get_users_count():
    sql = '''SELECT count(*) FROM users; '''
    return select_result(sql)
