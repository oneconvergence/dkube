from dkube.sdk import *
from dkube.slurm import *

training_name = generate('mnist')
training = DkubeTraining("oc", name=training_name,
                         description='triggered from dkube pl launcher')
training.update_container(framework="tensorflow_1.14",
                          image_url="ocdr/d3-datascience-tf-cpu:v1.14")
training.update_startupscript('python model.py')
training.add_code("m")
training.add_input_dataset("m", mountpath='/opt/dkube/input')
training.add_output_model("m", mountpath='/opt/dkube/output')

props = JobProperties(partition="C-16Cpu-30GB")

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc0YmNkZjBmZWJmNDRiOGRhZGQxZWIyOGM2MjhkYWYxIn0.eyJ1c2VybmFtZSI6Im9jIiwicm9sZSI6ImRhdGFzY2llbnRpc3QsbWxlLHBlLG9wZXJhdG9yIiwiZXhwIjo0ODUwMzU1NTk0LCJpYXQiOjE2MTAzNTU1OTQsImlzcyI6IkRLdWJlIn0.HYOnQCE-BvVOEEPS83zX3nqtywVCMNtLnoIX06sDg12RX8AEWsCkx-w_Tx085FvqHGb_lYG8eyvNqnlzftsXIXjlwcnd3AvRwIfZ6bTL8hzv_vor9nnQcwsY97ehXJsDRANu9OxbZDLKmFI9ujaLPbPCAkFFFPHno8eBBrSfWBsWqcRgnjKAR0gS6kzVnoleX6jySmpV5GVpImX2IMCEEXzOm_xZ17badrHUdnpa6ai-SoIXMSJFcWYyUiQaIPAsDN7OZbHIX8NE_P-O-YllrXPhjf97aCnvzya9jBV-DwkwhtMfj2MkzZXouEsBCfhWKQ2Mucyd88WO5RDLjsXeZA"

res = launch_slurmjob("dap20", props, "oc", token,
                      training.job, url="https://192.168.200.133:32222")

print(res)
