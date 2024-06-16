import joblib
import numpy as np
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
    global class_names
    pred = np.argmax(model.predict(vector))
    predimg = class_names[pred]