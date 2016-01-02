import xsql
sql = xsql.Xsql()
print sql.start_connection('greenwall.ckjdodi2wmgo.us-east-1.rds.amazonaws.com','gw','root','xander1997')
print sql.write_data('sample',['moisture','addWater'],['123','100'])
print sql.read_data('sample',['moisture','addWater'],['moisture','addWater'],['123','100'])