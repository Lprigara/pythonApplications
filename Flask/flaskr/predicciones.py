import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

import sys

def decisionTreeClassifierAlgorithm(x_train, y_train, x_test):
    clf = DecisionTreeClassifier()
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    return y_pred

    
def randomForestClassifierAlgorithm(x_train, y_train, x_test):
    clf = RandomForestClassifier()
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    return y_pred
    
    
def predecirIris(algoritmo, datosRecogidos):
    df = pd.read_csv("iris.csv")

    x = df.drop(["species"], axis=1)  #axis=1 = para que borre la columna

    y = df["species"]
    
    nuevoDf = pd.DataFrame(datosRecogidos)
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
    y_pred = ""
    
    if algoritmo == 'dtc':
        y_pred = decisionTreeClassifierAlgorithm(x_train, y_train, nuevoDf)
    elif algoritmo == 'rfc':
        y_pred = randomForestClassifierAlgorithm(x_train, y_train, nuevoDf)
    
    print(y_test)
    
    return y_pred[0]