import streamlit as st
import pandas as pd
import pickle
import mlflow.pyfunc
import support_clean as sc

# Configurar la página de Streamlit
st.set_page_config(
    page_title="Predicción de Precios de Alquiler en Madrid",
    page_icon="🏠",
    layout="centered",
)

# Título y descripción
st.title("🏠 Predicción de Precios de Alquiler en Madrid")
st.write("Introduce los datos de una casa para conocer su precio aproximado de alquiler en la provincia de Madrid")

# Mostrar una imagen llamativa
st.image(
    "../assets/portada-isabel-diaz-ayuso.jpg",  # URL de la imagen
    caption="Avalado por Ayuso.",
    use_column_width=True,
)

# Cargar el modelo
local_mlflow_model_path = "../model_tracking/327450721189704106/2dfdd21c3fff4f458d5123148cdd800e/artifacts/model/model.pkl"
loaded_pipeline = mlflow.pyfunc.load_model(local_mlflow_model_path)


# Formularios de entrada
st.header("🔧 Características de la casa")
col1, col2 = st.columns(2)


# [["size","distance","bathrooms","exterior","parkingSpace_included_in_listing",
#              "rooms", "floor_grouped", "p_area_property_grouped",
#              "hasPlan"]]

with col1:
    size = st.number_input("Área en m²", min_value=50, max_value=500, value=60, step=1)
    rooms = st.number_input("Número de Habitaciones", min_value=1, max_value=10, value=1, step=1)
    floor = st.number_input("Nº de planta", min_value=0, max_value=10, value=3, step=1)
    exterior = st.selectbox("Si/No", ["Si", "No"], help="¿Es exterior?")
    hasPlan = st.selectbox("Si/No", ["Si", "No"], help="¿Tiene plan?")


with col2:
    distance = st.number_input("Distancia con Km.0 en m", min_value=0, max_value=10000, value=1000, step=1)
    bathrooms = st.number_input("Número de Cuartos de Baño", min_value=1, max_value=5, value=1, step=1)
    property_type = st.selectbox("Barrio", ["Flat", "Studio", "Penthouse", "Duplex"], help="Selecciona el tipo de casa.")
    parking_included = st.selectbox("Si/No", ["Si", "No"], help="¿Tiene parking incluido?")

# Botón para realizar la predicción
if st.button("💡 Predecir Precio"):
    # Crear DataFrame con los datos ingresados
    new_house = pd.DataFrame({
        'size': [size],
        'distance': [distance],
        'bathrooms': [bathrooms],
        'exterior': [exterior],
        "parkingSpace_included_in_listing": [parking_included],
        "rooms": [rooms], 
        "floor_grouped": [floor], 
        "p_area_property_grouped": [property_type],
        "hasPlan": [hasPlan]
    })

    new_house = sc.clean_new_house(new_house)

    prediction = loaded_pipeline.predict(new_house)

    # Mostrar el resultado
    st.success(f"💵 El precio estimado de la casa es: ${prediction}")
    st.balloons()

# Pie de página
st.markdown(
    """
    ---
    **Proyecto creado con el potencial de la ciencia de datos.**  
    Desarrollado con ❤️ usando Streamlit.
    """,
    unsafe_allow_html=True,
)