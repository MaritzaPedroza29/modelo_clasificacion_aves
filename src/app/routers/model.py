from fastapi.responses import StreamingResponse, JSONResponse
from fastapi import APIRouter, FastAPI, File, UploadFile
import pandas as pd
from PIL import Image
from io import BytesIO
from app.services.model import clasificar
from app.utils.getVectorIMG import getVectorIMG

model_predict = APIRouter(tags=['Model'])

@model_predict.post("/model", response_class=StreamingResponse)
async def predict(file: UploadFile = File(...)):
    print("aquí")
    image = Image.open(BytesIO(await file.read()))
    vector = getVectorIMG(image)
    pred_class, max_probability = clasificar(vector)
    # Convertir max_probability a float para asegurar que sea serializable a JSON
    max_probability = float(max_probability)
    
    # Crear el JSON response
    return JSONResponse({"class": pred_class, "probability": max_probability})