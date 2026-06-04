import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Physics Data Lab",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Physics Data Lab")
st.caption("Interactive simulations for learning physics with Python")

tab1, tab2, tab3, tab4 = st.tabs([
    "🌊 Waves",
    "🏀 Projectile Motion",
    "🪐 Orbit Simulation",
    "📌 About"
])

# ---------------- WAVES ----------------

with tab1:
    st.header("🌊 Wave Simulation")

    col_controls, col_info = st.columns([1, 2])

    with col_controls:
        wave_type = st.selectbox("Wave type", ["Sine", "Cosine"])
        amplitude = st.slider("Amplitude", 1.0, 10.0, 2.0)
        frequency = st.slider("Frequency", 0.5, 10.0, 2.0)
        phase = st.slider("Phase", 0.0, 10.0, 0.0)

    x = np.linspace(0, 10, 1000)

    if wave_type == "Sine":
        y = amplitude * np.sin(frequency * x + phase)
        formula = r"y = A \sin(fx + \phi)"
    else:
        y = amplitude * np.cos(frequency * x + phase)
        formula = r"y = A \cos(fx + \phi)"

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name=wave_type))

    fig.update_layout(
        title=f"{wave_type} Wave",
        template="plotly_dark",
        xaxis_title="x",
        yaxis_title="y",
        height=550
    )

    with col_info:
        st.plotly_chart(fig, use_container_width=True)

    st.latex(formula)

    st.info(
        "Amplitude controls the height of the wave, frequency controls how many "
        "oscillations appear, and phase shifts the wave horizontally."
    )

# ---------------- PROJECTILE MOTION ----------------

with tab2:
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

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Trajectory"))

    fig2.update_layout(
        title="Projectile Trajectory",
        template="plotly_dark",
        xaxis_title="Horizontal distance (m)",
        yaxis_title="Height (m)",
        height=550
    )

    with col_graph:
        st.plotly_chart(fig2, use_container_width=True)

    max_height = (velocity**2 * np.sin(theta)**2) / (2 * gravity)
    range_distance = (velocity**2 * np.sin(2 * theta)) / gravity

    c1, c2, c3 = st.columns(3)
    c1.metric("Time of flight", f"{time_of_flight:.2f} s")
    c2.metric("Max height", f"{max_height:.2f} m")
    c3.metric("Range", f"{range_distance:.2f} m")

    st.latex(r"x(t) = v_0 \cos(\theta)t")
    st.latex(r"y(t) = v_0 \sin(\theta)t - \frac{1}{2}gt^2")

# ---------------- ORBIT ----------------

with tab3:
    st.header("🪐 Simple Orbit Simulation")

    col_controls, col_graph = st.columns([1, 2])

    with col_controls:
        radius = st.slider("Orbit radius", 1.0, 10.0, 4.0)
        eccentricity = st.slider("Eccentricity", 0.0, 0.8, 0.2)

    theta = np.linspace(0, 2 * np.pi, 600)

    r = radius * (1 - eccentricity**2) / (1 + eccentricity * np.cos(theta))

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    fig3 = go.Figure()

    fig3.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="lines",
        name="Orbit"
    ))

    fig3.add_trace(go.Scatter(
        x=[0],
        y=[0],
        mode="markers",
        name="Central Body",
        marker=dict(size=14)
    ))

    fig3.update_layout(
        title="Elliptical Orbit",
        template="plotly_dark",
        xaxis_title="x",
        yaxis_title="y",
        height=550,
        yaxis=dict(scaleanchor="x", scaleratio=1)
    )

    with col_graph:
        st.plotly_chart(fig3, use_container_width=True)

    st.latex(r"r = \frac{a(1-e^2)}{1 + e\cos(\theta)}")

    st.info(
        "This is a simplified orbital model. The eccentricity controls how stretched "
        "the orbit is: 0 is circular, higher values are more elliptical."
    )

# ---------------- ABOUT ----------------

with tab4:
    st.header("📌 About this project")

    st.write(
        """
        **Physics Data Lab** is an interactive physics dashboard built with Python.

        The goal of this project is to combine:
        - Physics
        - Data visualization
        - Scientific computing
        - Interactive web apps
        - GitHub portfolio development
        """
    )

    st.subheader("Technologies")
    st.write("Python · Streamlit · NumPy · Plotly")

    st.subheader("Author")
    st.write("Valentin Merlo")