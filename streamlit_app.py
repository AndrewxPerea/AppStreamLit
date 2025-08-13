import streamlit as st
import pandas as pd
import plotly.express as px

# Título
st.title("📊 Análisis de Archivos con Streamlit")
st.write("Sube un archivo Excel o CSV para visualizar y analizar los datos.")

# Cargar archivo
archivo = st.file_uploader("Sube tu archivo", type=["xlsx", "xls", "csv"])

if archivo is not None:
    # Leer archivo según tipo
    try:
        if archivo.name.endswith(".csv"):
            df = pd.read_csv(archivo)
        else:
            df = pd.read_excel(archivo)

        st.success("✅ Archivo cargado correctamente.")

        # Mostrar vista previa
        st.subheader("Vista previa de datos")
        st.dataframe(df)

        # Seleccionar columna para gráfico
        columnas_numericas = df.select_dtypes(include=["number"]).columns.tolist()

        if columnas_numericas:
            col_x = st.selectbox("Selecciona la columna X (categoría)", df.columns)
            col_y = st.selectbox("Selecciona la columna Y (valor numérico)", columnas_numericas)

            # Gráfico interactivo
            fig = px.bar(df, x=col_x, y=col_y, title="Gráfico interactivo")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("⚠ No se encontraron columnas numéricas para graficar.")

    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")
else:
    st.info("📂 Esperando que subas un archivo...")
