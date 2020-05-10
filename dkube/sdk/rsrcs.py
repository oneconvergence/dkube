from .lib import *

class DkubeTraining(TrainingBase):
    def __init__(self, user, name=generate('train'), description='', tags=[]):
        self.user = user
        self.name = name

        super().__init__()

        self.job.name = name
        self.job.description = description
        self.training_def.tags = tags

        #Defaults
        self.tf_framework_details.tfversion = 'v1.14'
        self.executor_def.custom = None
        self.input_project.script = 'python model.py'

    def update_executor(self, executor=choices('dkube', 'custom'), 
                        framework=choices('tf1.14', 'tf1.13')):
        if executor == 'dkube':
            self.executor_def.custom = None
            if framework == 'tf1.14':
                self.tf_framework_details.tfversion = 'v1.14'
            if framework == 'tf1.13':
                self.tf_framework_details.tfversion = 'v1.13'
        if executor == 'custom':
            self.executor_def.choice = 'custom'
            self.executor_def.dkube = None

    def update_container(self, image_url=None, login_uname=None, login_pswd=None):
        self.custom_container.path = image_url
        self.custom_container.username = login_uname
        self.custom_container.password = login_pswd

    def update_startupscript(self, startup_script=None):
        self.input_project.script = startup_script        
   
    def update_envvars(self, envs={}):
        pass

    def add_project(self, name, commitid=None):
        name = self.user + ':' + name
        self.input_project_data.name = name

    def add_input_dataset(self, name, version=None, mountpath=None):
        name = self.user + ':' + name
        repo = self.repo(name=name, version=version, mountpath=mountpath)
        self.input_datasets.append(repo)

    def add_input_model(self, name, version=None, mountpath=None):
        name = self.user + ':' + name
        repo = self.repo(name=name, version=version, mountpath=mountpath)
        self.input_models.append(repo)

    def add_output_model(self, name, version=None, mountpath=None):
        name = self.user + ':' + name
        repo = self.repo(name=name, version=version, mountpath=mountpath)
        self.output_models.append(repo)

    def add_config_file(self, name, body=None):
        self.configfile.name = name
        self.configfile.body = body

    def update_distribution(self, strategy=choices('none', 'manual', 'auto'), workers=0, gpus=0):
        pass

class DkubePreprocessing(PreprocessingBase):
    def __init__(self, user, name=generate('data'), description='', tags=[]):
        self.user = user
        self.name = name

        super().__init__()

        self.job.name = name
        self.job.description = description
        self.pp_def.tags = tags

        #defaults
        self.custom_container.path = 'docker.io/ocdr/dkube-datascience-tf-cpu:v1.14'


    def update_container(self, image_url=None, login_uname=None, login_pswd=None):
        self.custom_container.path = image_url
        self.custom_container.username = login_uname
        self.custom_container.password = login_pswd

    def update_startupscript(self, startup_script=None):
        self.input_project.script = startup_script        
   

    def update_envvars(self, envs={}):
        pass

    def add_project(self, name, commitid=None):
        name = self.user + ':' + name
        self.input_project_data.name = name

    def add_input_dataset(self, name, version=None, mountpath=None):
        name = self.user+ ':' + name
        repo = self.repo(name=name, version=version, mountpath=mountpath)
        self.input_datasets.append(repo)

    def add_output_dataset(self, name, version=None, mountpath=None):
        name = self.user+ ':' + name
        repo = self.repo(name=name, version=version, mountpath=mountpath)
        self.output_datasets.append(repo)

    def add_config_file(self, name, body=None):
        self.configfile.name = name
        self.configfile.body = body

class DkubeServing(ServingBase):
    def __init__(self, user, name=generate('serving'), description='', tags=[]):
        self.user = user
        self.name = name

        super().__init__()

        self.job.name = name
        self.job.description = description
        self.pp_def.tags = tags

   
    def update_tranformer(self, image_url=None, login_uname=None, login_pswd=None):
        self.custom_container.path = image_url
        self.custom_container.username = login_uname
        self.custom_container.password = login_pswd

    def update_serving_model(self, model, version=None):
        self.serving_def.model = model
        self.serving_def.version = version
        self.serving_dev.owner = self.user


