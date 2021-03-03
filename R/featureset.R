#' @export
DkubeFeature <- R6::R6Class(
  'DkubeFeature',
  public = list(
    `token` = NULL,
    is_df_null = function(df){
      if (dim(df)[1] == 0 || dim(df)[2] == 0) {
        # True if there is no row or column
        return(TRUE)
      }
      else{
        return(FALSE)
      }
    },
    write_feature = function(df, filename = "featureset.parquet", path=NULL){
      if(self$is_df_null(df)){
        stop("Error: Dataframe is empty, can't write featureset")
      }
      if(is.null(path)){
        return()
      }
      arrow::write_parquet(df, file.path(path, filename))
    },
    read_features = function(name = NULL, filename = "featureset.parquet", path=NULL){
      if(is.null(path)){
        return(data.frame())
      }
      df <- arrow::read_parquet(file.path(path, filename))
      return(data.frame(df))
    },
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
    },
    featureset_commit = function(name=NULL, df=NULL, path=NULL, filepath="/tmp/metadata.yaml"){
      if(is.null(name) && is.null(df)){
        stop("Error: Name and dataframe both cannot be empty")
      }
      filepath = self$write_metadata(df=df, filepath)
      self$write_feature(df=df, path=path)
      token <- Sys.getenv("DKUBE_USER_ACCESS_TOKEN")
      dkubeapi <- dkube$sdk$DkubeApi
      api <- dkubeapi(token = token)
      api$upload_featurespec(featureset=name, filepath=filepath)
      api$commit_featureset(name=name, path=path, dftype="R")
    }
  ) 
)
