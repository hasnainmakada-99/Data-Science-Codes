import pandas as pd

from analysis_core import (
    create_genre_report,
    create_movie_report,
    preprocess_movie_data,
    recommend_movies
)


# ============================================================
# HEADING FUNCTION
# This makes the console output easier to read.
# ============================================================
def print_heading(title):
    print("\n" + "=" * 76)
    print(title)
    print("=" * 76)


# ============================================================
# MAIN CONSOLE PROGRAM
# The dataset is directly written as a Python dictionary.
#
# Run:
# python console_app.py
# ============================================================
def main():
    print_heading(
        "MOVIE RATING DATA PREPROCESSING USING PANDAS"
    )

    # --------------------------------------------------------
    # 1. CREATE DATASET WITH MISSING VALUES
    # None represents a missing value.
    # --------------------------------------------------------
    movie_data = {
        "MovieID": [
            "MV101",
            "MV102",
            "MV103",
            None,
            "MV105",
            "MV106",
            "MV107",
            "MV108",
            "MV109",
            "MV110",
            "MV111",
            "MV112",
            "MV113",
            "MV114",
            "MV115"
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
            8.5,
            None,
            7.8,
            9.1,
            8.9,
            None,
            9.3,
            6.7,
            8.1,
            7.5,
            8.8,
            None,
            8.4,
            7.2,
            9.0
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
            125000,
            98000,
            110000,
            150000,
            175000,
            87000,
            210000,
            65000,
            132000,
            105000,
            143000,
            190000,
            118000,
            99000,
            205000
        ],

        "Likes": [
            11200,
            7500,
            8900,
            13500,
            16000,
            6100,
            19800,
            4200,
            10400,
            8100,
            12100,
            17400,
            9600,
            7200,
            18800
        ]
    }

    # Convert dictionary into a Pandas DataFrame.
    movies = pd.DataFrame(movie_data)

    print_heading(
        "1. ORIGINAL DATASET WITH MISSING VALUES"
    )
    print(
        movies.to_string(index=False)
    )

    # Perform all preprocessing steps.
    processed_movies, average_rating = (
        preprocess_movie_data(movies)
    )

    print_heading(
        "2. FILL MISSING RATING USING AVERAGE RATING"
    )
    print(
        f"Average Rating used: {average_rating:.2f}"
    )

    print(
        processed_movies[
            ["MovieID", "MovieTitle", "Rating"]
        ].to_string(index=False)
    )

    print_heading(
        "3. REMOVE ROWS WITH MISSING MOVIEID OR GENRE"
    )
    print(
        processed_movies[
            [
                "MovieID",
                "MovieTitle",
                "Genre",
                "Rating"
            ]
        ].to_string(index=False)
    )

    print_heading(
        "4. CONVERT RATING INTO INTEGER TYPE"
    )
    print(
        processed_movies[
            ["MovieID", "Rating"]
        ].to_string(index=False)
    )

    print(
        "\nRating data type:",
        processed_movies["Rating"].dtype
    )

    print_heading(
        "5. NORMALIZE RATING VALUES"
    )
    print(
        processed_movies[
            [
                "MovieID",
                "MovieTitle",
                "Rating",
                "NormalizedRating"
            ]
        ].to_string(index=False)
    )

    print_heading(
        "TOP-RATED AND POPULAR MOVIES"
    )
    print(
        processed_movies[
            [
                "PopularityRank",
                "MovieID",
                "MovieTitle",
                "Genre",
                "Rating",
                "ViewCount",
                "PopularityScore"
            ]
        ].to_string(index=False)
    )

    print_heading(
        "GENRE-WISE PERFORMANCE REPORT"
    )

    genre_report = create_genre_report(
        processed_movies
    )

    print(
        genre_report.to_string(index=False)
    )

    print_heading(
        "SAMPLE MOVIE RECOMMENDATIONS"
    )

    preferred_genre = "Science Fiction"

    recommendations = recommend_movies(
        processed_movies,
        preferred_genre=preferred_genre,
        minimum_rating=7,
        top_n=5
    )

    print(
        f"Preferred Genre: {preferred_genre}\n"
    )

    print(
        recommendations[
            [
                "MovieID",
                "MovieTitle",
                "Genre",
                "Rating",
                "PopularityScore"
            ]
        ].to_string(index=False)
    )

    report = create_movie_report(
        processed_movies,
        average_rating
    )

    print_heading(
        "AUTOMATED MOVIE ANALYTICS REPORT"
    )

    print(report)

    # Save the processed results.
    processed_movies.to_csv(
        "processed_movie_data.csv",
        index=False
    )

    genre_report.to_csv(
        "genre_wise_report.csv",
        index=False
    )

    with open(
        "movie_analytics_report.txt",
        "w",
        encoding="utf-8"
    ) as report_file:
        report_file.write(report)

    print_heading("FILES CREATED")

    print("processed_movie_data.csv")
    print("genre_wise_report.csv")
    print("movie_analytics_report.txt")


if __name__ == "__main__":
    main()