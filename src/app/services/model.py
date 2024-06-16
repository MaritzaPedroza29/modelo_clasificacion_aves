import csv
import joblib
import numpy as np
from tensorflow.keras.utils import load_img, img_to_array

ruta = "app/assets/model_aves.pkl"
model = joblib.load(ruta)

class_names_set = set()
directory = "app/assets/birds.csv"
with open(directory) as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
        class_names_set.add(row[2])

class_names = list(class_names_set)

def clasificar(vector):
    global class_names, model
    
    # Hacer la predicción usando el modelo
    model_predict = model.predict(vector)
    
    # Obtener la clase predicha y la probabilidad más alta
    pred_class_idx = np.argmax(model_predict)
    pred_class = class_names[pred_class_idx]
    max_probability = np.max(model_predict)
    
    return pred_class, max_probability
