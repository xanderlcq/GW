import serial
import glob
import datablock
import xsql

devices_list = glob.glob('/dev/ttyACM*')
print devices_list[0]
ser = serial.Serial(devices_list[0],9600)
sql = xsql.Xsql()
print sql.start_connection('greenwall1', 'root', 'xander')

while True:
    try:
        data = datablock.Datablock(ser.readline)
        if data.is_valid():
            sql.write_data(data.get_id(), data.get_data_keys(), data.get_data())
    except AssertionError:
        print 'Serial reading failed'
        sql.write_data('log', 'errors', 'Serial reading failed.')

