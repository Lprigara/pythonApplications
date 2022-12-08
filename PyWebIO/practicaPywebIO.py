###################################
### Autor: Leonor Priego García ###
###################################

from predicciones import predecirIris
from pywebio.output import *
from pywebio.input import *

petal_length = input("Indica la longitud del pétalo", type=FLOAT)
petal_width = input("Indica la anchura del pétalo", type=FLOAT)
sepal_length = input("Indica la longitud del sépalo", type=FLOAT)
sepal_width = input("Indica la anchura del sépalo", type=FLOAT)

algoritmo = select("Selecciona un algoritmo de predicción:", ["Random Forest Classifier", "Decision Tree Classifier"])


datosIris = {"sepal_length":[sepal_length],
                     "sepal_width":[sepal_width],
                     "petal_length":[petal_length],
                     "petal_width":[petal_width]}

if algoritmo == "Random Forest Classifier":  
    especiePredecida = predecirIris('rfc', datosIris)
elif algoritmo == "Decision Tree Classifier":
    especiePredecida = predecirIris('dtc', datosIris)


if especiePredecida == "setosa":
    path = 'setosa.jpeg'
elif especiePredecida == "virginica":
    path = 'virginica.jpeg'
elif especiePredecida == 'versicolor': 
    path = 'versicolor.jpeg'


img = open(path, 'rb').read() 

    
popup('La especie predecida es:', [
    put_html('<h3>'+especiePredecida+'</h3>'),
    put_image(img, width='300px'),
])
      
