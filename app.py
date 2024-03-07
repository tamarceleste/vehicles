import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv(r'C:\Users\tamar\OneDrive\Documentos\Data_Science\Sprint 5\vehicles\vehicles_us.csv') # leer los datos
car_data["marca"]=car_data["model"].apply(lambda x:x.split()[0])
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el precio promedio de cada marca de auto')
            
    # crear un histograma
  
    fig = px.histogram(car_data, x="model", y="price", histfunc='avg')
    fig.show()
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

prices=car_data.pivot_table(index="marca", columns="model",values="price", aggfunc="mean")
scatt_button = st.button("Construir diagrama")

if scatt_button: 
    st.write("Creación de un diagrama para el promedio de precios según modelo")
    
    fig2=px.scatter(prices,title="Promedio de precios por modelo</b><br><sup>Autos enlistados</sup>")
    fig2.update_xaxes(title_text="")
    fig2.update_yaxes(title_text="")
    fig2.update_layout(showlegend=False)
    fig2.show()
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)