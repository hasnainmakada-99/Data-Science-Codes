import pandas as pd
import streamlit as st

from analysis_core import (
    create_genre_report,
    create_movie_report,
    preprocess_movie_data,
    recommend_movies
)


# ============================================================
# PAGE SETTINGS
# ============================================================
st.set_page_config(
    page_title="Movie Recommendation Analytics Dashboard",
    page_icon="🎬",
    layout="wide"
)


# ============================================================
# SAMPLE DATA FOR DASHBOARD
# The dashboard also uses a dictionary by default.
# ============================================================
def create_dashboard_data():
    movie_data = {
        "MovieID": [
            "MV101", "MV102", "MV103", None, "MV105",
            "MV106", "MV107", "MV108", "MV109", "MV110",
            "MV111", "MV112", "MV113", "MV114", "MV115"
        ],
        "MovieTitle": [
            "The Last Horizon",
            "City Lights",
            "Hidden Truth",
            "Lost Kingdom",
            "Digital Dreams",
            "Silent River",
            "Future Code",
            "Broken Compass",
            "Midnight Journey",
            "Laugh Again",
            "Ocean Mystery",
            "Final Mission",
            "Parallel Lives",
            "Wild Trails",
            "The Great Escape"
        ],
        "Rating": [
            8.5, None, 7.8, 9.1, 8.9,
            None, 9.3, 6.7, 8.1, 7.5,
            8.8, None, 8.4, 7.2, 9.0
        ],
        "Genre": [
            "Science Fiction",
            "Comedy",
            "Thriller",
            "Fantasy",
            "Science Fiction",
            "Drama",
            "Science Fiction",
            None,
            "Adventure",
            "Comedy",
            "Mystery",
            "Action",
            "Drama",
            "Adventure",
            "Action"
        ],
        "ViewCount": [
            125000, 98000, 110000, 150000, 175000,
            87000, 210000, 65000, 132000, 105000,
            143000, 190000, 118000, 99000, 205000
        ],
        "Likes": [
            11200, 7500, 8900, 13500, 16000,
            6100, 19800, 4200, 10400, 8100,
            12100, 17400, 9600, 7200, 18800
        ]
    }

    return pd.DataFrame(movie_data)


# ============================================================
# PAGE TITLE
# ============================================================
st.title("🎬 Movie Recommendation Analytics Dashboard")

st.write(
    "Preprocess movie ratings, compare genres, "
    "track viewer preferences and recommend movies."
)


# ============================================================
# SIDEBAR CONTROLS
# ============================================================
st.sidebar.header("Dashboard Controls")

data_source = st.sidebar.radio(
    "Choose data source",
    ["Use dictionary data", "Upload CSV"]
)

if data_source == "Upload CSV":
    uploaded_file = st.sidebar.file_uploader(
        "Upload movie CSV",
        type=["csv"]
    )

    if uploaded_file is None:
        st.info("Upload a CSV file to continue.")
        st.stop()

    raw_data = pd.read_csv(uploaded_file)

else:
    raw_data = create_dashboard_data()


# ============================================================
# PREPROCESS DATA
# ============================================================
try:
    processed_data, average_rating = (
        preprocess_movie_data(raw_data)
    )
except ValueError as error:
    st.error(str(error))
    st.stop()

available_genres = sorted(
    processed_data["Genre"].unique().tolist()
)

selected_genres = st.sidebar.multiselect(
    "Select genres",
    options=available_genres,
    default=available_genres
)

minimum_rating = st.sidebar.slider(
    "Minimum rating",
    min_value=int(processed_data["Rating"].min()),
    max_value=int(processed_data["Rating"].max()),
    value=int(processed_data["Rating"].min())
)

filtered_data = processed_data[
    processed_data["Genre"].isin(selected_genres)
    & (processed_data["Rating"] >= minimum_rating)
].copy()

if filtered_data.empty:
    st.warning("No movies match the selected filters.")
    st.stop()


# ============================================================
# METRICS
# ============================================================
top_movie = filtered_data.iloc[0]

most_viewed_movie = filtered_data.loc[
    filtered_data["ViewCount"].idxmax()
]

metric_1, metric_2, metric_3, metric_4 = st.columns(4)

metric_1.metric(
    "Movies Analysed",
    len(filtered_data),
    border=True
)

metric_2.metric(
    "Average Rating",
    f'{filtered_data["Rating"].mean():.2f}',
    border=True
)

metric_3.metric(
    "Top Movie",
    top_movie["MovieTitle"],
    delta=f'Rating {top_movie["Rating"]}',
    border=True
)

metric_4.metric(
    "Most Viewed",
    most_viewed_movie["MovieTitle"],
    delta=f'{most_viewed_movie["ViewCount"]:,} views',
    border=True
)


# ============================================================
# DASHBOARD TABS
# ============================================================
(
    preprocessing_tab,
    top_movies_tab,
    genre_tab,
    recommendation_tab,
    report_tab
) = st.tabs(
    [
        "Preprocessing",
        "Top Movies",
        "Genre Report",
        "Recommendations",
        "Automated Report"
    ]
)


# ============================================================
# PREPROCESSING TAB
# ============================================================
with preprocessing_tab:
    st.subheader("Original Dataset with Missing Values")

    st.dataframe(
        raw_data,
        hide_index=True
    )

    st.subheader("Processed Dataset")

    st.success(
        f"Average rating used: {average_rating:.2f}"
    )

    st.dataframe(
        processed_data,
        hide_index=True
    )


# ============================================================
# TOP MOVIES TAB
# ============================================================
with top_movies_tab:
    st.dataframe(
        filtered_data[
            [
                "PopularityRank",
                "MovieTitle",
                "Genre",
                "Rating",
                "ViewCount",
                "PopularityScore"
            ]
        ],
        hide_index=True
    )

    chart_data = filtered_data[
        ["MovieTitle", "Rating"]
    ].set_index("MovieTitle")

    st.bar_chart(chart_data)


# ============================================================
# GENRE REPORT TAB
# ============================================================
with genre_tab:
    genre_report = create_genre_report(
        filtered_data
    )

    st.dataframe(
        genre_report,
        hide_index=True
    )

    chart_data = genre_report[
        ["Genre", "AverageRating"]
    ].set_index("Genre")

    st.bar_chart(chart_data)


# ============================================================
# RECOMMENDATION TAB
# ============================================================
with recommendation_tab:
    preferred_genre = st.selectbox(
        "Select preferred genre",
        options=available_genres
    )

    recommendation_rating = st.slider(
        "Minimum recommendation rating",
        min_value=int(processed_data["Rating"].min()),
        max_value=int(processed_data["Rating"].max()),
        value=int(processed_data["Rating"].min())
    )

    recommendations = recommend_movies(
        processed_data,
        preferred_genre,
        recommendation_rating,
        top_n=5
    )

    st.dataframe(
        recommendations[
            [
                "MovieTitle",
                "Genre",
                "Rating",
                "ViewCount",
                "PopularityScore"
            ]
        ],
        hide_index=True
    )


# ============================================================
# REPORT TAB
# ============================================================
with report_tab:
    report = create_movie_report(
        filtered_data,
        average_rating
    )

    st.text(report)

    st.download_button(
        "Download Report",
        data=report,
        file_name="movie_analytics_report.txt",
        mime="text/plain"
    )