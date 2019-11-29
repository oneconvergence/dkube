import enum

class VersionInfo(object):
    def __init__(self):
        self.__cuda     = ''
        self.__dkube    = ''
        self.__nvidia   = ''

    @property
    def cuda(self):
        return self.__cuda
    @property
    def dkube(self):
        return self.__dkube
    @property
    def nvidia(self):
        return self.__nvidia

    @cuda.setter
    def cuda(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__cuda = data

    @dkube.setter
    def dkube(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__dkube = data

    @dkube.setter
    def nvidia(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__nvidia = data

    def to_json(self):
        return {'cuda': self.cuda, 'dkube': self.dkube, 'nvidia': self.nvidia}

    def from_json(self, data:dict):
        assert type(data) == dict

        self.cuda   = data.get('cuda', '') #optional
        self.dkube  = data['dkube']
        self.nvidia = data.get('nvidia', '') #optional


class JobGenerated(object):
    def __init__(self):
        self.__accelerator  = ''
        self.__affinity     = ''
        self.__best_objective_value = ''
        self.__best_trial_id    = ''
        self.__hp_tuning_info   = ''
        self.__jobid    = ''
        self.__ngpus_alloc  = 0
        self.__ngpus_max    = 0
        self.__runtime      = TimeStamps()
        self.__status       = Status()
        self.__studyref     = ''
        self.__subclass     = ''
        self.__tbref        = ''
        self.__trialref     = ''
        self.__user         = ''
        self.__uuid         = ''
        self.__version      = VersionInfo()

    @property
    def accelerator(self):
        return self.__accelerator
    @property
    def affinity(self):
        return self.__affinity
    @property
    def best_objective_value(self):
        return self.__best_objective_value
    @property
    def hp_tuning_info(self):
        return self.__hp_tuning_info
    @property
    def jobid(self):
        return self.__jobid
    @property
    def ngpus_alloc(self):
        return self.__ngpus_alloc
    @property
    def ngpus_max(self):
        return self.__ngpus_max
    @property
    def runtime(self):
        return self.__runtime
    @property
    def status(self):
        return self.__status
    @property
    def studyref(self):
        return self.__studyref
    @property
    def subclass(self):
        return self.__subclass
    @property
    def tbref(self):
        return self.__tbref
    @property
    def trialref(self):
        return self.__trialref
    @property
    def user(self):
        return self.__user
    @property
    def uuid(self):
        return self.__uuid
    @property
    def version(self):
        return self.__version

    def to_json(self):
        return {'accelerator': self.accelerator,
                'affinity': self.affinity,
                'best_objective_value': self.best_objective_value,
                'best_trial_id': self.best_trial_id,
                'hp_tuning_info': self.hp_tuning_info,
                'jobid': self.jobid,
                'ngpus_alloc': self.ngpus_alloc,
                'ngpus_max': self.ngpus_max,
                'runtime': self.runtime.to_json(),
                'status': self.status.to_json(),
                'studyref': self.studyref,
                'subclass': self.subclass,
                'tbref': self.tbref,
                'trialref': self.trialref,
                'user': self.user,
                'uuid': self.uuid,
                'versions': self.version.to_json()
                }

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        self.__accelerator = data.get('accelerator', '')
        self.__affinity = data.get('affinity', '')
        self.__best_objective_value = data.get('best_objective_value', '')
        self.__best_trial_id = data.get('best_trial_id', '')
        self.__hp_tuning_info = data.get('hp_tuning_info', '')
        self.__jobid = data['jobid']
        self.__ngpus_alloc = data.get('ngpus_alloc', 0)
        self.__ngpus_max = data.get('ngpus_max', 0)
        self.__runtime.from_json(data['runtime'])
        self.__status.from_json(data['status'])
        self.__studyref = data.get('studyref', '')
        #MAK TODO - fix from server side, this field should always be returned
        self.__subclass = data.get('subclass', '')
        self.__tbref = data.get('tbref', '')
        self.__trialref = data.get('trialref', '')
        self.__user = data['user']
        self.__uuid = data['uuid']
        self.__version.from_json(data['versions'])


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

        self._days(data.get('days', ''))
        self._hours(data.get('hours', ''))
        self._minutes(data.get('minutes', ''))
        self._seconds(data.get('seconds', ''))

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
        #MAK TODO - fix from server side, start time should come once job is submitted
        self._start(data.get('start', ''))
        self._end(data.get('end', ''))
        self.duration.from_json(data.get('duration', {}))

class State(enum.Enum):
    QUEUED      = 'queued'
    STARTING    = 'starting'
    TRAINING    = 'training'
    RUNNING     = 'running'
    COMPLETE    = 'complete'
    STOPPED     = 'stopped'
    STOPPING    = 'stopping'
    DELETING    = 'deleting'
    ERROR       = 'error'
    UNKNOWN     = 'unknown'

    @staticmethod
    def from_str(label:str):
        assert type(label) == str, "type mismatch error"
        label = label.lower()
        if label == 'queued': return State.QUEUED
        elif label == 'starting': return State.STARTING
        elif label == 'training': return State.TRAINING
        elif label == 'running': return State.RUNNING
        elif label == 'complete': return State.COMPLETE
        elif label == 'stopped': return State.STOPPED
        elif label == 'stopping': return State.STOPPING
        elif label == 'deleting': return State.DELETING
        elif label == 'error': return State.ERROR
        else: raise NotImplementedError

    @staticmethod
    def is_final_state(state:str):
        return state in ['complete', 'stopped', 'error']

    @staticmethod
    def is_inprogress_state(state:str):
        return state in ['queued', 'starting', 'training', 'running', 'stopping', 'deleting']

    @staticmethod
    def is_running_state(state:str):
        return state in ['running']

class Status(object):
    def __init__(self):
        self.__reason = ""
        self.__state  = State.UNKNOWN

    @property
    def reason(self):
        return self.__reason
    @property
    def state(self):
        return self.__state

    def _state(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__state = State.from_str(data)

    def _reason(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__reason = data

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        self._state(data['state'])
        self._reason(data.get('reason', ''))

    def to_json(self):
        return {'state': self.state, 'reason': self.reason}
