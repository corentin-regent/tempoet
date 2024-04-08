#!/bin/bash

image_name=tempoet

docker build -t $image_name .
docker run --user $(id -u) -i --rm --mount type=bind,src=$(pwd),dst=/output $image_name
