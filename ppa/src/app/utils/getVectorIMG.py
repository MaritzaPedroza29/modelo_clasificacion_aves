from tensorflow.keras.utils import load_img, img_to_array
import numpy as np

def getVectorIMG(img):
    #img = load_img(filename,target_size=(224,224))
    imgconv = img_to_array(img)
    img_array = np.expand_dims(imgconv,axis=0)

    return img_array