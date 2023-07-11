#cmd: uvicorn api:app --reload

from fastapi import FastAPI, File, UploadFile

from fastapi.middleware.cors import CORSMiddleware

from deepface import DeepFace

import cv2

import requests

from PIL import Image

from io import BytesIO

import os

from typing_extensions import Annotated


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.get("/")
def hello_root():
    return {"message": "Bem vindo"}
 
@app.post("/analyze")
async def analyze_face(file: UploadFile = File(...)):
    with open(file.filename, "wb") as f:
        f.write(await file.read())
        resultado = DeepFace.analyze(file.filename, actions=("age", "emotion", "gender", "race"))
        os.remove(file.filename)
    return resultado

@app.post("/verify")
async def analyze_face(url_image1: UploadFile = File(...), url_image2: UploadFile = File(...)):
    with open(url_image1.filename, "wb") as f1:
        f1.write(await url_image1.read())

    with open(url_image2.filename, "wb") as f2:
        f2.write(await url_image2.read())

    resultado = DeepFace.verify(img1_path = url_image1.filename, img2_path = url_image2.filename)

    os.remove(url_image1.filename)
    os.remove(url_image2.filename)

    return str(resultado)
