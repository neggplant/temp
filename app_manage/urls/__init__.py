#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2020/11/10 11:05
@Author  : XJC
@Describe:
"""

from django.conf import settings
# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
# print(os.environ)
if settings.CITY == 'hz':
    from .dev import *
