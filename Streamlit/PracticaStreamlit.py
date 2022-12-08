
###################################
### Autor: Leonor Priego García ###
###################################

import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

st.title("Gráfica de Steamlit para finanzas")

st.sidebar.subheader("Filtra por los datos que quieras consultar")

empresas = ["GOOGL", "AAPL", "MSFT", 
            "TSLA", "NFLX"]
empresas = list(empresas)
filtroEmpresas = st.sidebar.multiselect(
    "Empresas: ", options=empresas, default=empresas)


rangoAños = st.sidebar.slider(
    "Rango de años: ", 2015, 2018, (2016,2017))

st.sidebar.write("Rango de años: ", rangoAños)

fechaInicio = rangoAños[0]
fechaFin = rangoAños[1]


### TABLA COMBINADA
st.subheader("Tabla que combina los datos de todas las empresas")
df=pd.DataFrame(columns=['Open', 'High', 'Low', 
                         'Close', 'Adj Close', 
                         'Volume', 'Empresa'])

for empresa in filtroEmpresas:
    df1 = yf.download(empresa, f"{fechaInicio}-1-1", f"{fechaFin}-12-31")
    df1['Empresa'] = str(empresa)
    df = pd.concat([df, df1])
    totals = df.groupby("Empresa", as_index=False)['Volume'].sum()
    

st.write(df)

### VOLUMEN TOTAL
st.subheader("Total del Volumen de cada empresa")

for i in filtroEmpresas:
     st.write(i, " - ",
              f'{totals[totals["Empresa"]==i]["Volume"].values[0]:,}', "$")
    

fig = px.bar(
        totals,
        y="Empresa",
        x="Volume",
        color="Empresa",
        color_discrete_sequence=px.colors.sequential.Reds,
    )
fig.update_layout(barmode="stack", xaxis={"categoryorder": "total descending"})
st.plotly_chart(fig, use_container_width=True)


### Gráfico circular
st.subheader("Value of each Symbol")

fig1 = px.pie(
            totals, 
            values="Volume", 
            names="Empresa", 
            color="Empresa", 
            color_discrete_sequence=px.colors.sequential.Reds
        )
fig1.update_layout(margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig1, use_container_width=True)