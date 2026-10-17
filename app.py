"""Panel interactivo de anuncios de vehículos usados."""

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


DATA_PATH = Path(__file__).with_name("vehicles_us.csv")


@st.cache_data
def load_data():
    """Lee los anuncios y convierte columnas numéricas para los gráficos."""
    data = pd.read_csv(DATA_PATH)
    for column in ("price", "odometer", "model_year"):
        data[column] = pd.to_numeric(data[column], errors="coerce")
    return data


st.set_page_config(page_title="Vehículos usados", layout="wide")
st.header("Anuncios de vehículos usados")
st.write("Explora los precios y el kilometraje de los vehículos publicados.")

cars = load_data()
st.caption(f"{len(cars):,} anuncios en el conjunto de datos")

show_histogram = st.checkbox("Mostrar histograma del kilometraje", value=True)
show_scatter = st.checkbox("Mostrar relación entre kilometraje y precio", value=True)

if show_histogram:
    valid_odometer = cars.dropna(subset=["odometer"])
    histogram = px.histogram(
        valid_odometer,
        x="odometer",
        nbins=50,
        title="Distribución del kilometraje",
        labels={"odometer": "Kilometraje"},
    )
    st.plotly_chart(histogram, width="stretch")

if show_scatter:
    valid_pairs = cars.dropna(subset=["odometer", "price"])
    valid_pairs = valid_pairs[(valid_pairs["odometer"] >= 0) & (valid_pairs["price"] > 0)]
    scatter = px.scatter(
        valid_pairs,
        x="odometer",
        y="price",
        render_mode="svg",
        opacity=0.35,
        hover_data=["model", "condition"],
        title="Precio frente a kilometraje",
        labels={"odometer": "Kilometraje", "price": "Precio (USD)"},
    )
    st.plotly_chart(scatter, width="stretch")
