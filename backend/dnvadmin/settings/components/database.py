#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File           :    database
@Time           :    2024/8/26 23:25
@Author         :    cp
@Version        :    1.0
@Email          :    cplinux98@gmail.com
@Description    :    
"""
from dnvadmin.settings.components import config

DATABASES = {
  'default': {
    'ENGINE'  : 'django.db.backends.' + config('DJANGO_DB_ENGINE'),
    'NAME'    : config('DJANGO_DB_NAME'),
    'USER'    : config('DJANGO_DB_USERNAME'),
    'PASSWORD': config('DJANGO_DB_PASSWORD'),
    'HOST'    : config('DJANGO_DB_HOST'),
    'PORT'    : config('DJANGO_DB_PORT'),
    },
}
