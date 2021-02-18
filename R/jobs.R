#' Dkube Preprocressing job
#'
#' @param user username
#' @param name job name
#' @param description additional details for the run
#'
#' @export
DkubePreprocessing <- function(user = NULL, name = NULL, description = NULL){
  preprocessing <- dkube$sdk$rsrcs$DkubePreprocessing(user, name=name, description=description)
}

#' Dkube Training job
#'
#' @param user username
#' @param name job name
#' @param description additional details for the run
#'
#' @export
DkubeTraining <- function(user = NULL, name = NULL, description = NULL){
  trainig <- dkube$sdk$rsrcs$DkubeTraining(user, name=name, description=description)
}

#' Dkube Serving job
#'
#' @param user username
#' @param name job name
#' @param description additional details for the run
#'
#' @export
DkubeServing <- function(user = NULL, name = NULL, description = NULL){
  serving <- dkube$sdk$rsrcs$DkubeServing(user, name=name, description=description)
}

#' Dkube IDE job
#'
#' @param user username
#' @param name job name
#' @param description additional details for the run
#'
#' @export
DkubeIDE <- function(user = NULL, name = NULL, description = NULL){
  serving <- dkube$sdk$rsrcs$DkubeIDE(user, name=name, description=description)
}
