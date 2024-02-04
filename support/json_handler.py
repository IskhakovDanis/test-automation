import json

class JSONHandler:

    @staticmethod
    def load_json(key_info, path):
        with open(path, 'r') as f:
            data = json.load(f)
        return data[key_info]


    def dump_json(self):
        pass


