from keras.preprocessing import image
import numpy as np
from keras import backend as k
from tensorflow.keras.models import model_from_json


def predecir(url_imagen):

    print(url_imagen)

    imagen = image.load_img(path=url_imagen, target_size=(150, 150, 3))
    imagen = image.img_to_array(imagen)
    imagen /= 255
    imagen = np.expand_dims(imagen, axis= 0)

    #print(imagen.name)
    modelo = cargarModelo(r'apiSNN/logica/arquitectur', r'apiSNN/logica/pes')
    print('mo')
    print(modelo)
    prediccion = modelo.predict(imagen)
    dc = None
    for i in prediccion:
        dc = i
    for l in dc:
        print(l*100)

    maximo = max(dc)
    round(maximo*100, 2)
    i, = np.where(np.isclose(dc, maximo))
    retorno = dict()

    if i[0] == 0:
        retorno['pred'] = 'sunflower'
        retorno['porcentaje'] = round(maximo*100, 2)
    elif i[0] == 1:
        retorno['pred'] = 'tulip'
        retorno['porcentaje'] = round(maximo*100, 2)
    elif i[0] == 2:
        retorno['pred'] = 'daisy'
        retorno['porcentaje'] = round(maximo*100, 2)
    elif i[0] == 3:
        retorno['pred'] = 'rose'
        retorno['porcentaje'] = round(maximo*100, 2)
    elif i[0] == 4:
        retorno['pred'] = 'dandelion'
        retorno['porcentaje'] = round(maximo*100, 2)


    return retorno


def cargarModelo(url_modelo, url_pesos):
    k.reset_uids()
    with open(url_modelo + '.json', 'r') as f:
        modelo = model_from_json(f.read())

    modelo.load_weights(url_pesos + '.h5')
    return modelo