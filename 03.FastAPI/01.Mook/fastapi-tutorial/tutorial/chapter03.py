#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from datetime import date
from enum import Enum
from typing import Optional, List

"""
对路径参数进行校验用 Path
对查询参数进行校验用 Query
"""
from fastapi import APIRouter, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Field

app03 = APIRouter()

"""Path Parameters and Number Validations 路径参数和数字验证"""


# 没有传入路径参数
@app03.get("/path/parameters")
def path_params01():
    return {"message": "This is a message"}


# 传入路径参数，用 {} 扩起来，并且扩起来的部分是名字 get中和def函数定义中的 参数名字 要一致
@app03.get("/path/{parameters}")  # 函数的顺序就是路由的顺序，
                                # 当 传入的paramenters的值为 parameters 时， 会先相应👆那个 没有路径参数的的 方法
def path_prams02(parameters: str):
    return {"message": parameters}


class CityName(str, Enum):
    Beijing = "Beijing China"
    Shanghai = "Shanghai China"


@app03.get("/enum/{city}")  # 枚举类型的参数
async def latest(city: CityName):
    if city == CityName.Shanghai:
        return {"city_name": city, "confirmed": 1492, "death": 7}
    if city == CityName.Beijing:
        return {"city_name": city, "confirmed": 971, "death": 9}
    return {"city_name": city, "latest": "unknown"}


#  file_path 后面的 :path 是当 file_path 中含有 / 时，不当做路径，而是当作值，类似转义
@app03.get("/files/{file_path:path}")  # 通过path parameters传递文件路径
def filepath(file_path: str):
    return f"The file path is {file_path}"


@app03.get("/path_/{num}")
def path_params_validate(
    num: int = Path(..., title="Your Number", description="不可描述", ge=1, le=10),
):
    return num


"""Query Parameters and String Validations 查询参数和字符串验证"""


@app03.get("/query")
def page_limit(page: int = 1, limit: Optional[int] = None):  # 给了默认值就是选填的参数，没给默认值就是必填参数
    if limit:
        return {"page": page, "limit": limit}
    return {"page": page}


@app03.get("/query/bool/conversion")  # bool类型转换：yes on 1 True true会转换成true, 其它为false
def type_conversion(param: bool = False):
    return param


@app03.get("/query/validations")  # 长度+正则表达式验证，比如长度8-16位，以a开头。其它校验方法看Query类的源码
def query_params_validate(
    value: str = Query(..., min_length=8, max_length=16, regex="^a"),  # ...换成None就变成选填的参数
    values: List[str] = Query(["v1", "v2"], alias="alias_name")
):  # 多个查询参数的列表。参数别名
    return value, values


"""Request Body and Fields 请求体和字段-----这里的字段是pydantic 的 Field"""


class CityInfo(BaseModel):
    #                   ... 是必填的意思
    name: str = Field(..., example="Beijing")  # example是注解的作用，值不会被验证
    country: str
    country_code: str = None  # 给一个默认值
    country_population: int = Field(default=800, title="人口数量", description="国家的人口数量", ge=800)

    class Config:
        schema_extra = {
            "example": {
                "name": "Shanghai",
                "country": "China",
                "country_code": "CN",
                "country_population": 1400000000,
            }
        }


@app03.post("/request_body/city")
def city_info(city: CityInfo):
    print(city.name, city.country)  # 当在IDE中输入city.的时候，属性会自动弹出
    return city.dict()


"""Request Body + Path parameters + Query parameters 多参数混合"""


@app03.put("/request_body/city/{name}")
def mix_city_info(
    name: str,
    city01: CityInfo,
    city02: CityInfo,  # Body可以是多个的
    confirmed: int = Query(ge=0, description="确诊数", default=0),
    death: int = Query(ge=0, description="死亡数", default=0),
):
    if name == "Shanghai":
        return {"Shanghai": {"confirmed": confirmed, "death": death}}
    return city01.dict(), city02.dict()


@app03.put("/request_body/multiple/parameters")
def body_multiple_parameters(
    city: CityInfo = Body(..., embed=True),  # 当只有一个Body参数的时候，embed=True表示请求体参数嵌套。多个Body参数默认就是嵌套的
    confirmed: int = Query(ge=0, description="确诊数", default=0),
    death: int = Query(ge=0, description="死亡数", default=0),
):
    print(f"{city.name} 确诊数：{confirmed} 死亡数：{death}")
    return city.dict()


"""Request Body - Nested Models 数据格式嵌套的请求体"""


class Data(BaseModel):
    city: List[CityInfo] = None  # 这里就是定义数据格式嵌套的请求体
    date: date  # 额外的数据类型，还有uuid datetime bytes frozenset等，参考：https://fastapi.tiangolo.com/tutorial/extra-data-types/
    confirmed: int = Field(ge=0, description="确诊数", default=0)
    deaths: int = Field(ge=0, description="死亡数", default=0)
    recovered: int = Field(ge=0, description="痊愈数", default=0)


@app03.put("/request_body/nested")
def nested_models(data: Data):
    return data


"""Cookie 和 Header 参数"""


@app03.get("/cookie")  # 效果只能用Postman测试
def cookie(cookie_id: Optional[str] = Cookie(None)):  # 定义Cookie参数需要使用Cookie类，否则就是查询参数
    return {"cookie_id": cookie_id}


@app03.get("/header")
def header(user_agent: Optional[str] = Header(None, convert_underscores=True), x_token: List[str] = Header(None)):
    """
    有些HTTP代理和服务器是不允许在请求头中带有下划线的，所以Header提供convert_underscores属性让设置
    :param user_agent: convert_underscores=True 会把 user_agent 变成 user-agent
    :param x_token: x_token是包含多个值的列表
    :return:
    """
    return {"User-Agent": user_agent, "x_token": x_token}
