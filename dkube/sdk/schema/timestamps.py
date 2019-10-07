class Duration(object):
    def __init__(self):
        self.__days    = ""
        self.__hours   = ""
        self.__minutes = ""
        self.__seconds = ""

    @property
    def days(self):
        return self.__days
    @property
    def hours(self):
        return self.__hours
    @property
    def minutes(self):
        return self.__minutes
    @property
    def seconds(self):
        return self.__seconds

    def _days(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__days = data

    def _hours(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__hours = data

    def _minutes(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__minutes = data

    def _seconds(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__seconds = data

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"

        self._days(data['days'])
        self._hours(data['hours'])
        self._minutes(data['minutes'])
        self._seconds(data['seconds'])

class TimeStamps(object):
    def __init__(self):
        self.__start      = ""
        self.__end        = ""
        self.__duration   = Duration()

    @property
    def start(self):
        return self.__start
    @property
    def end(self):
        return self.__end
    @property
    def duration(self):
        return self.__duration

    def _start(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__start = data

    def _end(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__end = data

    def _duration(self, data:Duration):
        assert type(data) == Duration, "type mismatch error"
        self.__duration = data

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"

        self._start(data['start'])
        self._end(data['end'])
        self.duration.from_json(data['duration'])
