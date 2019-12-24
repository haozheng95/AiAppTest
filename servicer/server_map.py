#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yinhaozheng
@software: PyCharm
@file: server_map.py
@time: 2019-12-23 15:15
"""
import os

import pytest
import requests

__mtime__ = '2019-12-23'

AccessMap = {
    "idcardocr": "7001",
    "mathai": "7002",
    "nowatermark": "7003",
    "license-plate-recognition": "7004",
    "image-stitching": "7005",
    "opencv-car-location": "7006",
    "playing-card-recognition": "7007",
    "chinese-ocr": "7008",
    "faceai-gender": "7009/gender",
    "faceai-colorize": "7009/colorize",
    "faceai-compose": "7009/compose",
    "faceai-detectionOpencv": "7009/detectionOpencv",
    "faceai-emotion": "7009/emotion",
    "faceai-faceRecognitionMakeup": "7009/faceRecognitionMakeup",
    "faceai-faceRecognitionOutline": "7009/faceRecognitionOutline",
}

baseUrl = "http://47.105.165.164:7010"
fileDir = "../data"

requestOneList = [
    {"url": baseUrl + "/mathai", "file": os.path.join(fileDir, "math_ai.jpg")},
    {"url": baseUrl + "/license-plate-recognition", "file": os.path.join(fileDir, "licensePlateRecognition.jpg")},
    {"url": baseUrl + "/opencv-car-location", "file": os.path.join(fileDir, "opencv_car_location.jpg")},
    {"url": baseUrl + "/chinese-ocr", "file": os.path.join(fileDir, "chinese_ocr_2.png")},
    {"url": baseUrl + "/idcardocr", "file": os.path.join(fileDir, "idcardocr.jpg")},
]

faceAiDir = os.path.join(fileDir, "faceai")
requestFaceAiList = [
    {"url": baseUrl + "/faceai-gender", "file": os.path.join(faceAiDir, "gather.png")},
    {"url": baseUrl + "/faceai-colorize", "file": os.path.join(faceAiDir, "colorize2.png")},
    {"url": baseUrl + "/faceai-compose", "file": os.path.join(faceAiDir, "compose.png")},
    {"url": baseUrl + "/faceai-detectionOpencv", "file": os.path.join(faceAiDir, "xingye-1.png")},
    {"url": baseUrl + "/faceai-emotion", "file": os.path.join(faceAiDir, "emotion.png")},
    {"url": baseUrl + "/faceai-faceRecognitionMakeup", "file": os.path.join(faceAiDir, "ag.png")},
    {"url": baseUrl + "/faceai-faceRecognitionOutline", "file": os.path.join(faceAiDir, "ag.png")},
]


def requestOne(file, url):
    with open(file, "rb") as f:
        files = {'file': f}
        response = requests.post(url=url, files=files)
    return dict(status_code=response.status_code, content=response.json(), response=response)


def testNginxRequestOne():
    for content in requestOneList:
        print(content)
        result = requestOne(content["file"], content["url"])
        print(result)


def tesstNginxRequestFaceAi():
    for content in requestFaceAiList:
        print(content)
        result = requestOne(content["file"], content["url"])
        print(result)


if __name__ == '__main__':
    # tesstNginxRequestFaceAi()
    content = {'url': 'http://47.105.165.164:7010/faceai-gender', 'file': '../data/faceai/gather.png'}
    # content = {'url': 'http://47.105.165.164:7009/gender', 'file': '../data/faceai/gather.png'}
    result = requestOne(content["file"], content["url"])
    print(result)
