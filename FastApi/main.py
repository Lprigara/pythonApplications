from predicciones import predecirIris
import json
import csv
from fastapi import FastAPI, status
import pandas as pd
from models import Iris, IrisPredictable



app = FastAPI()

MEDIA_ROOT = "iris.csv"

@app.get("/test")
async def test_1():
    return "Bienvenido a FastAPI"


@app.get("/iris/")
async def iris():
    df = pd.read_csv(MEDIA_ROOT)
    data = df.to_json(orient="index")
    data = json.loads(data)
    return data


@app.post("/insertData/", status_code=201)
async def insertData(item:Iris):
    with open(MEDIA_ROOT, 'a', newline="") as csvFile:
        fieldnames=['sepal_length', 'sepal_width',
                    'petal_length', 'petal_width',
                    'species']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writerow({'sepal_length':item.sepal_length,
                         'sepal_width':item.sepal_width,
                         'petal_length':item.petal_length,
                         'petal_width':item.petal_width,
                         'species':item.species})
        
        return {**item.dict(), "msg":"Resource inserted successfully"}
    
    
@app.put("/updateData/{item_id}", status_code=200)
async def updateData(item_id:int, item:Iris):
    df = pd.read_csv(MEDIA_ROOT)
    df.loc[df.index[item_id-2], "sepal_length"] = item.sepal_length
    df.loc[df.index[item_id-2], "sepal_width"] = item.sepal_width
    df.loc[df.index[item_id-2], "petal_length"] = item.petal_length
    df.loc[df.index[item_id-2], "petal_width"] = item.petal_width
    df.loc[df.index[item_id-2], "species"] = item.species
    df.to_csv(MEDIA_ROOT, index=False)
    return {"item_id":item_id, **item.dict(), "msg":"Resource updated successfully"}


@app.delete("/deleteData/{item_id}", status_code=200)
async def deleteData(item_id:int):
    df = pd.read_csv(MEDIA_ROOT)
    df.drop(df.index[item_id-2], inplace=True)
    df.to_csv(MEDIA_ROOT, index=False)
    return {"item_id":item_id, "msg":"Resource deleted successfully."}


@app.post('/decisionTreeClassifier/', status_code=200)
async def decisionTreeClassifier(item:IrisPredictable):
    algoritmo = "dtc"
    datosIris = {"sepal_length":[item.sepal_length],
                     "sepal_width":[item.sepal_width],
                     "petal_length":[item.petal_length],
                     "petal_width":[item.petal_width]}
        
    especiePredecida = predecirIris(algoritmo, datosIris)

    return {"La especie predecida es:":especiePredecida, **datosIris}


@app.post('/randomForestClassifier/', status_code=200)
async def randomForestClassifier(item:IrisPredictable):
    algoritmo = "rfc"
    datosIris = {"sepal_length":[item.sepal_length],
                     "sepal_width":[item.sepal_width],
                     "petal_length":[item.petal_length],
                     "petal_width":[item.petal_width]}
        
    especiePredecida = predecirIris(algoritmo, datosIris)

    return {"La especie predecida es:":especiePredecida, **datosIris}