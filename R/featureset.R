#' Dkube Featureset
#'
#' @param df dataframe
#'
#' @export
is_df_null = function(df){
  if (dim(df)[1] == 0 || dim(df)[2] == 0) {
    # True if there is no row or column
    return(TRUE)
  }
  else{
    return(FALSE)
  }
}

#' Dkube Featureset
#'
#' @param name featureset name
#'
#' @export
create_featureset = function(name){
  token <- Sys.getenv("DKUBE_USER_ACCESS_TOKEN")
  featureset = dkube$sdk$rsrcs$DkubeFeatureSet(name=name)
  dkubeapi <- dkube$sdk$DkubeApi
  api <- dkubeapi(token = token)
  api$create_featureset(featureset)
}

#' Dkube Featureset
#'
#' @param name featureset name
#' @param df dataframe
#' @param filename parquet file name
#' @param path output mount path
#'
#' @export
write_featureset = function(name, df, filename = "featureset.parquet", path=NULL){
  if(is_df_null(df)){
    stop("Error: Dataframe is empty, can't write featureset")
  }
  print("inside write")
  if(is.null(path) && file.exists("/etc/dkube/config.json")){
    print("loading config")
    dkube_config = jsonlite::fromJSON("/etc/dkube/config.json")
    mounted_featuresets = dkube_config$outputs$featureset
    for (each_mounted_fs in mounted_featuresets){
      if(!is.null(each_mounted_fs)){
        if (each_mounted_fs$name == name){
          path = each_mounted_fs$location
          print(path)
          is_mounted = TRUE
          break
        }
      }
    }
  }
  if(is.null(path)){
    dkube_path = Sys.getenv("DKUBE_USER_STORE")
    jobuuid = Sys.getenv("DKUBE_JOB_UUID")
    if(length(dkube_path) < 2){
      return()
    }
    featureset_folder = file.path("gen/outputs/", jobuuid, name)
    path = file.path(dkube_path, featureset_folder)
    dir.create(path, recursive = TRUE)
    print(path)
  }
  print("edrf",path)
  arrow::write_parquet(df, file.path(path, filename))
}

#' Dkube Featureset
#'
#' @param df dataframe
#' @param filename parquet file name
#' @param path input mount path
#'
#' @export
read_featureset = function(name = NULL, filename = "featureset.parquet", path=NULL){
  is_mounted = FALSE
  if(is.null(path) && is.null(name)){
    message("Name and path both can't be empty")
    return(data.frame())
  }
  if(is.null(path) && file.exists("/etc/dkube/config.json")){
    dkube_config = jsonlite::fromJSON("/etc/dkube/config.json")
    mounted_featuresets = dkube_config$inputs$featureset
    for (each_mounted_fs in mounted_featuresets){
      if(!is.null(each_mounted_fs)){
        if (each_mounted_fs$name == name){
          path = each_mounted_fs$location
          is_mounted = TRUE
          break
        }
      }
    }
  }
  if (is_mounted == FALSE){
    token <- Sys.getenv("DKUBE_USER_ACCESS_TOKEN")
    dkubeapi <- dkube$sdk$DkubeApi
    api <- dkubeapi(token = token)
    path = api$read_featureset(name=name, dftype="R")
  }
  if(!is.null(path)){
    df <- arrow::read_parquet(file.path(path, filename))
    return(data.frame(df))
  }
  else{
    message("Featureset not found")
    return(data.frame())
  }
}


#' Dkube Featureset
#'
#' @param df dataframe
#' @param filename yaml file name to write metadata
#'
#' @export
write_metadata = function(df, filepath=NULL){
  if(is.null(filepath)){
    stop("File path not provided to write metadata")
  }
  metadata = list()
  index = 1
  for (i in colnames(df)){
    met_data = vector(mode="list", length=3)
    names(met_data) = c("name", "description", "schema")
    met_data[[1]] = i; met_data[[2]] = "none"; met_data[[3]] = typeof(df[[i]])
    metadata[[index]] = met_data
    index = index + 1
  }
  yaml::write_yaml(metadata, filepath)
  return(filepath)
}

#' Dkube Featureset
#'
#' @param name featureset name
#' @param df dataframe
#' @param path output mount path
#' @param filepath parquet file name
#'
#' @export
commit_featureset = function(name=NULL, df=NULL, path=NULL, filepath="/tmp/metadata.yaml"){
  if(is.null(name) && is.null(df)){
    stop("Error: Name and dataframe both cannot be empty")
  }
  filepath = write_metadata(df=df, filepath)
  write_featureset(name=name, df=df, path=path)
  token <- Sys.getenv("DKUBE_USER_ACCESS_TOKEN")
  dkubeapi <- dkube$sdk$DkubeApi
  api <- dkubeapi(token = token)
  api$upload_featurespec(featureset=name, filepath=filepath)
  api$commit_featureset(name=name, path=path, dftype="R")
}
