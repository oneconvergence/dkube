#' @export
DkubeAPI <- function(url = NULL, token){
  dkubeapi <- dkube$sdk$DkubeApi
  api <- dkubeapi(token = token)
}
