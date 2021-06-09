# pytorch-image-model-server-docker
pytorch-image-model-server-docker

## goal 
containerize this in docker container running on arm64/v8
for vidia jetson nano or an nvidia tx2

## steps
1. please read build.sh
1. in build.sh edit the username to be your username for docker
1. please run build.sh to build
1. the build will not run
1. feel free to try qemu arm emulation and buildx for compilation aid (i tried)
1. feel free to change the dockerfile, versions of the libraries, or the base (FROM) docker image
1. feel free to change bring in prebuilt wheels and docker images for arm (ive tried)
1. after building, please run the docker container on nvidia arm device
1. ssh into docker container
1. run model.py
1. if model.py runs succesfully then it is a success

thank you.


