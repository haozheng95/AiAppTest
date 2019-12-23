#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yinhaozheng
@software: PyCharm
@file: test_func.py
@time: 2019-12-02 11:51
"""
import sys

__mtime__ = '2019-12-02'

import pytest
from request import *
import logging

logging.basicConfig(level=logging.DEBUG)

normalCode = 200


def test_math_ai():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = math_ai()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def test_nowatermark():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = nowatermark()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def test_license_plate_recognition():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = license_plate_recognition()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def test_image_stitching():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = image_stitching()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def test_opencv_car_location():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = opencv_car_location()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def test_playing_card_recognition():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = playing_card_recognition()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def test_chinese_ocr():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = chinese_ocr()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def test_face_ai_gender():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = face_ai_gender()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def test_face_ai_colorize():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = face_ai_colorize()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def test_face_ai_compose():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = face_ai_compose()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def test_face_ai_detection_opencv():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = face_ai_detection_opencv()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def test_face_ai_emotion():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = face_ai_emotion()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def test_face_ai_face_recognition_makeup():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = face_ai_face_recognition_makeup()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def test_face_ai_face_recognition_outline():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = face_ai_face_recognition_outline()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def test_idcardocr():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = idcardocr()
    print_api_details(result, log)
    assert result["status_code"] == normalCode


def print_api_details(result, log):
    request = result["response"].request
    log.debug("request url --------> %s", request.url)
    # log.debug("request body -------> %s", request.body)
    log.debug("request method -----> %s", request.method)
    log.debug("request headers ----> %s", request.headers)
    log.debug("response -----------> %s", result)


if __name__ == '__main__':
    # pytest.main(["-vs"])
    pytest.main()
