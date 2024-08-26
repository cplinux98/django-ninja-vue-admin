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

from pathlib import Path
from decouple import AutoConfig

# 找到项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
print(BASE_DIR)

# 读取.env文件
config = AutoConfig(search_path=BASE_DIR.joinpath('config'))
print(BASE_DIR.joinpath('config'))