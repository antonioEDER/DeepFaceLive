#cmd: uvicorn api:app --reload

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from deepface import DeepFace
import json

import cv2
import requests
from PIL import Image
from io import BytesIO
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.get("/")
def hello_root():
    return {"message": "Bem vindo"}
 
@app.get("/analyze")
def analyze_face(url_image):
    file = "faceimage.png"
    
    response = requests.get(url_image)
    image = Image.open(BytesIO(response.content))
    image.save(file)

    imread = cv2.imread(file)
    resultado = DeepFace.analyze(imread, actions=("age", "emotion", "gender", "race"))

    os.remove(file)

    return resultado

@app.get("/verify")
def analyze_face(url_image1,url_image2):
    file1 = "faceimage1.png"
    file2 = "faceimage2.png"
    
    response1 = requests.get(url_image1)
    image1 = Image.open(BytesIO(response1.content))
    image1.save(file1)

    response2 = requests.get(url_image2)
    image2 = Image.open(BytesIO(response2.content))
    image2.save(file2)

    resultado = DeepFace.verify(img1_path = file1, img2_path = file2)

    os.remove(file1)
    os.remove(file2)

    return str(resultado)
