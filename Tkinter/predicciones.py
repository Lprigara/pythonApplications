import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

def logisticRegressionAlgorithm(x_train, y_train, x_test):
    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)
    y_pred = logreg.predict(x_test)
    return y_pred

    
def supportVectorMachinesAlgorithm(x_train, y_train, x_test):
    svc = SVC()
    svc.fit(x_train, y_train)
    y_pred = svc.predict(x_test)
    return y_pred


def kneighborsClassifierAlgorithm(x_train, y_train, x_test):
    knc = KNeighborsClassifier(n_neighbors = 3)
    knc.fit(x_train, y_train)
    y_pred = knc.predict(x_test)
    return y_pred
    
    
def predecir(algoritmo, datosRecogidos):
    df_train = pd.read_csv('train.csv')

    #Se elimina la columna Cabin porque tiene muchos datos nulos
    df_train = df_train.drop(columns='Cabin', axis=1)

    #Reemplazo los datos faltantes en la edad por la media de esta columna
    #print(df_train["Age"].mean())
    promedio = 30
    df_train['Age'].fillna(promedio, inplace=True)

    #Como embarked tiene dos datos nulos, los cambiamos por el dato que más se repite (moda)
    moda = df_train['Embarked'].mode()[0]
    df_train['Embarked'].fillna(moda, inplace=True)

    #Cambio los datos de sexos y embarque en números
    df_train.replace({'Sex':{'male':0,'female':1}, 
                      'Embarked':{'S':0,'C':1,'Q':2}}, 
                     inplace=True)

    #X se queda con las columnas [Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]
    #Y se queda con [Survived]
    X= df_train.drop(columns = ['PassengerId','Name','Ticket','Survived'],axis=1)
    Y = df_train['Survived']

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, 
                                                        test_size=0.2, 
                                                        random_state=2)
    
    y_pred = ""
    
    if algoritmo == 0:
        y_pred = logisticRegressionAlgorithm(X_train, Y_train, datosRecogidos)
        print("lr")
    elif algoritmo == 1:
        y_pred = supportVectorMachinesAlgorithm(X_train, Y_train, datosRecogidos)
        print("svc")
    elif algoritmo == 2:
        y_pred = kneighborsClassifierAlgorithm(X_train, Y_train, datosRecogidos)
        print("kn")
       
    return y_pred[0]