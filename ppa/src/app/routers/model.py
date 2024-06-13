from fastapi.responses import StreamingResponse
from fastapi import APIRouter
import pandas as pd
import io
from app.services.model import clasificar
from app.utils.getVectorIMG import getVectorIMG

model = APIRouter(tags=['Model'])

@get_predict.get("/model", response_class=StreamingResponse, summary="recibe imagen y retorna nomb re d ela clase maokdans", description="blablabla")
def predict(img):
    vector = getVectorIMG(img)
    pred = clasificar(vector)
    return pred