class DkubeProject(ProjectBase):
    def __init__(self, user, name=generate("project"), tags=None):
        self.user = user
        self.name = name

        super().__init__()

        self.datum.name = name
        self.datum.tags = tags

    def update_project_source(self, source=choices('github', 'bitbucket')):
        self.datum.source = 'git'

    def update_github_details(self, url, branch=None, authmode=choices('none', 'apikey', 'sshkey', 'password'), authkey=''):
        self.datum.url = url
        self.gitaccess.url = url
        self.gitaccess.branch = branch

        if authmode == 'apikey':
            self.gitcreds.username = self.user
            self.gitcreds.apikey = authkey
        elif authmode == 'password':
            self.gitcreds.username = self.user
            self.gitcreds.password = authkey
        elif authmode == 'sshkey':
            self.gitcreds.username = self.user
            self.gitcreds.sshkey = sshkey

    def update_bitbucket_details(self, url, branch=None, authmode=choices('none', 'sshkey', 'password'), authkey=''):
        self.update_github_details(url, branch, authmode, authkey)

class DkubeDataset(DatasetBase):
    def __init__(self, user, name=generate("dataset"), tags=None):
        self.user = user
        self.name = name

        super().__init__()

        self.datum.name = name
        self.datum.tags = tags

    def update_dataset_source(self, source=choices('dvs', 'github', 'bitbucket', 's3', 'gcs', 'nfs')):
        if source == 'github' or source == 'bitbucket':
            self.datum.source = 'git'
        elif source == 's3':
            self.datum.source = 'aws_s3'
        else:
            self.datum.source = source

    def update_github_details(self, url, branch=None, authmode=choices('none', 'apikey', 'sshkey', 'password'), authkey=''):
        self.datum.url = url
        self.gitaccess.url = url
        self.gitaccess.branch = branch

        if authmode == 'apikey':
            self.gitcreds.username = self.user
            self.gitcreds.apikey = authkey
        elif authmode == 'password':
            self.gitcreds.username = self.user
            self.gitcreds.password = authkey
        elif authmode == 'sshkey':
            self.gitcreds.username = self.user
            self.gitcreds.sshkey = sshkey

    def update_bitbucket_details(self, url, branch=None, authmode=choices('none', 'sshkey', 'password'), authkey=''):
        self.update_github_details(url, branch, authmode, authkey)

    def update_s3_details(self, bucket, prefix, key, secret):
        self.s3access.bucket = bucket
        self.s3access.prefix = prefix
        self.s3access.access_key_id = key
        self.s3access.access_key = secret

    def update_gcs_details(self, bucket, prefix, key, secret):
        self.gcsaccess.bucket = bucket
        self.gcsaccess.prefix = prefix
        self.gcssecret.name = key
        self.gcssecret.content = secret

    def update_nfs_details(self, path, server):
        self.nfsaccess.path = path
        self.nfsaccess.server = server

class DkubeModel(ModelBase):
    def __init__(self, user, name=generate("model"), tags=None):
        self.user = user
        self.name = name

        super().__init__()

        self.datum.name = name
        self.datum.tags = tags

    def update_model_source(self, source=choices('dvs', 'github', 'bitbucket', 's3', 'gcs')):
        if source == 'github' or source == 'bitbucket':
            self.datum.source = 'git'
        elif source == 's3':
            self.datum.source = 'aws_s3'
        else:
            self.datum.source = source

    def update_github_details(self, url, branch=None, authmode=choices('none', 'apikey', 'sshkey', 'password'), authkey=''):
        self.datum.url = url
        self.gitaccess.url = url
        self.gitaccess.branch = branch

        if authmode == 'apikey':
            self.gitcreds.username = self.user
            self.gitcreds.apikey = authkey
        elif authmode == 'password':
            self.gitcreds.username = self.user
            self.gitcreds.password = authkey
        elif authmode == 'sshkey':
            self.gitcreds.username = self.user
            self.gitcreds.sshkey = sshkey

    def update_bitbucket_details(self, url, branch=None, authmode=choices('none', 'sshkey', 'password'), authkey=''):
        self.update_github_details(url, branch, authmode, authkey)

    def update_s3_details(self, bucket, prefix, key, secret):
        self.s3access.bucket = bucket
        self.s3access.prefix = prefix
        self.s3access.access_key_id = key
        self.s3access.access_key = secret

    def update_gcs_details(self, bucket, prefix, key, secret):
        self.gcsaccess.bucket = bucket
        self.gcsaccess.prefix = prefix
        self.gcssecret.name = key
        self.gcssecret.content = secret
