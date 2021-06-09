#!/bin/bash
image_name=${PWD##*/}
user_name="gibsoncratus"
sudo docker build -t $user_name/$image_name:latest --push .
