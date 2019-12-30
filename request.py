#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yinhaozheng
@software: PyCharm
@file: request.py
@time: 2019-12-02 11:46
"""
import json
import os
import sys

__mtime__ = '2019-12-02'

import requests

baseUrl = "http://47.105.165.164"
baseUrl = "http://127.0.0.1"
fileDir = "data"


# 1
def math_ai():
    port = 7002
    url = baseUrl + ":" + str(port)
    file = os.path.join(fileDir, "math_ai.jpg")
    with open(file, "rb") as f:
        files = {'file': f}
        response = requests.post(url=url, files=files)
    return dict(status_code=response.status_code, content=response.json(), response=response)


def nowatermark():
    port = 7003
    url = baseUrl + ":" + str(port)
    fDir = os.path.join(fileDir, "nowatermark")
    template = os.path.join(fDir, "template.jpg")
    file = os.path.join(fDir, "file.jpg")
    with open(template, "rb") as t:
        with open(file, "rb") as f:
            files = dict(
                template=t,
                file=f
            )
            response = requests.post(url=url, files=files)
    return dict(status_code=response.status_code, content=response.json(), response=response)


# 1
def license_plate_recognition():
    port = 7004
    url = baseUrl + ":" + str(port)
    file = os.path.join(fileDir, "licensePlateRecognition.jpg")
    with open(file, "rb") as f:
        files = {'file': f}
        response = requests.post(url=url, files=files)
    return dict(status_code=response.status_code, content=response.json(), response=response)


def image_stitching():
    port = 7005
    url = baseUrl + ":" + str(port)
    fDir = os.path.join(fileDir, "ImageStitching")
    img1 = os.path.join(fDir, "01_suburbA.jpg")
    img2 = os.path.join(fDir, "01_suburbB.jpg")
    with open(img1, "rb") as t:
        with open(img2, "rb") as f:
            files = dict(
                img1=t,
                img2=f
            )
            response = requests.post(url=url, files=files)
    return dict(status_code=response.status_code, content=response.json(), response=response)


# pass 1
def opencv_car_location():
    port = 7006
    url = baseUrl + ":" + str(port)
    file = os.path.join(fileDir, "opencv_car_location.jpg")
    with open(file, "rb") as f:
        files = {'file': f}
        response = requests.post(url=url, files=files)
    return dict(status_code=response.status_code, content=response.json(), response=response)


# pass
def playing_card_recognition():
    port = 7007
    url = baseUrl + ":" + str(port)
    file = os.path.join(fileDir, "playing-card-recognition.jpg")
    data = {"num_cards": 4}
    with open(file, "rb") as f:
        files = {'file': f}
        response = requests.post(url=url, data=data, files=files)
    return dict(status_code=response.status_code, content=response.json(), response=response)


# pass 1
def chinese_ocr():
    port = 7008
    url = baseUrl + ":" + str(port)
    file = os.path.join(fileDir, "chinese_ocr_2.png")
    with open(file, "rb") as f:
        files = {'file': f}
        response = requests.post(url=url, files=files)
    return dict(status_code=response.status_code, content=response.json(), response=response)


def face_ai_1(name, file):
    port = 7009
    url = baseUrl + ":" + str(port)
    files = {}
    face_ai_data = os.path.join(fileDir, "faceai")
    if name == "compose":
        maozi = os.path.join(face_ai_data, "maozi-1.png")
        decorate = open(maozi, "rb")
        files["decorate"] = decorate
    url += "/" + name

    file = os.path.join(face_ai_data, file)
    with open(file, "rb") as f:
        files['file'] = f
        response = requests.post(url=url, files=files)
    if "decorate" in files:
        files["decorate"].close()
    return dict(status_code=response.status_code, content=response.json(), response=response)


# 分辨性别 pass
def face_ai_gender():
    return face_ai_1("gender", "gather.png")


# 图片重新上色 pass
def face_ai_colorize():
    return face_ai_1("colorize", "colorize2.png")


# 图像加帽子特效 pass
def face_ai_compose():
    return face_ai_1("compose", "compose.png")


# 标出图像中五官的位置 pass
def face_ai_detection_opencv():
    return face_ai_1("detectionOpencv", "xingye-1.png")


# 标出图像中人脸的表情 pass
def face_ai_emotion():
    return face_ai_1("emotion", "emotion.png")


# 数字化妆
def face_ai_face_recognition_makeup():
    return face_ai_1("faceRecognitionMakeup", "ag.png")


# 绘制面部轮廓
def face_ai_face_recognition_outline():
    return face_ai_1("faceRecognitionOutline", "ag.png")


# 身份证识别 pass 1
def idcardocr():
    port = 7001
    headers = {"boundary": "----WebKitFormBoundary7MA4YWxkTrZu0gW"}
    url = baseUrl + ":" + str(port)
    file = os.path.join(fileDir, "idcardocr.jpg")
    with open(file, "rb") as f:
        files = {'file': f}
        response = requests.post(url=url, files=files, headers=headers)
    return dict(status_code=response.status_code, content=response.json(), response=response)


def document_scanner():
    port = 5000
    url = baseUrl + ":" + str(port)
    dir = os.path.join(fileDir, "scanner_doc")
    file = os.path.join(dir, "cell_pic.jpg")
    with open(file, "rb") as f:
        files = {'file': f}
        response = requests.post(url=url, files=files)
    return dict(status_code=response.status_code, content=response.json(), response=response)


if __name__ == '__main__':
    result = document_scanner()
    print(result)
