from datetime import date
from html import escape

import requests
import streamlit as st


@st.cache_data(ttl=3600)
def get_apod_data(selected_date):
    api_key = "DEMO_KEY"
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_key,
        "date": selected_date.isoformat(),
        "thumbs": "true",
    }

    response = requests.get(url, params=params, timeout=12)
    response.raise_for_status()
    return response.json()


def show_nasa_apod():
    st.title("NASA Astronomy Picture of the Day")
    st.write(
        """
        Browse NASA's Astronomy Picture of the Day archive with a cleaner view,
        date selection, cached API calls, and graceful error handling.
        """
    )

    c1, c2 = st.columns([1, 1])
    with c1:
        selected_date = st.date_input(
            "Choose a date",
            value=date.today(),
            min_value=date(1995, 6, 16),
            max_value=date.today(),
        )
    with c2:
        st.write("")
        st.write("")
        refresh = st.button("Refresh APOD", use_container_width=True)

    if refresh:
        get_apod_data.clear()

    try:
        with st.spinner("Contacting NASA and preparing the astronomy card..."):
            data = get_apod_data(selected_date)
    except requests.exceptions.HTTPError as exc:
        status = exc.response.status_code if exc.response is not None else "unknown"
        st.error(f"NASA returned an error for this request. Status code: {status}.")
        st.info("Try another date or refresh the request in a moment.")
        return
    except requests.exceptions.Timeout:
        st.error("The NASA API request timed out.")
        st.info("Please refresh or try again later.")
        return
    except requests.exceptions.RequestException as exc:
        st.error(f"Could not fetch data from NASA APOD: {exc}")
        return
    except ValueError:
        st.error("NASA returned data in an unexpected format.")
        return

    title = data.get("title", "Untitled APOD")
    apod_date = data.get("date", selected_date.isoformat())
    explanation = data.get("explanation", "No explanation was provided.")
    media_type = data.get("media_type")
    media_url = data.get("url")
    copyright_text = data.get("copyright", "Public domain or not specified")
    safe_title = escape(title)
    safe_apod_date = escape(apod_date)
    safe_copyright = escape(copyright_text)

    st.markdown(
        f"""
        <div style="
            border: 1px solid rgba(148, 163, 184, 0.25);
            border-radius: 8px;
            padding: 1.2rem;
            margin: 0.5rem 0 1rem 0;
            background: rgba(255, 255, 255, 0.04);
        ">
            <p style="margin:0;color:#2f6fed;font-weight:700;text-transform:uppercase;">
                {safe_apod_date}
            </p>
            <h2 style="margin:0.3rem 0 0.4rem 0;">{safe_title}</h2>
            <p style="margin:0;color:#697386;">Credit: {safe_copyright}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    media_col, text_col = st.columns([1.35, 1])
    with media_col:
        if media_type == "image" and media_url:
            st.image(media_url, use_container_width=True)
        elif media_type == "video" and media_url:
            st.video(media_url)
            thumbnail = data.get("thumbnail_url")
            if thumbnail:
                st.caption("Video APOD preview available from NASA.")
        else:
            st.warning("NASA did not provide a supported media item for this date.")

    with text_col:
        st.subheader("Explanation")
        st.write(explanation)
        if data.get("hdurl"):
            st.link_button("Open HD image", data["hdurl"], use_container_width=True)
        if media_url:
            st.link_button("Open NASA media", media_url, use_container_width=True)
