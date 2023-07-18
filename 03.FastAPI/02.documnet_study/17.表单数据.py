# -*- coding: utf-8 -*-
# @Time    : 2023/7/10 17:51
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 17.表单数据.py
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
