import streamlit as st


def _info_card(title, body):
    st.markdown(
        f"""
        <div style="
            border: 1px solid rgba(148, 163, 184, 0.25);
            border-radius: 8px;
            padding: 1rem;
            min-height: 150px;
            background: rgba(255, 255, 255, 0.04);
        ">
            <h3 style="margin-top: 0;">{title}</h3>
            <p style="margin-bottom: 0; color: #5f6b7a;">{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_about():
    st.title("About Physics Data Lab")
    st.write(
        """
        Physics Data Lab is an educational Streamlit application designed to make
        physics concepts easier to explore through simulations, data visualization,
        astronomy content, and practical calculators.
        """
    )

    st.subheader("Purpose")
    st.write(
        """
        The purpose of this project is to combine physics, programming, and data
        analysis in one interactive dashboard. Instead of only reading formulas,
        users can change parameters, observe the results, upload their own data,
        and connect scientific ideas with visual feedback.
        """
    )

    purpose_cards = st.columns(3)
    with purpose_cards[0]:
        _info_card(
            "Learn by experimenting",
            "Change inputs and immediately see how wave, projectile, and orbital models respond.",
        )
    with purpose_cards[1]:
        _info_card(
            "Explore real data",
            "Use CSV uploads and NASA APOD content to connect physics with data-driven workflows.",
        )
    with purpose_cards[2]:
        _info_card(
            "Build portfolio proof",
            "Show applied Python, UI structure, API integration, and scientific visualization in one app.",
        )

    st.subheader("Technologies used")
    tech_cols = st.columns(3)
    tech_cols[0].markdown(
        """
        **Application**

        - Python
        - Streamlit
        - Modular app structure
        """
    )
    tech_cols[1].markdown(
        """
        **Data and math**

        - NumPy
        - Pandas
        - Physics equations
        """
    )
    tech_cols[2].markdown(
        """
        **Visualization and APIs**

        - Plotly
        - Requests
        - NASA Open APIs
        """
    )

    st.subheader("What was learned")
    st.write(
        """
        This project helped practice how to turn scientific formulas into usable
        interfaces, how to organize a Streamlit project into reusable modules,
        and how to build charts that respond to user input. It also introduced
        API error handling, cached data loading, CSV analysis, and the importance
        of clear navigation for multi-section apps.
        """
    )

    learned_cols = st.columns(2)
    with learned_cols[0]:
        st.markdown(
            """
            **Technical lessons**

            - Building interactive controls with Streamlit.
            - Creating Plotly charts and animations.
            - Reading and summarizing CSV data with Pandas.
            - Handling API loading, refresh, and errors.
            """
        )
    with learned_cols[1]:
        st.markdown(
            """
            **Product lessons**

            - Designing a landing page for a portfolio project.
            - Grouping navigation into clear user journeys.
            - Writing educational explanations next to simulations.
            - Presenting features in a professional, readable way.
            """
        )

    st.subheader("Future roadmap")
    st.write(
        """
        Physics Data Lab can keep growing into a richer scientific learning and
        analysis environment. The next improvements would focus on more models,
        stronger data workflows, and a production-ready deployment experience.
        """
    )

    roadmap = [
        "Add more simulations such as pendulum motion, springs, collisions, and electric fields.",
        "Include sample datasets so users can try Data Lab without uploading a file.",
        "Add downloadable chart exports and generated analysis reports.",
        "Support a personal NASA API key through environment variables.",
        "Add tests for physics calculator formulas and data transformations.",
        "Deploy the app publicly with updated screenshots and a live demo link.",
    ]
    for item in roadmap:
        st.checkbox(item, value=False, disabled=True)

    st.subheader("Author")
    st.write("Built by Valentin Merlo as a physics, data, and Python portfolio project.")
