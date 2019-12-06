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
    log.debug(result)
    assert result["status_code"] == normalCode


def test_nowatermark():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = nowatermark()
    log.debug(result)
    assert result["status_code"] == normalCode


def test_license_plate_recognition():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = license_plate_recognition()
    log.debug(result)
    assert result["status_code"] == normalCode


def test_image_stitching():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = image_stitching()
    log.debug(result)
    assert result["status_code"] == normalCode


def test_opencv_car_location():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = opencv_car_location()
    log.debug(result)
    assert result["status_code"] == normalCode


def test_playing_card_recognition():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = playing_card_recognition()
    log.debug(result)
    assert result["status_code"] == normalCode


def test_chinese_ocr():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = chinese_ocr()
    log.debug(result)
    assert result["status_code"] == normalCode


def test_face_ai_gender():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = face_ai_gender()
    log.debug(result)
    assert result["status_code"] == normalCode


def test_face_ai_colorize():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = face_ai_colorize()
    log.debug(result)
    assert result["status_code"] == normalCode


def test_face_ai_compose():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = face_ai_compose()
    log.debug(result)
    assert result["status_code"] == normalCode


def test_face_ai_detection_opencv():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = face_ai_detection_opencv()
    log.debug(result)
    assert result["status_code"] == normalCode


def test_face_ai_emotion():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = face_ai_emotion()
    log.debug(result)
    assert result["status_code"] == normalCode


def test_face_ai_face_recognition_makeup():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = face_ai_face_recognition_makeup()
    log.debug(result)
    assert result["status_code"] == normalCode


def test_face_ai_face_recognition_outline():
    log = logging.getLogger(sys._getframe().f_code.co_name)
    result = face_ai_face_recognition_outline()
    log.debug(result)
    assert result["status_code"] == normalCode
