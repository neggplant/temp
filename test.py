#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 11/20/20 1:27 PM
@Author  : CQ
@Describe:
"""
import time
print(time.localtime().tm_wday)

from datetime import datetime, date
print(date.weekday(datetime.now()))