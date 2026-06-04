import streamlit as st
import numpy as np
import plotly.graph_objects as go


def show_projectile():
    st.header("🏀 Projectile Motion")

    col_controls, col_graph = st.columns([1, 2])

    with col_controls:
        velocity = st.slider("Initial velocity (m/s)", 5.0, 100.0, 30.0)
        angle = st.slider("Launch angle (degrees)", 5.0, 85.0, 45.0)
        gravity = st.slider("Gravity (m/s²)", 1.0, 20.0, 9.8)

    theta = np.radians(angle)

    time_of_flight = (2 * velocity * np.sin(theta)) / gravity
    t = np.linspace(0, time_of_flight, 300)

    x = velocity * np.cos(theta) * t
    y = velocity * np.sin(theta) * t - 0.5 * gravity * t**2

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Trajectory"))

    fig.update_layout(
        title="Projectile Trajectory",
        template="plotly_dark",
        xaxis_title="Horizontal distance (m)",
        yaxis_title="Height (m)",
        height=550
    )

    with col_graph:
        st.plotly_chart(fig, width="stretch")

    max_height = (velocity**2 * np.sin(theta)**2) / (2 * gravity)
    range_distance = (velocity**2 * np.sin(2 * theta)) / gravity

    c1, c2, c3 = st.columns(3)
    c1.metric("Time of flight", f"{time_of_flight:.2f} s")
    c2.metric("Max height", f"{max_height:.2f} m")
    c3.metric("Range", f"{range_distance:.2f} m")

    st.latex(r"x(t) = v_0 \cos(\theta)t")
    st.latex(r"y(t) = v_0 \sin(\theta)t - \frac{1}{2}gt^2")