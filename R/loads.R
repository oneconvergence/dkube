dkube <- NULL
.onLoad <- function(libname, pkgname) {
  # use superassignment to update global reference to scipy
  Sys.setenv(FRAMEWORK = "R")
  dkube <<- reticulate::import("dkube", delay_load = TRUE)
}
