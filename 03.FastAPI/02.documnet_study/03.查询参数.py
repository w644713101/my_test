from fastapi import FastAPI
from typing import Union
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# 声明不属于路径参数的其他函数参数时，它们将被自动解释为"查询字符串"参数
@app.get('/items')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip+limit]


# 可选参数
"""
Optional[X] 等价于 X | None （或 Union[X, None] ）
"""
@app.get('/items/{items_id}')
async def read_item2(items_id: str, q: Union[str, None] = None):
    if q:
        return {'data': f'hava q {q}'}
    return {'data': "don't have q"}


# 查询参数类型转换
"""
short: bool = False
在不传入short 的时候会有默认赋值参数
在传入参数的时候，会把传入的值转成bool类型，如果转类型失败会报错

如果改成 short = False
则传入的short 的类型是 string
"""
@app.get('/items2/{item_id}')
async def read_item3(item_id: str, q: Union[str, None] = None, short: bool=False):
    print(type(short))
    return {'data': str(type(short))}


# 必须查询参数
"""
当你想让一个查询参数成为必需的，不声明任何默认值就可以, 比如needy参数
"""
@app.get('/items3/{item_id}')
async def read_item4(item_id: str, needy: str):
    return item_id
