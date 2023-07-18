# -*- coding: utf-8 -*-
# @Time    : 2023/7/10 16:22
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 13.header参数.py
from typing import Union
from fastapi import FastAPI, Header


app = FastAPI()


@app.get('/items/')
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {'User-Agent': user_agent}


@app.get('/items2')
async def read_item2(
        strange_header: Union[str, None] = Header(default=None, convert_underscores=False)
):
    return {'strange_header': strange_header}

