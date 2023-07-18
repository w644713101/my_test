from fastapi import FastAPI
from enum import Enum
app = FastAPI()


# 路径参数
@app.get('/items/{item_id}')
async def read_item(item_id):
    return {'item_id': item_id}


# 有类型的路径参数
@app.get('/items2/{item_id}')
async def read_item2(item_id: int):
    return {'item_id': item_id}
"""
顺序很重要
在创建路径操作时，你会发现有些情况下路径是固定的。

比如 /users/me，我们假设它用来获取关于当前用户的数据.

然后，你还可以使用路径 /users/{user_id} 来通过用户 ID 获取关于特定用户的数据。

如果/users/me 在 /users/{user_id} 的后面
如果访问固定的 /users/me 会误把 user_id 解析成 me
"""


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# 枚举类型参数
@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {'model_name': model_name, 'message': 'deep'}

    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'lecnn'}

    return {'model_name': model_name, 'message': 'residuals'}


# 路径转换器
# 如果不加 :path 会拼接成路径
# 如果加上 :path 会传参的形式实现
@app.get('/files/{file_path: path}')
async def read_file(file_path: str):
    return {'file_path': file_path}
