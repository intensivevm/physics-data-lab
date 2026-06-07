# Physics Data Lab

Physics Data Lab is an interactive Streamlit application for exploring physics simulations, astronomy data, CSV analysis, and practical physics calculators. It was built as a portfolio project to demonstrate scientific computing, data visualization, API integration, and clean dashboard design with Python.

## Features

- Professional Streamlit home page with landing layout, feature cards, project overview, and quick navigation.
- Sidebar navigation organized into Home, Simulations, NASA APOD, Data Lab, Physics Tools, and About.
- Interactive simulations for waves, projectile motion, and orbital mechanics.
- Improved orbit simulation with Plotly animation, play/pause controls, speed settings, smooth frames, and educational orbital parameter notes.
- NASA Astronomy Picture of the Day viewer with date selector, loading state, refresh button, error handling, and card-style presentation.
- Data Lab page for CSV uploads, data preview, summary statistics, and basic Plotly charts.
- Physics Tools page with calculators for uniform motion, accelerated motion, kinetic energy, potential energy, force, and work.

## Screenshots

Add updated screenshots here after running the application locally or deploying it.

```text
assets/screenshot.jpg
```

Recommended screenshots:

- Home landing page
- Orbit simulation
- Data Lab with an uploaded CSV
- NASA APOD page
- Physics Tools calculators

## Technologies Used

- Python
- Streamlit
- NumPy
- Pandas
- Plotly
- Requests
- NASA Open APIs

## Setup Instructions

1. Clone the repository.

```bash
git clone https://github.com/intensivevm/physics-data-lab.git
cd physics-data-lab
```

2. Create and activate a virtual environment.

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS or Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Run the app.

```bash
python -m streamlit run app.py
```

## Live Demo

Live demo: add your deployed Streamlit Community Cloud URL here.

Suggested deployment target:

```text
https://share.streamlit.io/
```

## Project Structure

```text
physics-data-lab/
├── app.py
├── requirements.txt
├── assets/
│   └── screenshot.jpg
└── simulations/
    ├── about.py
    ├── data_lab.py
    ├── nasa_apod.py
    ├── orbit.py
    ├── physics_tools.py
    ├── projectile.py
    └── waves.py
```

## Roadmap

- Add more simulations such as pendulum motion, spring systems, and electric fields.
- Add sample CSV datasets for the Data Lab page.
- Add downloadable chart exports.
- Add unit tests for calculator equations.
- Replace the NASA demo API key with an environment-based API key.
- Add fresh screenshots after deployment.

## Author

Valentin Merlo

- GitHub: [@intensivevm](https://github.com/intensivevm)
