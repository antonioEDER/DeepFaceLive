#cmd: uvicorn api:app --reload

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from deepface import DeepFace

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

