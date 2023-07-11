from deepface import DeepFace

import cv2

imagem = cv2.imread("./img/1.png")

resultado = DeepFace.analyze(imagem, actions=("age", "emotion", "gender"))

print(resultado)

