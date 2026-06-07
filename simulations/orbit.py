import numpy as np
import plotly.graph_objects as go
import streamlit as st


def show_orbit():
    st.title("Orbit Simulation")
    st.write(
        """
        Explore how radius and eccentricity shape an orbit. The central body is
        placed at one focus, which matches the geometry used in Keplerian orbits.
        """
    )

    col_controls, col_chart = st.columns([1, 2.2])

    with col_controls:
        semi_major_axis = st.slider("Semi-major axis (a)", 1.0, 10.0, 4.0, 0.1)
        eccentricity = st.slider("Eccentricity (e)", 0.0, 0.85, 0.25, 0.01)
        frame_count = st.slider("Animation smoothness", 80, 360, 180, 20)
        speed = st.slider("Animation speed", 0.25, 3.0, 1.0, 0.25)
        show_radius = st.checkbox("Show radius vector", value=True)

        st.markdown("### Orbital parameters")
        st.write(
            """
            **Semi-major axis** controls the orbit size.
            **Eccentricity** controls how stretched the orbit is.
            A value of `0` is circular, while values closer to `1` are more elliptical.
            """
        )

    theta = np.linspace(0, 2 * np.pi, frame_count)
    semi_latus_rectum = semi_major_axis * (1 - eccentricity**2)
    radius = semi_latus_rectum / (1 + eccentricity * np.cos(theta))
    orbit_x = radius * np.cos(theta)
    orbit_y = radius * np.sin(theta)

    periapsis = semi_major_axis * (1 - eccentricity)
    apoapsis = semi_major_axis * (1 + eccentricity)
    focus_distance = semi_major_axis * eccentricity
    period_label = semi_major_axis ** 1.5

    frame_duration = max(12, int(60 / speed))

    base_traces = [
        go.Scatter(
            x=orbit_x,
            y=orbit_y,
            mode="lines",
            line=dict(color="#5dade2", width=3),
            name="Orbit path",
        ),
        go.Scatter(
            x=[0],
            y=[0],
            mode="markers",
            marker=dict(size=22, color="#ffd166"),
            name="Central body",
        ),
        go.Scatter(
            x=[orbit_x[0]],
            y=[orbit_y[0]],
            mode="markers",
            marker=dict(size=13, color="#ef476f"),
            name="Orbiting body",
        ),
    ]

    if show_radius:
        base_traces.append(
            go.Scatter(
                x=[0, orbit_x[0]],
                y=[0, orbit_y[0]],
                mode="lines",
                line=dict(color="#95a5a6", width=2, dash="dot"),
                name="Radius vector",
            )
        )

    frames = []
    for index in range(frame_count):
        frame_data = [
            go.Scatter(x=orbit_x, y=orbit_y),
            go.Scatter(x=[0], y=[0]),
            go.Scatter(x=[orbit_x[index]], y=[orbit_y[index]]),
        ]
        if show_radius:
            frame_data.append(
                go.Scatter(x=[0, orbit_x[index]], y=[0, orbit_y[index]])
            )
        frames.append(go.Frame(data=frame_data, name=str(index)))

    fig = go.Figure(data=base_traces, frames=frames)
    fig.update_layout(
        template="plotly_dark",
        height=620,
        margin=dict(l=20, r=20, t=60, b=20),
        title="Keplerian Orbit Animation",
        xaxis=dict(title="x", zeroline=False),
        yaxis=dict(title="y", zeroline=False, scaleanchor="x", scaleratio=1),
        updatemenus=[
            {
                "type": "buttons",
                "showactive": False,
                "x": 0.02,
                "y": 1.12,
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": frame_duration, "redraw": True},
                                "fromcurrent": True,
                                "transition": {"duration": 0},
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                                "transition": {"duration": 0},
                            },
                        ],
                    },
                ],
            }
        ],
        sliders=[
            {
                "currentvalue": {"prefix": "Position: "},
                "steps": [
                    {
                        "label": str(index),
                        "method": "animate",
                        "args": [
                            [str(index)],
                            {
                                "mode": "immediate",
                                "frame": {"duration": 0, "redraw": True},
                                "transition": {"duration": 0},
                            },
                        ],
                    }
                    for index in range(0, frame_count, max(1, frame_count // 18))
                ],
            }
        ],
    )

    with col_chart:
        st.plotly_chart(fig, use_container_width=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Periapsis", f"{periapsis:.2f}")
    m2.metric("Apoapsis", f"{apoapsis:.2f}")
    m3.metric("Focus distance", f"{focus_distance:.2f}")
    m4.metric("Relative period", f"{period_label:.2f}")

    st.subheader("How to read the orbit")
    st.write(
        """
        In the polar equation `r = a(1 - e^2) / (1 + e cos(theta))`,
        `r` is the distance from the central body to the orbiting body.
        Higher eccentricity lowers the periapsis, raises the apoapsis,
        and makes the body's distance change more dramatically during one revolution.
        """
    )
    st.latex(r"r = \frac{a(1 - e^2)}{1 + e\cos(\theta)}")
    st.latex(r"T^2 \propto a^3")
