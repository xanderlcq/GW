#!/usr/bin/python
import serial
import xsql
import myjson
import glob

a = myjson.Myjson('{"key1":123,"key2":321}')
print a.get_keys()
print a.get_valuesList()
'''
devices_list =  glob.glob('/dev/tty.usb*')
print devices_list[0]

ser = serial.Serial(devices_list[0],9600)
while 1:
    json = ser.readline()
    print json
'''
"""json format: {"key":value, "key":value}"""
"""
key work list:
moist
volume

'{"moisture":12.0,"light":122,"temperature":12}'

a = xsql.Xsql()
print a.start_connection('greenwall1','root')
keys =['moisture','light','note']
values = ['123','321','"abc"']
a.write_data('plant1',keys,values)
#devices_list =  glob.glob('/dev/tty.usb*')
#rint devices_list[0]"""
"""
ser = serial.Serial(devices_list[0],9600)
while 1:
    read = ser.readline()
    print read
    json = myjson.Myjson(read)
    m = json.get_value('moisture')
    print a.write_data('plant1', 'moisture', m)
"""

