###################################
### AUTOR: LEONOR PRIEGO GARCÍA ###
###################################

import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv('datosTitanic.csv')

figura = px.scatter(df, x="Age", y="Sex", color="Survived")


dfSurvived = df['Survived'].replace([0,1],["Fallece","Sobrevive"])
figura1 = px.pie(dfSurvived, 
                 names='Survived', 
                 title='Gráfico circular que indica el porcentaje de supervivientes y fallecidos.',
                 hole=0.3)


figura2 = px.strip(df, 
                   x=df['Sex'].replace(["male","female"],["Hombres","Mujeres"]), 
                   y="Age", 
                   color=df['Survived'].replace([0,1],["Fallece","Sobrevive"]),
                   title="Gráfico de dispersión que indica en función de la edad y el sexo de las personas que sobreviven o fallecen.", 
                   stripmode="overlay")


figura3 = px.histogram(df,
                      x = "Age",
                      color = df['Survived'].replace([0,1],["Fallece","Sobrevive"]),
                      title="Gráfico de barras que indica las personas que sobreviven o fallecen en función de la edad.")


figura4 = px.scatter_3d(df, 
                        x='Pclass', 
                        y='Fare', 
                        z='Age',
                        color=df['Survived'].replace([0,1],["Fallece","Sobrevive"]), 
                        title="Gráfico de dispersión en 3D que indica las personas que sobreviven o fallecen en función de la clase y la tarifa de pasajero.")




app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children="Supervivencia en el accidente del Titanic.", 
            style={'text-align': 'center', 'margin':'3% 0'}), 
    dcc.Graph(figure=figura1),
    html.P("Sobrevive cerca de un tercio de los pasajeros.", 
           style={'padding-left': '5%', 'font-weight': 'bold'}),
    html.Hr(),
    dcc.Graph(figure=figura2),
    html.P("Es curioso observar que sobreviven más mujeres que hombres.", 
           style={'padding-left': '5%', 'font-weight': 'bold'}),
    html.Hr(),
    dcc.Graph(figure=figura3),    
    html.P("Es curioso observar que sobreviven muchos más niños pequeños \
        de los que mueren.", 
           style={'padding-left': '5%', 'font-weight': 'bold'}),
    html.Hr(),
    dcc.Graph(figure=figura4),    
    html.P("Es curioso observar que cuanta más alta era la clase y la tarifa, \
        más número de supervivientes hay.", 
           style={'padding-left': '5%', 'font-weight': 'bold'})
],style={'margin-left':'2%'})


if __name__ == "__main__":
    app.run_server(debug=True)