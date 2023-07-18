from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'hello world'}

# 代码粘到 main.py 里面，
"""
uvicorn main:app 命令含义如下:
    main：main.py 文件（一个 Python「模块」）。
    app：在 main.py 文件中通过 app = FastAPI() 创建的对象。
    --reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。
"""
