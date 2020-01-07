#!/usr/bin/env bash

git_result=`git pull`;
echo "git result are \n $git_result";

down_result=`docker-composer down`;
echo "down result are \n $down_result";

up_result=`docker-composer -d`;
echo "up result are \n $up_result";
