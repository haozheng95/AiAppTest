#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yinhaozheng
@software: PyCharm
@file: docker_tools.py
@time: 2019-12-05 10:02
"""

__mtime__ = '2019-12-05'
import subprocess

dockerUser = "yinhaozheng"
tagVersion = "latest"


def processDockerShell(image):
    name, tag = image
    new = renameDockerShell(name, tag)
    pushDockerShell(new)


def findDockerShell():
    shell = "docker images | grep web"
    docker_images = subprocess.check_output(shell, shell=True)
    result = []
    for image in docker_images.decode().split("\n"):
        temp = [x for x in image.split(" ") if x != ""]
        if dockerUser in image:
            print("discard----->", image)
            continue
        print(image)
        if len(temp) > 2:
            result.append(temp[:2])
    return result


def renameDockerShell(name, tag):
    old = name + ":" + tag
    new = dockerUser + "/" + name + ":" + tagVersion
    shell = "docker tag " + old + " " + new
    subprocess.call(shell, shell=True)
    return new


def pushDockerShell(docker_info):
    print(docker_info)
    shell = "docker push " + docker_info
    subprocess.call(shell, shell=True)


def removeDockerShell(name, tag):
    docker_info = name + ":" + tag
    print("delete ----------> ", docker_info)
    shell = "docker rmi " + docker_info
    subprocess.call(shell, shell=True)


def main():
    images = findDockerShell()
    for image in images:
        # processDockerShell(image)
        removeDockerShell(image[0], image[1])


if __name__ == '__main__':
    main()
    # pushDockerShell("yinhaozheng/web-python36-faceai:latest")
