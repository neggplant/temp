#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2020/11/11 10:59
@Author  : CQ
@Describe:
"""

from django.conf import settings
# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
# print(os.environ)
if settings.CITY == 'hz':
   from .dev import create_scheduler,clear_scheduler
elif settings.CITY == 'nc':
   from .prod import create_scheduler,clear_scheduler