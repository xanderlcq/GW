__author__ = 'x'
import serial
import xsql
import myjson
import glob

devices_list =glob.glob('/dev/tty.ACM*')
print devices_list[0]
ser = serial.Serial(devices_list[0],9600)
a = xsql.Xsql()
print a.start_connection('greenwall1','root')

while 1 == 1:
    reading = ser.readline()
    if (reading is not None) and (reading != ''):
        print reading
        plant = reading[0:reading.index("{")]
        json_string = reading[reading.index("{"):]
        json = myjson.Myjson(json_string)
        a.write_data(plant, json.get_keys(), json.get_valuesList())