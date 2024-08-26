#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File           :    __init__.py
@Time           :    2024/8/26 22:28
@Author         :    cp
@Version        :    1.0
@Email          :    cplinux98@gmail.com
@Description    :    
"""
from os import environ
from pathlib import Path
from split_settings.tools import optional, include

BASE_DIR = Path(__file__).parent.parent.parent

# 使用`DJANGO_ENV` 环境变量来管理加载哪个配置文件:
environ.setdefault('DJANGO_ENV', 'development')
_ENV = environ['DJANGO_ENV']

# 从上到下读取，下面的可以覆盖上面文件中的变量/设置信息
_base_settings = [
    # 加载所有组件
    'components/common.py',
    'components/caches.py',
    'components/database.py',

    # 可选的环境，根据ENV这个变量来选择
    'environments/{0}.py'.format(_ENV),
    # 可选的文件，如果有就加载，没有就不加载
    optional('environments/local.py'),
]

# Include settings:
include(*_base_settings)
