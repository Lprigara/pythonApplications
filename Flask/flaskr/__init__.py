#### Autor: Leonor Priego García

from crypt import methods
from email import message
from pydoc import describe
import re
from unittest import result
from flask import Flask, request, render_template
import pandas as pd
import json
import csv
import predicciones

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    df = pd.read_csv('iris.csv')
    describe = df.describe().to_json(orient='index')
    describe = json.loads(describe)
    data = df.to_json(orient="index")
    data = json.loads(data)
    return render_template('showIris.html', data=data, describe=describe)


@app.route('/decisionTreeClassifier/', methods=["GET","POST"])
def decisionTreeClassifier():
    algoritmo = "dtc"
    
    if request.method == 'GET':
        return render_template('prediccion.html', 
                               algoritmo=algoritmo, 
                               especie="")
    
    elif request.method == 'POST':
        data = request.form
        datosIris = {"sepal_length":[float(data["sepal_length"])],
                     "sepal_width":[float(data["sepal_width"])],
                     "petal_length":[float(data["petal_length"])],
                     "petal_width":[float(data["petal_width"])]}
        
        especiePredecida = predicciones.predecirIris(algoritmo,
                                                    datosIris)

        return render_template('prediccion.html', 
                                especie=especiePredecida, 
                                algoritmo=algoritmo,
                                datosIris=datosIris)


@app.route('/randomForestClassifier/', methods=["GET","POST"])
def randomForestClassifier():
    algoritmo = "rfc"
    if request.method == 'GET':
        return render_template('prediccion.html', 
                               algoritmo=algoritmo, 
                               especie="")
    
    elif request.method == 'POST':
        data = request.form
        datosIris = {"sepal_length":[float(data["sepal_length"])],
                     "sepal_width":[float(data["sepal_width"])],
                     "petal_length":[float(data["petal_length"])],
                     "petal_width":[float(data["petal_width"])]}
        
        especiePredecida = predicciones.predecirIris(algoritmo,
                                                    datosIris)

        return render_template('prediccion.html', 
                                especie=especiePredecida, 
                                algoritmo=algoritmo,
                                datosIris=datosIris)


@app.route('/insertData/', methods=["GET", "POST"])
def insertData():
    result = ""
    if request.method == 'GET':
        return render_template("insert.html")
    elif request.method == 'POST':
        data = request.form
       
        with open("iris.csv", "a", newline="") as csvfile:
            fieldnames= ["sepal_length", "sepal_width", 
                         "petal_length", "petal_width", 
                         "species"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"sepal_length":data["sepal_length"],
                              "sepal_width":data["sepal_width"],
                              "petal_length":data["petal_length"],
                              "petal_width":data["petal_width"],
                              "species":data["species"]})
            result='Success'
        return render_template('insert.html',result=result)

        
@app.route('/updateData/', methods=["GET","PUT","POST"])
def updateData():
    if request.method == 'GET':
        df = pd.read_csv('iris.csv')
        lastData = df.iloc[-1] 
        sepal_width = str(lastData["sepal_width"])
        sepal_length = str(lastData["sepal_length"])
        petal_length = str(lastData["petal_length"])
        petal_width = str(lastData["petal_width"])
        species = str(lastData["species"])
        
        return render_template('update.html', 
                               sepal_length=sepal_length, 
                               sepal_width=sepal_width, 
                               petal_length=petal_length, 
                               petal_width=petal_width, 
                               species=species) 
    
    elif request.method == 'PUT':
        data = request.data
        data = json.loads(data)
        df = pd.read_csv('iris.csv')
        df.loc[df.index[-1], "sepal_length"] = data["sepal_length"]
        df.loc[df.index[-1], "sepal_width"] = data["sepal_width"]
        df.loc[df.index[-1], "petal_length"] = data["petal_length"]
        df.loc[df.index[-1], "petal_width"] = data["petal_width"]
        df.loc[df.index[-1], "species"] = data["species"]
        df.to_csv("iris.csv", index=False)
        result = df.iloc[-1].to_json(orient='index')
        result = json.loads(result)
        return result
    
    elif request.method == 'POST':
        data = request.form
        df = pd.read_csv('iris.csv')
        df.loc[df.index[-1], "sepal_length"] = data["sepal_length"]
        df.loc[df.index[-1], "sepal_width"] = data["sepal_width"]
        df.loc[df.index[-1], "petal_length"] = data["petal_length"]
        df.loc[df.index[-1], "petal_width"] = data["petal_width"]
        df.loc[df.index[-1], "species"] = data["species"]
        df.to_csv("iris.csv", index=False)
        result = 'Success'
        return render_template('update.html',result=result)
    
    
    #     def updater(filename):
    # with open(filename, newline= "") as file:
    #     readData = [row for row in csv.DictReader(file)]
    #     # print(readData)
    #     readData[0]['Rating'] = '9.4'
    #     # print(readData)

    #readHeader = readData[0].keys()
    #writer(readHeader, readData, filename, "update")


@app.route('/deleteData/', methods=["GET","POST","DELETE"])
def deleteData():
    if request.method == 'GET':
        df = pd.read_csv('iris.csv')
        lastData = df.iloc[-1] 
        sepal_width = str(lastData["sepal_width"])
        sepal_length = str(lastData["sepal_length"])
        petal_length = str(lastData["petal_length"])
        petal_width = str(lastData["petal_width"])
        species = str(lastData["species"])
        
        return render_template('delete.html', 
                               sepal_length=sepal_length, 
                               sepal_width=sepal_width, 
                               petal_length=petal_length, 
                               petal_width=petal_width, 
                               species=species) 
        
    elif request.method == 'POST':
        data = request.form
        df = pd.read_csv('iris.csv')
        df.drop(df.index[-1], inplace=False)
        df.to_csv("iris.csv", index=False)
        result = df.iloc[-1].to_json(orient='index')
        result = json.loads(result)
        return render_template('delete.html', mensaje="Success")


if __name__ == "__main__":
    app.run(debug=True)