# -*- coding: utf-8 -*-
# @Time    : 2023/7/10 17:49
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 16.响应状态码.py
from fastapi import FastAPI, status

app = FastAPI()


@app.post('/items/', status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {'name': name}

















