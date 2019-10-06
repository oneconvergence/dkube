class Status(object):
    def __init__(self):
        self.__reason = ""
        self.__state  = ""

    @property
    def reason(self):
        return self.__reason
    @property
    def state(self):
        return self.__state

    def _state(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__state = data

    def _reason(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__reason = data

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        #from json to this object

    def to_json(self):
        #return json of this object
        pass
