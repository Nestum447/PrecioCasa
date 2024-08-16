import streamlit as st
import pickle
import numpy as np  

# Cargar el modelo entrenado
with open('modelo_precio_casas.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Predicción de Precio de Casas NO DEJES QUE TIMEN ')

# Entradas de usuario
tamaño = st.number_input('Tamaño de la casa (en metros cuadrados):', min_value=500, max_value=10000, value=1500)
habitaciones = st.number_input('Número de habitaciones:', min_value=1, max_value=10, value=3)
edad = st.number_input('Edad de la casa (en años):', min_value=0, max_value=100, value=10)

# Hacer la predicción cuando se presione el botón
if st.button('Predecir Precio'):
    datos_nueva_casa = np.array([[tamaño, habitaciones, edad]])
    prediccion_precio = model.predict(datos_nueva_casa)
    st.write(f'El precio estimado de la casa es: ${prediccion_precio[0]:,.2f}')
