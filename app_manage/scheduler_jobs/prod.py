#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2020/11/11 10:59
@Author  : CQ
@Describe:
"""

from hero_nanchang.traffic_data_service import main as ods_video_det_data_pd
from hero_nanchang.traffic_data_service.scheduler_job.traffic_device_status_data.device_status_data_fetch import main as device_status_update
import traceback
import logging
import datetime as dt
import socket
from apscheduler.schedulers.background import BackgroundScheduler
service_logger = logging.getLogger('scheduler_logger')
scheduler = BackgroundScheduler(daemonic=True)
# scheduler.add_jobstore(DjangoJobStore(), "default")

def get_sharp_timestamp(minute):
    """
    计算当前时间之后最近的minute整点时间
    :return:
    """
    now = dt.datetime.now()
    time_diff = minute - now.minute % minute
    return now + \
           dt.timedelta(minutes=time_diff) - \
           dt.timedelta(seconds=now.second) - dt.timedelta(microseconds=now.microsecond)


def create_scheduler():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", 47200))
    except socket.error:
        print("!!!scheduler already started, DO NOTHING")
    else:

        # start_scheduler = get_conf_value(section='control_pram',option='if_scheduler')
        scheduler = BackgroundScheduler(daemonic=True)
        scheduler.start()
        # 清理历史任务
        scheduler.remove_all_jobs()
        try:
            # 清理历史任务
            # scheduler.remove_all_jobs()
            current_time = dt.datetime.now()
            scheduler.add_job(ods_video_det_data_pd, 'interval', minutes=1, start_date=current_time,
                              id='ods_video_det_data_pd', replace_existing=True)  # 添加监控任务：检测器ods数据转存kafka
            # scheduler.add_job(road_ranking_data, 'interval', minutes=2, start_date=current_time,
            #                   id='road_ranking_data_interval', replace_existing=True)  # 添加监控任务：高德openAPI道路指数
            # scheduler.add_job(road_ranking_data, 'date', run_date=current_time,
            #                   id='road_ranking_data_date', replace_existing=True)  # 添加监控任务：高德openAPI道路指数
            # scheduler.add_job(device_status_update, 'date', run_date=current_time,
            #                   id='device_status_update_date', replace_existing=True)  # 添加监控任务：设备状态更新
            scheduler.add_job(device_status_update, 'interval', minutes=10, start_date=current_time,
                              id='device_status_update_interval', replace_existing=True)  # 添加监控任务：设备状态更新

            # register_events(scheduler)
        except Exception as e:
            print(e)
            traceback.print_exc()
            # 报错则调度器停止执行
            scheduler.shutdown()
        else:
            # logger.info('[*traffic_alarm] start scheduler task！job list [%s]' % scheduler.get_jobs())
            print("=======================scheduler start==========================")


# create_scheduler()


def clear_scheduler():
    scheduler.remove_all_jobs()
    # logger.info('[*traffic_alarm] start scheduler task！job list [%s]' % scheduler.get_jobs())
    print("=======================scheduler stoped==========================")

