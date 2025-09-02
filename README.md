# 🏠 Carpio Machine Learning - Predicción de Precio de Casas en El Salvador

Aplicación en **Streamlit** que utiliza un modelo de **Machine Learning** previamente entrenado para predecir el precio de una casa en función de sus características principales.  

---

## 🚀 Características

- Interfaz sencilla en **Streamlit**.  
- El usuario ingresa:
  - **Tamaño de la casa** (m²).  
  - **Número de habitaciones**.  
  - **Edad de la casa** (años).  
- El modelo estima el **precio en dólares** y lo muestra en pantalla.  

---

## 🛠️ Tecnologías utilizadas

- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – Interfaz web interactiva  
- [NumPy](https://numpy.org/) – Manipulación de arrays  
- [Pickle](https://docs.python.org/3/library/pickle.html) – Carga del modelo entrenado  

---

## 📂 Requisitos previos

1. Archivo del modelo entrenado:  
   **`modelo_precio_casas.pkl`**  
   Debe estar en el mismo directorio que el archivo principal (`app.py`).  

   > Este archivo contiene el modelo de Machine Learning previamente entrenado con datos históricos de precios de casas.  

2. Dependencias de Python instaladas:  

   ```bash
   pip install streamlit numpy scikit-learn
