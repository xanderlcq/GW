__author__ = 'x'
# Last edit: 10/27/15 17:50

class Myjson(object):

    def __init__(self,json):
        assert self._is_json(json), 'Invalid Json Format'
        self.json = json

    def load_json(self,json):
        assert self._is_json(json), 'Invalid Json Format'
        self.json = json

    def get_value(self,key):
        assert self.json.find(key) != -1, 'The key you are looking for does not exist'
        lower_index = self.json.index(key)+len(key)+2
        upper_index = self.json.find(',',lower_index)
        if upper_index == -1:
            upper_index = self.json.find('}',lower_index)
        return self.json[lower_index:upper_index]  # stub

    def get_keys(self):
        """This function return a lists of keys in String

        Return: A list of strings, containing keys"""
        number_of_keys = self.json.count(':')
        keys_list = []
        upper_index = 0
        for x in range(0,number_of_keys):
            if x == 0:
                lower_index = self.json.index('"',upper_index+1)
                upper_index = self.json.index('"',lower_index+1)
                keys_list.append(self.json[lower_index+1:upper_index])
            else:
                pass
                lower_index = self.json.index(',"',upper_index+1)+1
                upper_index = self.json.index('"',lower_index+2)
                keys_list.append(self.json[lower_index+1:upper_index])
        return keys_list

    def convert_to_list(self):
        keys_list = self.get_keys()
        json_list = []
        for x in keys_list:
            json_list.append(x)
            json_list.append(self.get_value(x))
        return json_list  # stub

    def _is_json(self, jsonIn):
        import json
        try:
            json_object = json.loads(jsonIn)
        except ValueError, e:
            return False
        return True

# '{"key1":1.0,"key2":"str","key3":1}'

