#cmd: uvicorn api:app --reload

import os
import json
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from deepface import DeepFace
import numpy as np

def serialize(obj):
    if isinstance(obj, np.bool_):
        return bool(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


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
        resultado = DeepFace.analyze(file.filename, actions=("age", "emotion", "gender", "race"), detector_backend='mtcnn')
        os.remove(file.filename)
        
    return resultado

@app.post("/verify")
async def analyze_face(image1: UploadFile = File(...), image2: UploadFile = File(...)):
    with open(image1.filename, "wb") as f1:
        f1.write(await image1.read())

    with open(image2.filename, "wb") as f2:
        f2.write(await image2.read())

    resultado = DeepFace.verify(img1_path = image1.filename, img2_path = image2.filename, model_name='Facenet')

    os.remove(image1.filename)
    os.remove(image2.filename)

    json_string = json.dumps(resultado, default=serialize)
    json_object = json.loads(json_string)

    return json_object
