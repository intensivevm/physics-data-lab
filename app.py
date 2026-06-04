import streamlit as st

from simulations.waves import show_waves
from simulations.projectile import show_projectile
from simulations.orbit import show_orbit
from simulations.nasa_apod import show_nasa_apod


st.set_page_config(
    page_title="Physics Data Lab",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Physics Data Lab")
st.caption("Interactive simulations for learning physics with Python")
# Sidebar
st.sidebar.title("🚀 Physics Data Lab")

st.sidebar.write(
    """
    Interactive scientific simulations built with Python.

    Explore:
    - Waves
    - Projectile motion
    - Orbital mechanics
    - NASA astronomy data
    """
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Built using Streamlit, Plotly, NumPy and NASA APIs."
)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌊 Waves",
    "🏀 Projectile Motion",
    "🪐 Orbit Simulation",
    "🛰 NASA APOD",
    "📌 About"
])

with tab1:
    show_waves()

with tab2:
    show_projectile()

with tab3:
    show_orbit()

with tab4:
    show_nasa_apod()

with tab5:
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
    st.write("Python · Streamlit · NumPy · Plotly · Requests")

    st.subheader("Author")
    st.write("Valentin Merlo")