import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("🚀 Physics Data Lab")

st.write("Interactive sine wave visualization")

# Slider interactivo
frequency = st.slider("Frequency", 1, 10, 2)

# Datos
x = np.linspace(0, 10, 500)
y = np.sin(frequency * x)

# Crear gráfico
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=x,
        y=y,
        mode="lines",
        name="Sine Wave"
    )
)

fig.update_layout(
    title="Interactive Physics Graph",
    xaxis_title="X Axis",
    yaxis_title="Y Axis"
)

# Mostrar gráfico
st.plotly_chart(fig)