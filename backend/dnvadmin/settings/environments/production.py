#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File           :    production
@Time           :    2024/8/26 22:34
@Author         :    cp
@Version        :    1.0
@Email          :    cplinux98@gmail.com
@Description    :    ENV=production时加载的设置文件
"""
from dnvadmin.settings.components import config


# 生产环境
DEBUG = False
ALLOWED_HOSTS = [
    config('DJANGO_DOMAIN_NAME'),
    'localhost',
]

