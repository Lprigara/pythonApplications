
###################################
### Autor: Leonor Priego García ###
###################################

from predicciones import predecir
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QDoubleValidator, QIntValidator
import numpy as np

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = QMainWindow()
    ventana.setGeometry(800, 100, 500, 420)
    ventana.setWindowTitle("Predice la supervivencia de un pasajero en el Titanic")

    ## FUNCTIONS ##
    def predecirSupervivenciaTitanic():
        input_data, algoritmo = obtenerDatosEntrada()
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        
        sobrevive = predecir(algoritmo, input_data_reshaped)
        if sobrevive==0:
            QMessageBox.about(ventana, "Supervivencia Titanic", 
                              "El pasajero indicado muere")
        if sobrevive==1:
            QMessageBox.about(ventana, "Supervivencia Titanic", 
                              "El pasajero indicado sobrevive")


    def obtenerDatosEntrada():
        algoritmo = algoritmoInput.currentIndex()
        clase = int(clasePasajerosInput.currentText())
        sexo = sexoInput.currentIndex()
        edad = int(edadInput.text())
        sibSp = int(sibSpInput.text())
        parch = int(parchInput.text())
        fare = float(fareInput.text().replace(',','.'))
        embarked = embarkedInput.currentIndex()          

        return (clase,sexo,edad,sibSp,parch,fare,embarked), algoritmo
        
        
    ## LABELS ##
    label1 = QLabel(ventana)
    label1.setText("Predice la supervivencia de un pasajero en el Titanic")
    label1.setStyleSheet("font-size:15px; font-weight:bold;")
    label1.adjustSize()
    label1.move(30,5)
    
    label2 = QLabel(ventana)
    label2.setText("Indique los siguientes datos")
    label2.setStyleSheet("font-size:13px; font-weight:bold;")
    label2.adjustSize()
    label2.move(15,45)

    labelClasePasajero = QLabel(ventana)
    labelClasePasajero.setText("Clase de pasajero:")
    labelClasePasajero.adjustSize()
    labelClasePasajero.move(10,80)
    
    labelSexo = QLabel(ventana)
    labelSexo.setText("Sexo:")
    labelSexo.adjustSize()
    labelSexo.move(15,110)
    
    labelEdad = QLabel(ventana)
    labelEdad.setText("Edad:")
    
    labelEdad.adjustSize()
    labelEdad.move(15,140)
    
    labelSibSp = QLabel(ventana)
    labelSibSp.setText("Número de hermanos/cónyuges a bordo:")
    labelSibSp.adjustSize()
    labelSibSp.move(10,170)
    
    labelParch = QLabel(ventana)
    labelParch.setText("Número de padres/hijos a bordo:")
    labelParch.adjustSize()
    labelParch.move(15,200)
    
    labelFare = QLabel(ventana)
    labelFare.setText("Tarifa de pasajero:")
    labelFare.adjustSize()
    labelFare.move(15,230)
    
    labelEmbarked = QLabel(ventana)
    labelEmbarked.setText("Puerto de embarque:")
    labelEmbarked.adjustSize()
    labelEmbarked.move(15,260)
    
    labelAlgoritmo = QLabel(ventana)
    labelAlgoritmo.setText("Elige el algoritmo de predicción:")
    labelAlgoritmo.adjustSize()
    labelAlgoritmo.move(15,300)
    
    
    ## INPUTS ##
    clasePasajerosInput = QComboBox(ventana)
    clasePasajerosInput.setGeometry(282, 77, 120, 22)
    clasePasajerosInput.addItems(["1","2","3"])
    
    sexoInput = QComboBox(ventana)
    sexoInput.setGeometry(282, 107, 120, 22)
    sexosList = ["Masculino", "Femenino"]
    sexoInput.addItems(sexosList)
    
    edadInput = QLineEdit(ventana)
    edadInput.setValidator(QIntValidator(0,150))
    edadInput.move(282,137)
    
    sibSpInput = QLineEdit(ventana)
    sibSpInput.setValidator(QIntValidator(0,15))
    sibSpInput.move(282,167)
    
    parchInput = QLineEdit(ventana)
    parchInput.setValidator(QIntValidator(0,15))
    parchInput.move(282,197)
    
    fareInput = QLineEdit(ventana)
    fareInput.setValidator(QDoubleValidator(0.99,99.99,2))
    fareInput.move(282,227)
    
    embarkedInput = QComboBox(ventana)
    embarkedInput.setGeometry(282, 259, 120, 22)
    puertosList = ["Cherbourg", "Queenstown", "Southampton"]
    embarkedInput.addItems(puertosList)

    algoritmoInput = QComboBox(ventana)
    algoritmoInput.setGeometry(282, 297, 190, 22)
    algoritmosList = ["Logistic Regression", 
                      "Support Vector Machines", 
                      "K Neighbors Classifier"]
    algoritmoInput.addItems(algoritmosList)


    ## BUTTON ##
    predecirButton = QPushButton(ventana)
    predecirButton.setText("Predecir")
    predecirButton.clicked.connect(predecirSupervivenciaTitanic)
    predecirButton.move(350,350)

    
    estilos = '''
        QPushButton {
            background-color:#8F7855;
            color:white;
            font-weight: bold;
            border-width: 5px;
            border-style:solid;
            border-color:black;
            border-radius:5;
            padding:2px;
        }
        QMainWindow {
            background-color: #EE9A1A;
            }
    '''

    QApplication.instance().setStyleSheet(estilos)

ventana.show()
sys.exit(app.exec_())