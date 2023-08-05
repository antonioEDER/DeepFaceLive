
import os
import json

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from deepface import DeepFace

import numpy as np

class DeepFaceAnalyzer:
    def analyze(self, image_path: str) -> dict:
        resultado = DeepFace.analyze(image_path, actions=("age", "emotion", "gender", "race"), detector_backend='mtcnn')
        os.remove(image_path)
        return resultado

class FaceVerifier:
    def verify(self, image_path1: str, image_path2: str) -> dict:
        resultado = DeepFace.verify(img1_path=image_path1, img2_path=image_path2, model_name='Facenet')
        os.remove(image_path1)
        os.remove(image_path2)
        return resultado

class JsonSerializable:
    def serialize(self, obj):
        if isinstance(obj, np.bool_):
            return bool(obj)
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

def serialize(obj):
    if isinstance(obj, np.bool_):
        return bool(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

deep_face_analyzer = DeepFaceAnalyzer()
face_verifier = FaceVerifier()
json_serializer = JsonSerializable()

app.get("/")
def hello_root():
    return {"message": "Bem vindo"}

@app.post("/analyze")
async def analyze_face(file: UploadFile = File(...)):
    image_path = file.filename
    with open(image_path, "wb") as f:
        f.write(await file.read())
    resultado = deep_face_analyzer.analyze(image_path)
    return resultado

@app.post("/verify")
async def analyze_face(image1: UploadFile = File(...), image2: UploadFile = File(...)):
    image_path1 = image1.filename
    image_path2 = image2.filename

    with open(image_path1, "wb") as f1:
        f1.write(await image1.read())

    with open(image_path2, "wb") as f2:
        f2.write(await image2.read())

    resultado = face_verifier.verify(image_path1, image_path2)
    print(resultado)

    json_string = json.dumps(resultado, default=serialize)
    json_object = json.loads(json_string)

    return json_object