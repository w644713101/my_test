#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  # 这里不一定是app，名字随意


class CityInfo(BaseModel):
    province: str
    country: str
    is_affected: Optional[bool] = None  # 与bool的区别是可以不传，默认是null
    # is_affected: bool  如果这样写的话， 必须给 is_affected 赋值一个bool的值

"""
# @实例化的应用 . 请求方法
@app.get('/')
def hello_world():
    return {'hello': 'world'}

"""


"""
@app.get('/city/{city}')  # {city} 是要穿入的参数
@app.get('/city/{city}?q=xxxx')
    两个斜杠之间的叫路径参数
    ?q=xx 叫查询参数  
    查询参数直接在 方法中拿到就行，路径参数要起个名
def result(city: str, query_string: Optional[str] = None):  # Optional 同样是选填的意思
    return {'city': city, 'query_string': query_string}
"""


"""
不同的方法可以用相同的路径
@app.put('/city/{city}')
def result(city: str, city_info: CityInfo):
    return {'city': city, 'country': city_info.country, 'is_affected': city_info.is_affected}
"""

@app.get('/')
async def hello_world():
    return {'hello': 'world'}


@app.get('/city/{city}')
async def result(city: str, query_string: Optional[str] = None):
    return {'city': city, 'query_string': query_string}


@app.put('/city/{city}')
async def result(city: str, city_info: CityInfo):
    return {'city': city, 'country': city_info.country, 'is_affected': city_info.is_affected}

# 启动命令：uvicorn hello_world:app --reload
