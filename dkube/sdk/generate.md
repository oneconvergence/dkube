## Generate SDK internal files

1. Get latest API swagger YAML file from GPU as a service latest dev branch.
2. Convert into JSON using swagger editor **https://editor.swagger.io/**
3. Create a directory in PWD named **out/python** and keep swagger.json in PWD.
4. Run `docker run -v ${PWD}:/local swaggerapi/swagger-codegen-cli:2.4.18 generate -i /local/swagger.json -l python -o /local/out/python -DpackageName=dkube_api` 
5. Replace `dkube_api` with `dkube.sdk.internal.dkube_api` in all the files in `out/python/dkube_api`. 
6. Delete the directory `dkube/sdk/internal/dkube_api` from SDK repo
7. Copy `out/python/dkube_api` into `dkube/sdk/internal`.