from typing import Union
from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items1/')
async def read_items(q: Union[str, None] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({'q': q})
    return results


"""使用Query"""
@app.get('/items2/')
async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({'q': q})
    return results

