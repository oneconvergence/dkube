library("dkubeR")

user <- Sys.getenv("LOGNAME")
token <- Sys.getenv("DKUBE_USER_ACCESS_TOKEN")

coderepo <- 'https://github.com/oneconvergence/dkube-examples/tree/master/tf/classification/mnist/digits/classifier/program'
datarepo <- 'https://github.com/oneconvergence/dkube-examples/tree/master/tf/classification/mnist/digits/classifier/data'

api <- DkubeAPI(token=token)
code_name <- generate("mnist")
code <- DkubeCode(user, name = code_name)
code$update_git_details(coderepo)
api$create_code(code)

dataset_name <- generate("mnist")
dataset <- DkubeDataset(user, name = dataset_name)
dataset$update_dataset_source(source='git')
dataset$update_git_details(datarepo)
api$create_dataset(dataset)

model_name <- generate("mnist")
model <- DkubeModel(user, name = model_name)
model$update_model_source(source='dvs')
api$create_model(model)
