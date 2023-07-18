# @Time    : 2023/7/10 17:21
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 14.响应模型.py
from typing import Any, Union, List
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get('/items1/{item_id}', response_model=Item, response_model_exclude_unset=True)
async def read_item1(item_id: str):
    return items[item_id]


@app.get('/items2/{item_id}', response_model=Item, response_model_include={'name', 'description'})
async def read_items2(item_id: str):
    return items[item_id]


@app.get('/items3/{item_id}', response_model=Item, response_model_exclude={'tax'})
async def read_items3(item_id: str):
    return items[item_id]


