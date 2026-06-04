import streamlit as st
import requests


@st.cache_data(ttl=3600)
def get_apod_data():
    api_key = "DEMO_KEY"
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


def show_nasa_apod():
    st.header("🛰 NASA Astronomy Picture of the Day")

    st.write(
        "This section connects to NASA's APOD API and displays real astronomy data."
    )

    try:
        with st.spinner("Loading NASA astronomy data..."):
            data = get_apod_data()

        title = data["title"]
        date = data["date"]
        explanation = data["explanation"]
        media_type = data["media_type"]
        media_url = data["url"]

        st.subheader(title)
        st.caption(date)

        if media_type == "image":
            st.image(media_url, width="stretch")
        else:
            st.video(media_url)

        st.write(explanation)

    except requests.exceptions.RequestException:
        st.error("Could not fetch data from NASA API. Please try again later.")