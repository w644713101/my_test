from pydantic import BaseModel, ValidationError
import pandas as pd
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: int  # 必须字段
    name: str = "John Snow"
    signup_ts: Optional[datetime] = datetime.today()


# df = pd.read_excel('test.xlsx')
#
# for row in df.itertuples():
#     print(getattr(row, 'id'), getattr(row, 'test'))  # 输出每一行
#     # print(type(getattr(row, 'id')))
#     # print(type(row))
#     # print(len(row))
#     # print(row[0])
#     # print(row[1])
#     # print(row[2])
#     for i in range(1, len(row)):
#         print('row[i]', row[i])
#
#     print('-'*20)

user = User(**{'id': 123, 'name': 'user'})
print(user.signup_ts)




