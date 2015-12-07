import serial
import glob
import datablock
import xsql

devices_list = glob.glob('/dev/ttyACM*')
print devices_list[0]

sql = xsql.Xsql()
print sql.start_connection(host='greenwall1.ckjdodi2wmgo.us-east-1.r'
                                'ds.amazonaws.com',database='greenwall1',
                           user='root', password='xander')
serials = []
for ports in devices_list:
    serials.append(serial.Serial(devices_list[0],9600))

while True:
    for ser in serials:
        try:
            data = datablock.Datablock(ser.readline)
            if data.is_valid():
                try:
                    sql.write_data(data.get_id(), data.get_data_keys(), data.get_data())
                except AssertionError:
                    print 'Data writing failed'
        except AssertionError:
            print 'Serial reading failed'
