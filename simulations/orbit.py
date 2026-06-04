import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time


def show_orbit():

    st.header("🪐 Orbit Simulation")

    st.write(
        "Animated orbital motion using parametric equations."
    )

    # Controles
    radius = st.slider("Orbit radius", 1.0, 10.0, 4.0)
    eccentricity = st.slider("Eccentricity", 0.0, 0.8, 0.2)

    # Ángulos
    theta = np.linspace(0, 2 * np.pi, 400)

    # Ecuación orbital
    r = radius * (1 - eccentricity**2) / (
        1 + eccentricity * np.cos(theta)
    )

    # Coordenadas órbita
    orbit_x = r * np.cos(theta)
    orbit_y = r * np.sin(theta)

    # Placeholder dinámico
    chart = st.empty()

    # Loop animación
    for i in range(len(theta)):

        # Posición actual del planeta
        px = orbit_x[i]
        py = orbit_y[i]

        # Crear figura
        fig = go.Figure()

        # Órbita
        fig.add_trace(
            go.Scatter(
                x=orbit_x,
                y=orbit_y,
                mode="lines",
                name="Orbit"
            )
        )

        # Sol / cuerpo central
        fig.add_trace(
            go.Scatter(
                x=[0],
                y=[0],
                mode="markers",
                marker=dict(size=18),
                name="Star"
            )
        )

        # Planeta
        fig.add_trace(
            go.Scatter(
                x=[px],
                y=[py],
                mode="markers",
                marker=dict(size=12),
                name="Planet"
            )
        )

        # Layout
        fig.update_layout(
            template="plotly_dark",
            title="Animated Orbit",
            xaxis_title="x",
            yaxis_title="y",
            height=600,
            yaxis=dict(
                scaleanchor="x",
                scaleratio=1
            )
        )

        # Actualizar gráfico
        chart.plotly_chart(fig, width="stretch")

        # Espera
        time.sleep(0.02)