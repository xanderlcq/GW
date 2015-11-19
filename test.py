a = 'asdas{"key1":1.01,"key2":"str","key3":1}'
import datablock
try:
    data = datablock.Datablock(a)
    print data.get_raw_data()
    print data.get_id()
    print data.get_data_keys()
    print data.get_data()
    print data.is_valid()
    print data
except AssertionError:
    print 'Serial reading failed'
