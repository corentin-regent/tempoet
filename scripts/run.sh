#!/bin/bash

image_name=tempoet

docker build -t $image_name .
docker run --user $(id -u) -i --rm -v .:/output $image_name
