# -*- coding: utf-8 -*-
# @Time    : 2023/7/10 10:52
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : app.py
import json
import asyncio
from connect4 import PLAYER1, PLAYER2
import websockets


async def handler2(websocket):
    # 断开会报错
    while True:
        message = await websocket.recv()
        print(message)


async def handler3(websocket):
    # 用捕捉异常的方式解决断开会报错
    while True:
        try:
            message = await websocket.recv()
        except websockets.ConnectionClosedOK:
            break
        print(message)


async def handler4(websocket):
    # 更方便的方式实现断开会报错
    async for message in websocket:
        print(message)


async def handler(websocket):
    for player, column, row in [
        (PLAYER1, 3, 0),
        (PLAYER2, 3, 1),
        (PLAYER1, 4, 0),
        (PLAYER2, 4, 1),
        (PLAYER1, 2, 0),
        (PLAYER2, 1, 0),
        (PLAYER1, 5, 0),
    ]:
        event = {
            "type": "play",
            "player": player,
            "column": column,
            "row": row,
        }
        await websocket.send(json.dumps(event))
        await asyncio.sleep(0.5)
    event = {
        "type": "win",
        "player": PLAYER1,
    }
    await websocket.send(json.dumps(event))


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
