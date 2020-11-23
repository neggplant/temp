#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 11/4/20 2:53 PM
@Author  : CQ
@Describe:
"""
from django.http import JsonResponse
from django.db import connection


def start_scheduler(args):
    from .scheduler_jobs import create_scheduler
    json_demo = {}
    create_scheduler()
    response = JsonResponse(json_demo, safe=False, json_dumps_params={'ensure_ascii': False})
    return response


def end_scheduler(args):
    from .scheduler_jobs import clear_scheduler
    json_demo = {}
    clear_scheduler()
    response = JsonResponse(json_demo, safe=False, json_dumps_params={'ensure_ascii': False})
    return response


def health_check(args):
    try:
        with connection.cursor():
            pass
    except Exception:
        return JsonResponse({'code': 500}, safe=False, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'code': 200}, safe=False, json_dumps_params={'ensure_ascii': False})