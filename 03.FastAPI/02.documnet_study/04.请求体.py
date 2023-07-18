from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.post('/items')
async def crete_items(items: Item):
    return items


# 请求体+路径参数
@app.put('/items/{items_id}')
async def create_items2(item_id: int, item: Item):
    return {'item_id': item_id, **item.dict()}


# 请求体+路径参数+查询参数
@app.put('/items2/{item_id}')
async def create_item3(item_id: int, item: Item, q: Union[str, None] = None):
    res = {'item_id': item_id, **item.dict()}
    if q:
        res.update({'q': q})

    return res

