import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv(r'C:\Users\tamar\OneDrive\Documentos\Data_Science\Sprint 5\vehicles\vehicles_us.csv') # leer los datos
car_data["marca"]=car_data["model"].apply(lambda x:x.split()[0])
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para la distribución de año del modelo')
            
    # crear un histograma
  
    fig = px.histogram(car_data, x="model_year",color="fuel",title="Distribución de año de modelos enlistados</b><br><sup>Según tipo de combustible</sup>")
    fig.update_xaxes(title_text="Año del modelo")
    fig.update_yaxes(title_text="Cantidad de autos")
    fig.show()
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatt_button = st.button("Construir diagrama de dispersión")

if scatt_button: 
    st.write("Creación de un diagrama para el promedio de precios según modelo")
    mean_price= car_data.pivot_table(index="model_year", columns="transmission", values="price",aggfunc="mean")
    fig2=px.scatter(mean_price,
                    title="Precio promedio v/s año del modelo según transmisión</b><br><sup>Autos enlistados</sup>")
    fig2.update_xaxes(title_text="")
    fig2.update_yaxes(title_text="")
    fig2.show()
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)