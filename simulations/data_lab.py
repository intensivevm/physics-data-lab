import pandas as pd
import plotly.express as px
import streamlit as st


def _get_numeric_columns(dataframe):
    return dataframe.select_dtypes(include="number").columns.tolist()


def show_data_lab():
    st.title("Data Lab")
    st.write(
        """
        Upload a CSV file to inspect the dataset, review summary statistics,
        and create quick exploratory charts with Plotly.
        """
    )

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is None:
        st.info("Upload a CSV file to start exploring your data.")
        return

    try:
        dataframe = pd.read_csv(uploaded_file)
    except Exception as exc:
        st.error(f"Could not read this CSV file: {exc}")
        return

    if dataframe.empty:
        st.warning("The uploaded file is empty.")
        return

    row_count, column_count = dataframe.shape
    c1, c2, c3 = st.columns(3)
    c1.metric("Rows", f"{row_count:,}")
    c2.metric("Columns", f"{column_count:,}")
    c3.metric("Missing values", f"{int(dataframe.isna().sum().sum()):,}")

    st.subheader("Data preview")
    max_preview_rows = min(100, row_count)
    preview_rows = st.slider(
        "Rows to preview",
        1,
        max_preview_rows,
        min(10, max_preview_rows),
    )
    st.dataframe(dataframe.head(preview_rows), use_container_width=True)

    st.subheader("Summary statistics")
    numeric_columns = _get_numeric_columns(dataframe)
    if numeric_columns:
        st.dataframe(dataframe[numeric_columns].describe().T, use_container_width=True)
    else:
        st.info("No numeric columns were detected, so summary statistics are limited.")

    st.subheader("Build a chart")
    if not numeric_columns:
        st.warning("Charts require at least one numeric column.")
        return

    chart_type = st.selectbox("Chart type", ["Scatter", "Line", "Bar", "Histogram", "Box"])
    all_columns = dataframe.columns.tolist()

    if chart_type in {"Scatter", "Line", "Bar"}:
        col_x, col_y = st.columns(2)
        x_axis = col_x.selectbox("X axis", all_columns)
        y_axis = col_y.selectbox("Y axis", numeric_columns)
    else:
        x_axis = st.selectbox("Column", numeric_columns)
        y_axis = None

    color_options = ["None"] + all_columns
    color_column = st.selectbox("Color by", color_options)
    color = None if color_column == "None" else color_column

    if chart_type == "Scatter":
        fig = px.scatter(dataframe, x=x_axis, y=y_axis, color=color)
    elif chart_type == "Line":
        fig = px.line(dataframe, x=x_axis, y=y_axis, color=color)
    elif chart_type == "Bar":
        fig = px.bar(dataframe, x=x_axis, y=y_axis, color=color)
    elif chart_type == "Histogram":
        fig = px.histogram(dataframe, x=x_axis, color=color)
    else:
        fig = px.box(dataframe, y=x_axis, color=color)

    fig.update_layout(template="plotly_white", height=520)
    st.plotly_chart(fig, use_container_width=True)
