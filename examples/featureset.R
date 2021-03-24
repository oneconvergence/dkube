library(dkubeR)

# generating featureset name
fs_name = generate("fs-test")
print(fs_name)

# Creating featureset
create_featureset(name=fs_name)

# defining dataframe
data <- data.frame(
  emp_id = c (1:5),
  emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
  salary = c(623.3,515.2,611.0,729.0,843.25),
  start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11",
                         "2015-03-27")),
  stringsAsFactors = FALSE
)

# Committing featureset
commit_featureset(name=fs_name, df=data)

# Reading featureset
r_df = read_featureset(name=fs_name)
print(r_df)
