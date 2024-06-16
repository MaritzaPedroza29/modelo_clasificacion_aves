from tensorflow.keras.utils import load_img, img_to_array
from PIL import Image
import numpy as np

def  getVectorIMG(image: Image.Image) -> np.ndarray:
    #img = load_img(filename,target_size=(224,224))
    image = image.resize((224, 224))
    img_array = img_to_array(image)
    # Expandir las dimensiones si es necesario (opcional)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array