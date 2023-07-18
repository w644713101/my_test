# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 10:37
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 21.子依赖项.py
from typing import Union
from fastapi import Depends, Cookie, FastAPI

app = FastAPI()


def query_extractor(q: Union[str, None] = None):
    return q


def query_or_cookie_extractor(
        q: str = Depends(query_extractor),
        last_query: Union[str, None] = Cookie(default=None)
):
    if not q:
        return last_query
    return q


@app.get('/items/')
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {'q_or_cookie': query_or_default}











