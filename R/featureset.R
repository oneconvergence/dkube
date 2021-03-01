#' @export
DkubeFeatureSet <- R6::R6Class(
  'DkubeFeatureSet',
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
    write_feature = function(df, path=NULL){
      if(self$is_df_null(df)){
        stop("Error: Dataframe is empty, can't write featureset")
      }
      if(is.null(path)){
        return()
      }
      write_parquet(df, path)
    },
    read_features = function(name = NULL, path=NULL){
      if(is.null(path)){
        return(data.frame())
      }
      df <- read_parquet(path)
      return(data.frame(df))
    },
    featureset_metadata = function(df){
      if(self$is_df_null(df)){
        stop("Error: Dataframe is empty, can't computer metadata")
      }
      metadata = list()
      index = 1
      for (i in colnames(df)){
        met_data = list()
        met_data[["name"]] = i
        met_data[["description"]] = "none"
        met_data[["type"]] = typeof(df[[i]])
        metadata[[index]] = met_data
        index = index + 1
      }
      return(data.frame(metadata))
    },
    featureset_commit = function(name=NULL, df=NULL, path=NULL, metadata=NULL){
      if(is.null(name) && is.null(df)){
        stop("Error: Name and dataframe both cannot be empty")
      }
      if(is.null(metadata)){
        metadata = featureset_metadata(df)
      }
      self$write_feature(df, path)
      token <- Sys.getenv("DKUBE_USER_ACCESS_TOKEN")
      dkubeapi <- dkube$sdk$DkubeApi
      api <- dkubeapi(token = token)
      api$commit_featureset(name=name,path=path, metadata=r_to_py(metadata), dftype="R")
    }
  ) 
)
