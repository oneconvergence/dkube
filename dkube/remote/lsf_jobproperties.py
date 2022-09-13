import pprint
from typing import Any

def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x

def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x

class JobProperties(object):

    def __init__(self, application: str = "", min_num_cpu: int = 1, max_num_cpu: int = 0, proc_per_host: int = 0, extra_res: str = "", runlimithour: int = 0, runlimitminute: int = 0, max_mem: int = 0, rerunnable: str = "", app_profile: str = "", prj_name: str = "", res_id: str = "", login_shell: str = "", queue: str = "", ngpu: int = 0, gpu_mode: str = "", extra_params: str = "") -> None:
        self.application = application
        self.min_num_cpu = min_num_cpu
        self.max_num_cpu = max_num_cpu
        self.proc_per_host = proc_per_host
        self.extra_res = extra_res
        self.runlimithour = runlimithour
        self.runlimitminute = runlimitminute
        self.max_mem = max_mem
        self.rerunnable = rerunnable
        self.app_profile = app_profile
        self.prj_name = prj_name
        self.res_id = res_id
        self.login_shell = login_shell
        self.queue = queue
        self.ngpu = ngpu
        self.gpu_mode = gpu_mode
        self.extra_params = extra_params

    def to_dict(self) -> dict:
        result = {}
        result["application"] = from_str(self.application)
        result["min_num_cpu"] = from_int(self.min_num_cpu)
        result["max_num_cpu"] = from_int(self.max_num_cpu)
        result["proc_per_host"] = from_int(self.proc_per_host)
        result["extra_res"] = from_str(self.extra_res)
        result["runlimithour"] = from_int(self.runlimithour)
        result["runlimitminute"] = from_int(self.runlimitminute)
        result["max_mem"] = from_int(self.max_mem)
        result["rerunnable"] = from_str(self.rerunnable)
        result["app_profile"] = from_str(self.app_profile)
        result["prj_name"] = from_str(self.prj_name)
        result["res_id"] = from_str(self.res_id)
        result["login_shell"] = from_str(self.login_shell)
        result["queue"] = from_str(self.queue)
        result["ngpu"] = from_int(self.ngpu)
        result["gpu_mode"] = from_str(self.gpu_mode)
        result["extra_params"] = from_str(self.extra_params)
        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
