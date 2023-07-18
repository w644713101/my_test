# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 10:44
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 23.全局依赖项.py
from fastapi import Depends, FastAPI, Header, HTTPException


async def verify_token(x_token: str = Header(default=None)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(default=None)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key

app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


