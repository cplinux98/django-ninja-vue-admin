#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File           :    caches
@Time           :    2024/8/26 22:50
@Author         :    cp
@Version        :    1.0
@Email          :    cplinux98@gmail.com
@Description    :    
"""
# 配置缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}