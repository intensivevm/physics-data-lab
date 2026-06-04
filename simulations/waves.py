import streamlit as st
import numpy as np
import plotly.graph_objects as go


def show_waves():
    st.header("🌊 Wave Simulation")
    st.write(
        "Explore how amplitude, frequency and phase affect a periodic wave."
    )

    col_controls, col_graph = st.columns([1, 2])

    with col_controls:
        wave_type = st.selectbox("Wave type", ["Sine", "Cosine"])
        amplitude = st.slider("Amplitude", 1.0, 10.0, 2.0)
        frequency = st.slider("Frequency", 0.5, 10.0, 2.0)
        phase = st.slider("Phase", 0.0, 10.0, 0.0)

        st.markdown("### What do these controls mean?")
        st.write("**Amplitude:** controls the height of the wave.")
        st.write("**Frequency:** controls how many oscillations appear.")
        st.write("**Phase:** moves the wave horizontally.")

    x = np.linspace(0, 10, 1000)

    if wave_type == "Sine":
        y = amplitude * np.sin(frequency * x + phase)
        formula = r"y = A \sin(fx + \phi)"
    else:
        y = amplitude * np.cos(frequency * x + phase)
        formula = r"y = A \cos(fx + \phi)"

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            name=wave_type,
            line=dict(width=4)
        )
    )

    fig.update_layout(
        title=f"{wave_type} Wave",
        template="plotly_dark",
        xaxis_title="x",
        yaxis_title="y",
        height=550
    )

    with col_graph:
        st.plotly_chart(fig, width="stretch")

    st.markdown("### Mathematical model")
    st.latex(formula)

    col1, col2, col3 = st.columns(3)
    col1.metric("Amplitude", amplitude)
    col2.metric("Frequency", frequency)
    col3.metric("Phase", phase)