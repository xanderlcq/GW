a = 'sample{"moisture":345,"addWater":244}'
import datablock
import xsql
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
