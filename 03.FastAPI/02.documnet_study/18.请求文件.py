# -*- coding: utf-8 -*-
# @Time    : 2023/7/10 18:00
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 18.请求文件.py
from typing import List

from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post('/files')
async def create_file(file: bytes = File(default=None)):
    return {'file_size': len(file)}


@app.post('/upload_files')
async def create_upload_files(file: UploadFile = File(default=None)):
    return {'filename': file.filename}


@app.post("/files1/")
async def create_files1(files: List[bytes] = File(default=None)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles1/")
async def create_upload_files1(files: List[UploadFile] = File(default=None)):
    return {"filenames": [file.filename for file in files]}


