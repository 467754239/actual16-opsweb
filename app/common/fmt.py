
import time

def fmt_db_data(data):
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

def fmt_timestamp_timestr(timestamp):
    time_local = time.localtime(timestamp)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt
