#!/usr/bin/env bash
git pull https://github.com/zaibandr/dockerizing-tfind
docker-compose down
docker volume rm webdata_app
docker-compose build
docker-compose up -d