# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 10:43
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 22.路径操作装饰器依赖项.py
from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


async def verify_token(x_token: str = Header(default=None)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(default=None)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


# 无论路径装饰器依赖项是否返回值，路径操作都不会使用这些值。
@app.get('/items', dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
