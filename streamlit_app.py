import streamlit as st
import pandas as pd
import numpy as np

# Título y descripción
st.title("Demo Streamlit")
st.write("Esta es una aplicación de ejemplo con formulario y gráfico.")

# Formulario de datos
st.header("Formulario")
nombre = st.text_input("Tu nombre:")
numero = st.number_input("Número de datos a generar", min_value=5, max_value=100, value=20)

# Botón para generar datos
if st.button("Generar gráfico"):
    st.subheader(f"Hola {nombre if nombre else 'Usuario'} 👋")
    st.write("Aquí tienes un gráfico con datos aleatorios:")

    # Crear DataFrame aleatorio
    df = pd.DataFrame(
        np.random.randn(numero, 2),
        columns=['Columna A', 'Columna B']
    )

    # Mostrar tabla y gráfico
    st.dataframe(df)
    st.line_chart(df)

st.info("Puedes cambiar el número de datos y volver a generar el gráfico.")
