#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File           :    development
@Time           :    2024/8/26 22:35
@Author         :    cp
@Version        :    1.0
@Email          :    cplinux98@gmail.com
@Description    :    ENV=development时加载的设置文件
"""
from dnvadmin.settings.components import config

print("加载了开发环境")




# 设置开发环境
DEBUG = True

ALLOWED_HOSTS = ['*']

# 开发时使用sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}