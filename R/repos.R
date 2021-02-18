#' Dkube Code repo
#'
#' @param user username
#' @param name repo/resource name
#' @param description additional details for the repo
#'
#' @export
DkubeCode <- function(user = NULL, name = NULL){
  code <- dkube$sdk$rsrcs$DkubeCode(user, name = name)
}

#' Dkube Dataset repo
#'
#' @param user username
#' @param name repo/resource name
#' @param description additional details for the repo
#'
#' @export
DkubeDataset <- function(user = NULL, name = NULL){
  dataset <- dkube$sdk$rsrcs$DkubeDataset(user, name = name)
}

#' Dkube Model repo
#'
#' @param user username
#' @param name repo/resource name
#' @param description additional details for the repo
#'
#' @export
DkubeModel <- function(user = NULL, name = NULL){
  model <- dkube$sdk$rsrcs$DkubeModel(user, name = name)
}

#' Dkube Project
#'
#' @param user username
#' @param name repo/resource name
#' @param description additional details for the repo
#'
#' @export
DkubeProject <- function(user = NULL, name = NULL){
  model <- dkube$sdk$rsrcs$DkubeProject(user, name = name)
}

#' Dkube Featureset
#'
#' @param user username
#' @param name repo/resource name
#' @param description additional details for the repo
#'
#' @export
DkubeFeatureSet <- function(user = NULL, name = NULL){
  model <- dkube$sdk$rsrcs$DkubeFeatureSet(user, name = name)
}
