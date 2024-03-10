import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header(" Bienvenidos a mi primera aplicación web")#primer título
st.title("¡Vamos a crear algunos gráficos!")#título principal

st.markdown("En base a la siguiente lista de automóviles a la venta:")
st.write(car_data)#muestra la lista de datos

hist_button = st.button('Construir histograma') # crear un botón
show_hist = st.checkbox("Mostrar histograma")#crear una casilla
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma de distribución para el año de modelo de automóviles')
    if show_hist:#al seleccionar la casilla
        # crear un histograma
        fig = px.histogram(car_data, x="model_year",color="fuel",title="Distribución de año de modelos enlistados</b><br><sup>Según tipo de combustible</sup>")
        fig.update_xaxes(title_text="Año del modelo")
        fig.update_yaxes(title_text="Cantidad de autos")        
        fig.show() 
        # se muestra un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)

scatt_button = st.button("Construir gráfico de dispersión")
show_scatt = st.checkbox("Mostrar gráfico")#crear una segunda casilla

if scatt_button: #al hacer click en el botón
    st.write("Creación de gráfico de dispersión para el precio promedio de acuerdo a su año")#Se escribe el mensaje
    
    if show_scatt:#al seleccionar la casilla
        #crear un gráfico de dispersión
        mean_price= car_data.pivot_table(index="model_year", columns="transmission", values="price",aggfunc="mean")
        fig2=px.scatter(mean_price,
                    title="Precio promedio v/s año del modelo</b><br><sup>Según tipo de transmisión</sup>")
        fig2.update_xaxes(title_text="Año del modelo")
        fig2.update_yaxes(title_text="Precio promedio (dólares)")
        fig2.show()
        # se muestra un gráfico Plotly interactivo
        st.plotly_chart(fig2, use_container_width=True)
