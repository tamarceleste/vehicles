import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv(r'C:\Users\tamar\OneDrive\Documentos\Data_Science\Sprint 5\vehicles\vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el precio promedio de cada marca de auto')
            
    # crear un histograma
  
    fig = px.histogram(car_data, x="marca", y="price", histfunc='avg')
    fig.show()
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
