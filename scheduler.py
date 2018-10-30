#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ************************************************************************ 
# * 
# * @file: cheduler.py 
# * @author: suruoxi
# * @mail: monkeycarbon@gmail.com
# * @date: 2018-10-30 11:52 
# * @version 1.0  
# * @description: Python Script 
# * @Copyright (c)  all right reserved 
# * 
#************************************************************************* 

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

from chinese_calendar import is_workday, is_holiday
import time
import requests

# url.txt是存储钉钉webhook的文件，只有一行
ding_url = open('url.txt').read().strip()


def workday_msg(localtime):
    if localtime.tm_hour in [10,14,15,16,19,20]:
        return "该喝水啦"
    if localtime.tm_hour in [11,15,16,17,19,20]:
        return "该互动一下啦"
    if lcoaltime.tm_hour == 24:
        return "该睡觉啦"
    return None

def holiday_msg(localtime):
    return None

sched = BlockingScheduler()

def alarm_clock():
    date = datetime.date.today()
    localtime = time.localtime(time.time())
    if is_holiday(date):
        text = holiday_msg(localtime)
    elif is_workday(date):
        text = workday_msg(localtime)

    if text is not None:
        msg_body = {"msgtype": "text",
            "text": {"content": text},
            "at": { "isAtAll": True}
            }
        ret = requests.post(ding_url, json = msg_body)

sched.add_job(func=alarm_clock, trigger='cron', hour='0-23', start_date='2018-10-30 14:00:00')
sched.start()


