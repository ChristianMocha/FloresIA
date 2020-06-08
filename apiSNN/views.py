from django.core.files.storage import FileSystemStorage

import os
from django.shortcuts import render


from apiSNN.logica import modeloCNN





class MachineLearning():
    # imagen = models.ImageField(upload_to='imagenes')
    # prediccion = models.CharField(max_length=200, blank=True)
    def index(request):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        if request.method == 'POST':
            archivo = request.FILES['imagen']

            fileStorage = FileSystemStorage()
            fileStorage.save(archivo.name, archivo)
            file = BASE_DIR + '/foto/' + archivo.name
            retorno = modeloCNN.predecir(file)


            return render(request, "prediccion.html",
                          {"flower": retorno.get('flor'), "porcentaje": retorno.get('prediccion')})

        return render(request, 'index.html')



