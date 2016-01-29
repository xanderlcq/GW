import serial
import glob
import datablock
import xsql
import emailer
import time
while True:
    time.sleep(2)
    try:
        devices_list = glob.glob('/dev/tty.usb*')
        print devices_list[0]
    except IndexError:
        print 'failed to connect to Arduino, Check USB connection'

    sql = xsql.Xsql()
    print sql.start_connection(host='greenwall.ckjdodi2wmgo.us-east-1.rds.amazonaws.com',database='gw',
                               user='root', password='xander1997')
    serials = []
    for ports in devices_list:
        serials.append(serial.Serial(devices_list[0],9600))
    while True:
        for ser in serials:
            try:
                data = datablock.Datablock(ser.readline())
                if data.is_valid():
                    try:
                        sql.write_data(data.get_id(), data.get_data_keys(), data.get_data())
                        if 'error' in data.get_data_keys():
                            try:
                                e = emailer.Emailer()
                                msg = e.generate_data_email(data)
                                e.send_email('WARNING',msg,'bbakker@deerfield.edu')
                            except AssertionError:
                                print 'Failed to sent warning email'
                    except AssertionError:
                        print 'Data writing failed'
            except AssertionError:
                print 'Serial reading failed'
