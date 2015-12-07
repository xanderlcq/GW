import myjson


class Datablock(object):

    def __init__(self,data):
        self.data = data
        self.json = None
        if data is not None and (data != ''):
            self.json = myjson.Myjson(self.get_raw_data())

    def get_id(self):
        assert self.data.find("{") != -1, AssertionError
        return self.data[0:self.data.index("{")]

    def get_raw_data(self):
        assert self.data.find("{") != -1, AssertionError
        return self.data[self.data.index("{"):]

    def get_json(self):
        assert self.is_valid(), 'Invalid datablock'
        return self.json

    def get_data(self):
        assert self.is_valid(), 'Invalid datablock'
        return self.json.get_valuesList()

    def get_data_keys(self):
        assert self.is_valid(), 'Invalid datablock'
        return self.json.get_keys()

    def load_data(self,data):
        self.data = data
        if data is not None and (data != ''):
            self.json = myjson.Myjson(data)

    def is_valid(self):
        return self.data is not None and self.data != '' \
               and self.json is not None

    def __str__(self):
        return 'Raw data : '+self.get_raw_data()+'\nJson: '+str(self.json)