#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2020/11/11 10:59
@Author  : CQ
@Describe:
"""

import socket
import traceback
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from apple.views import apples_red, apples_green

executors = {
    'default': ThreadPoolExecutor(1),
    'processpool': ProcessPoolExecutor(1)
}
job_defaults = {
    'misfire_grace_time': 1100,
    'max_instances': 20,
    'coalesce': True,
}

scheduler = BackgroundScheduler(daemonic=True, executors=executors, job_defaults=job_defaults)
# scheduler = BackgroundScheduler(daemonic=True, executors=executors, job_defaults=job_defaults)
# scheduler = BackgroundScheduler(daemonic=True, executors=executors, job_defaults=job_defaults)
scheduler.add_jobstore(DjangoJobStore(), "default")


def create_scheduler():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", 27747))
    except socket.error:
        print("!!!scheduler already started, DO NOTHING")
    else:
        if True:
            # 清理历史任务
            scheduler.remove_all_jobs()
            try:
                ######################################evaluation_indicator_zkr########################################
                # 信号专家报警推送
                # 静态报警
                scheduler.add_job(
                    apples_red,
                    'interval', seconds=3,
                    id="apples_red",
                    replace_existing=True
                )
                scheduler.add_job(
                    apples_green,
                    'interval', seconds=3,
                    id="apples_green",
                    replace_existing=True
                )
                # # 静态报警
                # scheduler.add_job(
                #     apples_red,
                #     'interval', minutes=0.1,
                #     id="apples_red1",
                #     replace_existing=True
                # )
                # scheduler.add_job(
                #     apples_green,
                #     'interval', minutes=0.1,
                #     id="apples_green1",
                #     replace_existing=True
                # )
                # # 静态报警
                # scheduler.add_job(
                #     apples_red,
                #     'interval', minutes=0.1,
                #     id="apples_red2",
                #     replace_existing=True
                # )
                # scheduler.add_job(
                #     apples_green,
                #     'interval', minutes=0.1,
                #     id="apples_green2",
                #     replace_existing=True
                # )
                # # 静态报警
                # scheduler.add_job(
                #     apples_red,
                #     'interval', minutes=0.1,
                #     id="apples_red3",
                #     replace_existing=True
                # )
                # scheduler.add_job(
                #     apples_green,
                #     'interval', minutes=0.1,
                #     id="apples_green3",
                #     replace_existing=True
                # )
                # # 静态报警
                # scheduler.add_job(
                #     apples_red,
                #     'interval', minutes=0.1,
                #     id="apples_red4",
                #     replace_existing=True
                # )
                # scheduler.add_job(
                #     apples_green,
                #     'interval', minutes=0.1,
                #     id="apples_green4",
                #     replace_existing=True
                # )
                # # 静态报警
                # scheduler.add_job(
                #     apples_red,
                #     'interval', minutes=0.1,
                #     id="apples_red5",
                #     replace_existing=True
                # )
                # scheduler.add_job(
                #     apples_green,
                #     'interval', minutes=0.1,
                #     id="apples_green5",
                #     replace_existing=True
                # )
            except Exception as e:
                traceback.print_exc()
                scheduler.shutdown()
            else:
                scheduler.start()
                print("=======================scheduler start==========================")


def clear_scheduler():
    scheduler.remove_all_jobs()
    # logger.info('[*traffic_alarm] start scheduler task！job list [%s]' % scheduler.get_jobs())
    print("=======================scheduler stoped==========================")
