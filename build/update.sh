#!/usr/bin/env bash

git_result=`git pull`;
echo "git result are \n $git_result";

down_result=`docker-compose down`;
echo "down result are \n $down_result";

up_result=`docker-compose up -d`;
echo "up result are \n $up_result";
