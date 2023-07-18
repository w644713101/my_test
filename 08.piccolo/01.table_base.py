# -*- coding: utf-8 -*-
# @Time    : 2023/6/21 15:42
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 01.table_base.py
import asyncio
from piccolo.table import Table, create_db_tables_sync, create_db_tables
from piccolo.columns import ForeignKey, Integer, Varchar, Timestamp, Interval, Numeric, JSONB
from piccolo.engine.postgres import PostgresEngine
from piccolo.testing.model_builder import ModelBuilder


class Manager(Table):
    name = Varchar(length=100)


class Band(Table, tablename='music_band'):
    name = Varchar(length=100)
    manager = ForeignKey(references=Manager)
    popularity = Integer()


class Venue(Table):
    name = Varchar()
    capacity = Integer()


class Concert(Table):
    band_1 = ForeignKey(references=Band)
    band_2 = ForeignKey(references=Band)
    venue = ForeignKey(references=Venue)
    starts = Timestamp()
    duration = Interval()


class Ticket(Table):
    concert = ForeignKey(references=Concert)
    price = Numeric()


class RecordingStudio(Table):
    name = Varchar()
    facilities = JSONB()




async def main():
    # band = await ModelBuilder.build(Band)
    await create_db_tables(Band, Manager, if_not_exists=True)

asyncio.run(main())
