# Sprint 7: panel de anuncios de vehículos

Aplicación web que explora anuncios de venta de vehículos usados. Incluye un histograma del kilometraje y un gráfico de dispersión que compara kilometraje y precio. Cada gráfico se activa con una casilla de verificación.

## Estructura

- `app.py`: aplicación Streamlit.
- `vehicles_us.csv`: datos de anuncios proporcionados para el proyecto.
- `notebooks/EDA.ipynb`: exploración breve de datos y gráficos con Plotly.
- `requirements.txt`: dependencias de Python.

## Ejecutar localmente

1. Crea y activa un entorno virtual de Python.
2. Instala dependencias con `pip install -r requirements.txt`.
3. Ejecuta `streamlit run app.py` desde esta carpeta.

## Despliegue en Render

Aplicación desplegada: https://sprint-7-panel-vehiculos.onrender.com/

El servicio gratuito usa `pip install --upgrade pip && pip install -r requirements.txt` como **Build Command** y `streamlit run app.py --server.address 0.0.0.0 --server.port $PORT` como **Start Command**. Puede tardar en despertar tras un periodo de inactividad.

## Datos

Fuente: conjunto `vehicles_us.csv` facilitado en Sprint 7 de TripleTen. Los datos contienen anuncios de vehículos de Estados Unidos; son descriptivos y no representan el mercado actual.
