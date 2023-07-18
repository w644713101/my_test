# -*- coding: utf-8 -*-
# @Time    : 2023/6/25 15:47
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : piccolo_conf.py
from piccolo.engine import PostgresEngine

DB = PostgresEngine(
    config={
        "database": "postgres",
        "user": "admin",
        "password": "changeme",
        "host": "localhost",
        "port": 15431,
    }
)
