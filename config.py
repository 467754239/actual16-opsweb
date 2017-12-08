

import os

_basedir = os.path.abspath(os.path.dirname(__file__))

# LOG
LOGFILE = os.path.join(_basedir, 'logs/flask.log')


# MYSQL
MYSQLHOST     = '127.0.0.1'
MYSQLPORT     = 3306
MYSQLDB       = 'actual16_opsweb'
MYSQLUSER     = 'root'
MYSQLPASS     = '123456'
MYSQLCHARSET  = 'utf8'


# MAIL
MAIL_SERVER   = 'smtp.163.com'
MAIL_PORT     = 25
MAIL_USE_TLS  = True
#MAIL_USE_SSL  = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '13260071987@163.com')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'yi15093547036')

# UPLOAD
UPLOAD_FOLDER = '/tmp/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
