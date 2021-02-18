#' Dkube storage
#'
#' @param type type of dkube resource (program/dataset/model/featureset)
#' @param kind Kind of volume to be exported  (input/output/intermediate)
#' @param name name of the resource
#' @param version version of the resource (in v1,v2 format). default is 'latest' (Optional)
#'
#' @export
DkubeResourcePVC <- function(type, kind, name, version='latest'){
  preprocessing <- dkube$sdk$rsrcs$DkubeResourcePVC(type, kind, name, version='latest')
}
