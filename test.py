a = 'sample{"moisture":345,"addWater":244}'
import datablock
import xsql
'''
try:
    data = datablock.Datablock(a)
    print data.get_raw_data()
    print data.get_id()
    print data.get_data_keys()
    print data.get_data()
    print data.is_valid()
    print data
    sql = xsql.Xsql()
    print sql.start_connection('gw', 'root', 'xander1997')
    sql.write_data(data.get_id(), data.get_data_keys(), data.get_data())
except AssertionError:
    print 'Serial reading failed'
'''
data = datablock.Datablock("sample{\"error\":\"water tank empty\"}")
print data.get_raw_data()
print data.get_id()
print data.get_data_keys()
print data.get_data()
print data.is_valid()
print data.get_value(data.get_data_keys()[0])
import emailer
e = emailer.Emailer()
msg = e.generate_data_email(data,'error')
print msg

e#.send_email('WARNING',msg,'ali@deerfield.edu')

sql = xsql.Xsql()
print sql.start_connection(host='greenwall.ckjdodi2wmgo.us-east-1.rds.amazonaws.com',database='gw',
                           user='root', password='xander1997')
sql.write_data(data.get_id(), data.get_data_keys(), data.get_data())