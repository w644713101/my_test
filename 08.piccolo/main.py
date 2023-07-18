# piccolo-fastapi/main.py
from fastapi import FastAPI
from orm import ForeignKey, Integer
from piccolo.apps.user.tables import BaseUser
from piccolo.columns import Varchar
from piccolo.engine import engine_finder
from piccolo.table import Table
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Band(Table, tablename='music_band'):
    name = Varchar(length=100)
    popularity = Integer()


@app.on_event("startup")
async def startup():
    engine = engine_finder()
    await engine.start_connection_pool()
    # await BaseUser.create_table().run()
    await Band.create_table()


@app.on_event("shutdown")
async def shutdown():
    engine = engine_finder()
    await engine.close_connection_pool()


@app.get("/")
async def root():
    return {"message": "Hello World"}
