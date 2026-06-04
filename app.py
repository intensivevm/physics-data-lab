import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Configuración de página
st.set_page_config(
    page_title="Physics Data Lab",
    page_icon="🚀",
    layout="wide"
)

# Título
st.title("🚀 Physics Data Lab")
st.subheader("Interactive Wave Simulation")

# Sidebar
st.sidebar.header("Wave Controls")

# Selector de función
wave_type = st.sidebar.selectbox(
    "Select Wave Type",
    ["Sine", "Cosine", "Tangent"]
)

# Sliders
amplitude = st.sidebar.slider("Amplitude", 1, 10, 1)
frequency = st.sidebar.slider("Frequency", 1, 10, 2)
phase = st.sidebar.slider("Phase", 0, 10, 0)

# Datos
x = np.linspace(0, 10, 1000)

# Elegir función
if wave_type == "Sine":
    y = amplitude * np.sin(frequency * x + phase)

elif wave_type == "Cosine":
    y = amplitude * np.cos(frequency * x + phase)

else:
    y = amplitude * np.tan(frequency * x + phase)

# Crear gráfico
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=x,
        y=y,
        mode="lines",
        name=wave_type,
    )
)

# Layout gráfico
fig.update_layout(
    title=f"{wave_type} Wave",
    template="plotly_dark",
    xaxis_title="X Axis",
    yaxis_title="Y Axis",
    height=600
)

# Mostrar gráfico
st.plotly_chart(fig, use_container_width=True)

# Fórmula
st.markdown("## Mathematical Representation")

if wave_type == "Sine":
    st.latex(r"y = A \sin(fx + p)")

elif wave_type == "Cosine":
    st.latex(r"y = A \cos(fx + p)")

else:
    st.latex(r"y = A \tan(fx + p)")

# Métricas
col1, col2, col3 = st.columns(3)

col1.metric("Amplitude", amplitude)
col2.metric("Frequency", frequency)
col3.metric("Phase", phase)