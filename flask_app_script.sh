#!/bin/bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker build -t flask_docker .
docker run -p 5000:5000 -t flask_docker