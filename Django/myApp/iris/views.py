import imp
from pydoc import describe
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, redirect
from django.conf import settings
import pandas as pd
import csv
import json
from myApp.serializer import irisSerializer
from rest_framework.response import Response


@api_view(['GET'])
def irisData(request):
    if request.method == 'GET':
        irisFile = settings.MEDIA_ROOT + '/iris.csv'
        df = pd.read_csv(irisFile)
        data = df.to_json(orient="index")
        data = json.loads(data)
        describe = df.describe().to_json(orient="index")
        describe = json.loads(describe)
        return render(request, "iris/main.html", 
                      context={"data":data, "describe":describe},
                      status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def insertData(request):
    result=''
    if request.method == 'GET':
        return render(request, "iris/insert.html")
    elif request.method == 'POST':
        data = request.data
        print(data)
        serializer = irisSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            irisFile = settings.MEDIA_ROOT + '/iris.csv'
            with open(irisFile, "a", newline="") as csvFile:
                fieldnames = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
                writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
                writer.writerow({"sepal_length":data["sepal_length"],
                                 "sepal_width":data["sepal_width"],
                                 "petal_length":data["petal_length"],
                                 "petal_width":data["petal_width"],
                                 "species":data["species"]
                                 })
            result='Inserción completada'
            return render(request, 'iris/insert.html', context={"result":result}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                
                 
@api_view(['GET', 'PUT', 'POST'])
def updateData(request):
    if request.method == 'GET':
        irisFile = settings.MEDIA_ROOT + '/iris.csv'
        df = pd.read_csv(irisFile)
        lastData = df.iloc[-1] 
        sepal_width = str(lastData["sepal_width"])
        sepal_length = str(lastData["sepal_length"])
        petal_length = str(lastData["petal_length"])
        petal_width = str(lastData["petal_width"])
        species = str(lastData["species"])
        return render(request, 'iris/update.html', 
                      context={"sepal_length":sepal_length, 
                               "sepal_width":sepal_width, 
                               "petal_length":petal_length, 
                               "petal_width":petal_width, 
                               "species":species})

    # Lo probamos usando POSTMAN:
    elif request.method == 'PUT':
        data = request.data
        irisFile = settings.MEDIA_ROOT + '/iris.csv'
        df = pd.read_csv(irisFile)
        serializer = irisSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            df.loc[df.index[-1], "sepal_length"] = serializer.data["sepal_length"]
            df.loc[df.index[-1], "sepal_width"] = serializer.data["sepal_width"]
            df.loc[df.index[-1], "petal_length"] = serializer.data["petal_length"]
            df.loc[df.index[-1], "petal_width"] = serializer.data["petal_width"]
            df.loc[df.index[-1], "species"] = serializer.data["species"]
            df.to_csv(irisFile, index=False)
            return Response(df.iloc[-1], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Lo mismo que el método PUT pero a través del front-end:
    elif request.method == 'POST':
        data = request.data
        irisFile = settings.MEDIA_ROOT + '/iris.csv'
        df = pd.read_csv(irisFile)
        serializer = irisSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            df.loc[df.index[-1], "sepal_length"] = serializer.data["sepal_length"]
            df.loc[df.index[-1], "sepal_width"] = serializer.data["sepal_width"]
            df.loc[df.index[-1], "petal_length"] = serializer.data["petal_length"]
            df.loc[df.index[-1], "petal_width"] = serializer.data["petal_width"]
            df.loc[df.index[-1], "species"] = serializer.data["species"]
            df.to_csv(irisFile, index=False)
            return redirect('/iris/')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'POST'])
def deleteData(request):
    if request.method == 'GET':
        # TODO: mostrar el último dato del dataset en la plantilla delete.html
        pass
    # Lo probamos usando POSTMAN:
    elif request.method == 'DELETE':
        # TODO: eliminar el último dato del csv
        pass
    # Lo mismo que el método DELETE pero a través del front-end:
    elif request.method == 'POST':
        # TODO: eliminar el último dato del csv
        pass
