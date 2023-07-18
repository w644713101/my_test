# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 10:11
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 20.类作为依赖项.py
from typing import Union
from fastapi import Depends, FastAPI


app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get('/items/')
async def read_items(commons: CommonQueryParams = Depends()):
    response = {}

    if commons.q:
        response.update({'q': commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({'items': items})
    return response




