# -*- coding: utf-8 -*-
# @Time    : 2023/7/10 16:16
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 12.cookie参数.py
from typing import Union
from fastapi import Cookie, FastAPI


app = FastAPI()


@app.get('/items/')
async def read_items(ads_id: Union[str, None] = Cookie(default=None)):
    return {'ads_id': ads_id}



