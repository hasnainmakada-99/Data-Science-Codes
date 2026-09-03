import pandas as pd


# ============================================================
# DATA PREPROCESSING
# This function performs all required Pandas operations.
# ============================================================
def preprocess_movie_data(raw_data):
    # Work on a copy so the original data remains unchanged.
    data = raw_data.copy()

    # Remove unwanted spaces from column names.
    data.columns = data.columns.str.strip()

    # These columns are compulsory.
    required_columns = ["MovieID", "Rating", "Genre"]

    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            "Missing required columns: "
            + ", ".join(missing_columns)
        )

    # Convert Rating values into numbers.
    # Invalid values become missing values.
    data["Rating"] = pd.to_numeric(
        data["Rating"],
        errors="coerce"
    )

    # Calculate average rating before filling missing values.
    average_rating = data["Rating"].mean()

    # Fill missing Rating values using the average rating.
    data["Rating"] = data["Rating"].fillna(
        average_rating
    )

    # Remove rows with missing MovieID or Genre.
    data = data.dropna(
        subset=["MovieID", "Genre"]
    )

    # Clean text values.
    data["MovieID"] = (
        data["MovieID"]
        .astype(str)
        .str.strip()
    )

    data["Genre"] = (
        data["Genre"]
        .astype(str)
        .str.strip()
    )

    # Add MovieTitle when the column is missing.
    if "MovieTitle" not in data.columns:
        data["MovieTitle"] = data["MovieID"]

    data["MovieTitle"] = (
        data["MovieTitle"]
        .astype(str)
        .str.strip()
    )

    # Convert Rating into integer type.
    data["Rating"] = (
        data["Rating"]
        .round()
        .astype(int)
    )

    # Normalize Rating using Min-Max normalization.
    minimum_rating = data["Rating"].min()
    maximum_rating = data["Rating"].max()

    if maximum_rating == minimum_rating:
        data["NormalizedRating"] = 0.0
    else:
        data["NormalizedRating"] = (
            (data["Rating"] - minimum_rating)
            / (maximum_rating - minimum_rating)
        ).round(3)

    # Add ViewCount when it is missing.
    if "ViewCount" not in data.columns:
        data["ViewCount"] = 0

    # Add Likes when it is missing.
    if "Likes" not in data.columns:
        data["Likes"] = 0

    # Convert ViewCount and Likes into integer values.
    data["ViewCount"] = pd.to_numeric(
        data["ViewCount"],
        errors="coerce"
    ).fillna(0).astype(int)

    data["Likes"] = pd.to_numeric(
        data["Likes"],
        errors="coerce"
    ).fillna(0).astype(int)

    # Calculate engagement rate.
    data["EngagementRate"] = 0.0

    valid_view_rows = data["ViewCount"] > 0

    data.loc[
        valid_view_rows,
        "EngagementRate"
    ] = (
        data.loc[valid_view_rows, "Likes"]
        / data.loc[valid_view_rows, "ViewCount"]
        * 100
    ).round(2)

    # Calculate a simple popularity score.
    maximum_engagement = data["EngagementRate"].max()

    if maximum_engagement == 0:
        normalized_engagement = 0
    else:
        normalized_engagement = (
            data["EngagementRate"]
            / maximum_engagement
        )

    data["PopularityScore"] = (
        data["NormalizedRating"] * 0.60
        + normalized_engagement * 0.40
    ).round(3)

    # Sort popular movies first.
    data = data.sort_values(
        by=["PopularityScore", "Rating"],
        ascending=[False, False]
    ).reset_index(drop=True)

    # Add popularity rank.
    data["PopularityRank"] = range(
        1,
        len(data) + 1
    )

    return data, average_rating


# ============================================================
# GENRE-WISE REPORT
# ============================================================
def create_genre_report(data):
    genre_report = (
        data.groupby(
            "Genre",
            as_index=False
        )
        .agg(
            MovieCount=("MovieID", "count"),
            AverageRating=("Rating", "mean"),
            HighestRating=("Rating", "max"),
            TotalViews=("ViewCount", "sum"),
            AverageEngagement=("EngagementRate", "mean")
        )
    )

    genre_report[
        ["AverageRating", "AverageEngagement"]
    ] = genre_report[
        ["AverageRating", "AverageEngagement"]
    ].round(2)

    return genre_report.sort_values(
        by=["AverageRating", "TotalViews"],
        ascending=[False, False]
    ).reset_index(drop=True)


# ============================================================
# SIMPLE MOVIE RECOMMENDATION
# ============================================================
def recommend_movies(
    data,
    preferred_genre,
    minimum_rating=0,
    top_n=5
):
    recommendations = data[
        (data["Genre"] == preferred_genre)
        & (data["Rating"] >= minimum_rating)
    ].copy()

    recommendations = recommendations.sort_values(
        by=["PopularityScore", "Rating"],
        ascending=[False, False]
    )

    return recommendations.head(top_n)


# ============================================================
# AUTOMATED MOVIE ANALYTICS REPORT
# ============================================================
def create_movie_report(
    data,
    average_rating_used
):
    if data.empty:
        return "No movie records are available."

    top_movie = data.iloc[0]

    most_viewed_movie = data.loc[
        data["ViewCount"].idxmax()
    ]

    genre_report = create_genre_report(data)
    best_genre = genre_report.iloc[0]

    report = f"""
MOVIE STREAMING ANALYTICS REPORT
==================================================

Total cleaned movie records: {len(data)}
Average rating used to fill missing values: {average_rating_used:.2f}
Average final rating: {data["Rating"].mean():.2f}
Number of genres: {data["Genre"].nunique()}

TOP-RATED AND MOST POPULAR MOVIE
Movie ID: {top_movie["MovieID"]}
Movie Title: {top_movie["MovieTitle"]}
Genre: {top_movie["Genre"]}
Rating: {top_movie["Rating"]}
Popularity Score: {top_movie["PopularityScore"]:.3f}

MOST VIEWED MOVIE
Movie Title: {most_viewed_movie["MovieTitle"]}
Views: {most_viewed_movie["ViewCount"]}

BEST-PERFORMING GENRE
Genre: {best_genre["Genre"]}
Average Rating: {best_genre["AverageRating"]:.2f}
Total Views: {int(best_genre["TotalViews"])}

CONCLUSION
The movie dataset was cleaned and preprocessed successfully.
Missing Rating values were filled using the average rating.
Rows with missing MovieID or Genre were removed.
Ratings were converted to integers and normalized.
"""

    return report.strip()