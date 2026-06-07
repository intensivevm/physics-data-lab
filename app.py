import streamlit as st

from simulations.about import show_about
from simulations.data_lab import show_data_lab
from simulations.nasa_apod import show_nasa_apod
from simulations.orbit import show_orbit
from simulations.physics_tools import show_physics_tools
from simulations.projectile import show_projectile
from simulations.waves import show_waves


st.set_page_config(
    page_title="Physics Data Lab",
    page_icon="P",
    layout="wide",
)


def inject_styles():
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
        }
        .hero {
            padding: 2.4rem;
            border: 1px solid rgba(148, 163, 184, 0.25);
            border-radius: 10px;
            background: linear-gradient(135deg, #101828 0%, #19324d 48%, #144236 100%);
            color: #ffffff;
            margin-bottom: 1.4rem;
        }
        .hero h1 {
            font-size: 3rem;
            line-height: 1.05;
            margin-bottom: 0.8rem;
        }
        .hero p {
            font-size: 1.08rem;
            max-width: 760px;
            color: #d7e3f4;
        }
        .feature-card {
            min-height: 172px;
            padding: 1.15rem;
            border: 1px solid rgba(148, 163, 184, 0.25);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.04);
        }
        .feature-card h3 {
            font-size: 1.05rem;
            margin-bottom: 0.45rem;
        }
        .feature-card p {
            color: #556070;
            margin-bottom: 0;
        }
        .section-label {
            color: #2f6fed;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: .08em;
            font-size: .78rem;
        }
        div[data-testid="stMetric"] {
            border: 1px solid rgba(148, 163, 184, 0.2);
            border-radius: 8px;
            padding: 0.7rem 0.85rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def set_page(section, simulation=None):
    st.session_state["section"] = section
    if simulation:
        st.session_state["simulation"] = simulation


def show_home():
    st.markdown(
        """
        <section class="hero">
            <div class="section-label">Interactive science portfolio project</div>
            <h1>Physics Data Lab</h1>
            <p>
                A Streamlit laboratory for exploring physics simulations, NASA astronomy data,
                CSV analysis, and practical equation-based calculators in one polished dashboard.
            </p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    if c1.button("Open Simulations", use_container_width=True):
        set_page("Simulations", "Orbit")
        st.rerun()
    if c2.button("Analyze CSV Data", use_container_width=True):
        set_page("Data Lab")
        st.rerun()
    if c3.button("Explore NASA APOD", use_container_width=True):
        set_page("NASA APOD")
        st.rerun()
    if c4.button("Use Physics Tools", use_container_width=True):
        set_page("Physics Tools")
        st.rerun()

    st.markdown("### What this project demonstrates")
    cards = st.columns(4)
    features = [
        (
            "Physics simulations",
            "Interactive wave, projectile, and orbital mechanics models with live visual feedback.",
        ),
        (
            "Data analysis",
            "CSV upload, data preview, summary statistics, and Plotly charts for exploratory analysis.",
        ),
        (
            "API integration",
            "NASA Astronomy Picture of the Day with date selection, caching, loading, and error handling.",
        ),
        (
            "Scientific tooling",
            "Reusable calculators for motion, energy, force, and work using standard physics equations.",
        ),
    ]

    for column, (title, description) in zip(cards, features):
        column.markdown(
            f"""
            <div class="feature-card">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### Project overview")
    left, right = st.columns([1.35, 1])
    with left:
        st.write(
            """
            Physics Data Lab is designed as a portfolio-ready educational app.
            It combines scientific computing, interactive visualization, external API usage,
            and practical data workflows inside a clean Streamlit interface.
            """
        )
        st.write(
            """
            The app is intentionally modular: each experience lives in its own Python module,
            making it easy to extend with new simulations, calculators, datasets, or astronomy views.
            """
        )
    with right:
        st.metric("Modules", "7")
        st.metric("Visualization library", "Plotly")
        st.metric("App framework", "Streamlit")


def render_sidebar():
    st.sidebar.title("Physics Data Lab")
    st.sidebar.caption("Interactive physics, data, and astronomy tools.")

    section_options = [
        "Home",
        "Simulations",
        "NASA APOD",
        "Data Lab",
        "Physics Tools",
        "About",
    ]
    section = st.sidebar.radio(
        "Navigation",
        section_options,
        index=section_options.index(st.session_state.get("section", "Home")),
    )
    st.session_state["section"] = section

    simulation = st.session_state.get("simulation", "Waves")
    if section == "Simulations":
        st.sidebar.markdown("### Simulations")
        simulation_options = ["Waves", "Projectile Motion", "Orbit"]
        simulation = st.sidebar.radio(
            "Choose a simulation",
            simulation_options,
            index=simulation_options.index(simulation)
            if simulation in simulation_options
            else 0,
        )
        st.session_state["simulation"] = simulation

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Sections")
    st.sidebar.write("Home")
    st.sidebar.write("Simulations")
    st.sidebar.write("NASA APOD")
    st.sidebar.write("Data Lab")
    st.sidebar.write("About")
    st.sidebar.info("Built with Streamlit, Plotly, NumPy, Pandas, and NASA APIs.")

    return section, simulation


inject_styles()
selected_section, selected_simulation = render_sidebar()

if selected_section == "Home":
    show_home()
elif selected_section == "Simulations":
    if selected_simulation == "Waves":
        show_waves()
    elif selected_simulation == "Projectile Motion":
        show_projectile()
    else:
        show_orbit()
elif selected_section == "NASA APOD":
    show_nasa_apod()
elif selected_section == "Data Lab":
    show_data_lab()
elif selected_section == "Physics Tools":
    show_physics_tools()
else:
    show_about()
