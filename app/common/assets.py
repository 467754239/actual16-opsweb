
from app.models import execute_sql
from app.models import select_result
from app.models import select_all_result


def add_asset(data):
    fields, values = [], []
    for k, v in data.items():
        fields.append(k)
        values.append("'%s'" % v)

    format_fields = ', '.join(fields)
    format_values = ', '.join(values)
    sql = '''INSERT INTO assets (%s) VALUES (%s);''' % (format_fields, format_values)
    print sql
    return execute_sql(sql)


def get_assets():
    sql = '''SELECT * FROM assets '''
    return select_all_result(sql)

def assetDel(pk):
    sql = '''DELETE FROM assets WHERE id = %s; ''' % int(pk)
    print sql
    return execute_sql(sql)

def get_assets_count():
    sql = '''SELECT count(*) FROM assets; '''
    return select_result(sql)

def validate_hostname_unique(hostname):
    sql = '''SELECT * FROM assets WHERE hostname='%s'; ''' % hostname
    return execute_sql(sql)
