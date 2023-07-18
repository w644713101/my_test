# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 09:55
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 19.依赖项_intro.py
from typing import Union

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    skip += 1
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons



