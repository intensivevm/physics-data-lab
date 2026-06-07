import streamlit as st


def _result(label, value, unit):
    st.metric(label, f"{value:,.3f} {unit}")


def show_physics_tools():
    st.title("Physics Tools")
    st.write(
        """
        Use these quick calculators to connect common physics equations with
        numerical results. All inputs use SI units.
        """
    )

    tool = st.selectbox(
        "Choose a calculator",
        [
            "Uniform motion",
            "Accelerated motion",
            "Kinetic energy",
            "Potential energy",
            "Force",
            "Work",
        ],
    )

    if tool == "Uniform motion":
        st.subheader("Uniform motion")
        distance = st.number_input("Distance (m)", min_value=0.0, value=100.0)
        time = st.number_input("Time (s)", min_value=0.001, value=10.0)
        velocity = distance / time
        _result("Velocity", velocity, "m/s")
        st.latex(r"v = \frac{d}{t}")

    elif tool == "Accelerated motion":
        st.subheader("Accelerated motion")
        initial_velocity = st.number_input("Initial velocity (m/s)", value=0.0)
        acceleration = st.number_input("Acceleration (m/s^2)", value=9.8)
        time = st.number_input("Time (s)", min_value=0.0, value=5.0)
        final_velocity = initial_velocity + acceleration * time
        displacement = initial_velocity * time + 0.5 * acceleration * time**2
        c1, c2 = st.columns(2)
        with c1:
            _result("Final velocity", final_velocity, "m/s")
        with c2:
            _result("Displacement", displacement, "m")
        st.latex(r"v_f = v_i + at")
        st.latex(r"\Delta x = v_i t + \frac{1}{2}at^2")

    elif tool == "Kinetic energy":
        st.subheader("Kinetic energy")
        mass = st.number_input("Mass (kg)", min_value=0.0, value=2.0)
        velocity = st.number_input("Velocity (m/s)", value=12.0)
        kinetic_energy = 0.5 * mass * velocity**2
        _result("Kinetic energy", kinetic_energy, "J")
        st.latex(r"K = \frac{1}{2}mv^2")

    elif tool == "Potential energy":
        st.subheader("Gravitational potential energy")
        mass = st.number_input("Mass (kg)", min_value=0.0, value=2.0)
        gravity = st.number_input("Gravity (m/s^2)", min_value=0.0, value=9.8)
        height = st.number_input("Height (m)", min_value=0.0, value=8.0)
        potential_energy = mass * gravity * height
        _result("Potential energy", potential_energy, "J")
        st.latex(r"U = mgh")

    elif tool == "Force":
        st.subheader("Force")
        mass = st.number_input("Mass (kg)", min_value=0.0, value=10.0)
        acceleration = st.number_input("Acceleration (m/s^2)", value=2.5)
        force = mass * acceleration
        _result("Force", force, "N")
        st.latex(r"F = ma")

    else:
        st.subheader("Work")
        force = st.number_input("Force (N)", value=25.0)
        distance = st.number_input("Distance (m)", min_value=0.0, value=4.0)
        angle = st.slider("Angle between force and motion (degrees)", 0.0, 180.0, 0.0)
        import math

        work = force * distance * math.cos(math.radians(angle))
        _result("Work", work, "J")
        st.latex(r"W = Fd\cos(\theta)")
