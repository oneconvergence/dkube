dkube <- NULL
.onLoad <- function(libname, pkgname) {
  # use superassignment to update global reference to scipy
  dkube <<- reticulate::import("dkube", delay_load = TRUE)
}
