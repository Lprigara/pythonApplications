
###################################
### Autor: Leonor Priego García ###
###################################

from turtle import width
import numpy as np
import pandas as pd
from predicciones import predecir
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk


ventana = tk.Tk()
ventana.title("Predice la supervivencia de un pasajero en el Titanic")
ventana.geometry("700x500")
ventana.resizable(0,0)
ventana.config(bg='#EE9A1A')


def obtenerDatosEntrada():
    algoritmo = comboAlgoritmo.current()
    clase = int(clasePasajerosInput.get())
    sexo = sexoInput.current()
    edad = int(edadInput.get())
    sibSp = int(sibSpInput.get())
    parch = int(parchInput.get())
    fare = float(fareInput.get().replace(',','.'))
    embarked = embarkedInput.current()
    return (clase,sexo,edad,sibSp,parch,fare,embarked), algoritmo
    
    
def predecirSupervivenciaTitanic():
    input_data, algoritmo = obtenerDatosEntrada()
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    sobrevive = predecir(algoritmo, input_data_reshaped)
    if sobrevive==0:
        messagebox.showinfo(message="El pasajero indicado muere", title="Supervivencia Titanic")
    if sobrevive==1:
        messagebox.showinfo(message="El pasajero indicado sobrevive", title="Supervivencia Titanic")


### ETIQUETAS LABEL ###
tk.Label(ventana, text="Predice la supervivencia de un pasajero en el Titanic", 
         font='Helvetica 18 bold').place(x=30, y=5)
tk.Label(ventana, text="Indique los siguientes datos", 
         font='Helvetica 13 bold').place(x=10, y=45)
tk.Label(ventana, text="Clase de pasajeros:").place(x=10, y=80)
tk.Label(ventana, text="Sexo:").place(x=10, y=110)
tk.Label(ventana, text="Edad:").place(x=10, y=140)
tk.Label(ventana, text="Número de hermanos/cónyuges a bordo:").place(x=10, y=170)
tk.Label(ventana, text="Número de padres/hijos a bordo:").place(x=10, y=200)
tk.Label(ventana, text="Tarifa de pasajero:").place(x=10, y=230)
tk.Label(ventana, text="Puerto de embarque:").place(x=10, y=260)


### INPUTS ###
clasePasajerosInput = ttk.Combobox(values=[1,2,3])
clasePasajerosInput.place(x=290, y=80)
sexoInput = ttk.Combobox(values=["Masculino", 
                                 "Femenino"])
sexoInput.place(x=290, y=110)
edadInput = tk.Entry(ventana)
edadInput.place(x=290, y=140)
sibSpInput = tk.Entry(ventana)
sibSpInput.place(x=290, y=170)
parchInput = tk.Entry(ventana)
parchInput.place(x=290, y=200)
fareInput = tk.Entry(ventana)
fareInput.place(x=290, y=230)
embarkedInput = ttk.Combobox(values=["Cherbourg", 
                                     "Queenstown", 
                                     "Southampton"])
embarkedInput.place(x=290, y=260)


tk.Label(ventana, text="Elige el algoritmo de predicción:",
         font='Helvetica 13 bold').place(x=10,y=300)

comboAlgoritmo = ttk.Combobox(values=["Logistic Regression", 
                                      "Support Vector Machines", 
                                      "K Neighbors Classifier"],width=35)
comboAlgoritmo.place(x=300, y=300)

tk.Button(ventana, text="Predecir", fg="white", bg="#8F7855", 
          width=14, height=3,
          command=predecirSupervivenciaTitanic).place(x=250,y=330)

ventana.mainloop()