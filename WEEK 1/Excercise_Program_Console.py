import sys
from pathlib import Path

import pandas as pd

from analysis_core import (
    analyse_models,
    clean_data,
    create_algorithm_summary,
    create_report,
    create_sample_data,
    perform_basic_operations
)


# ============================================================
# HEADING FUNCTION
# This keeps console output neat and readable.
# ============================================================
def print_heading(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


# ============================================================
# MAIN CONSOLE PROGRAM
#
# Run with sample data:
# python console_app.py
#
# Run with CSV data:
# python console_app.py sample_ai_models.csv
# ============================================================
def main():
    print_heading("AI MODEL PERFORMANCE ANALYSIS - CONSOLE MODE")

    csv_file = None

    # If the user gives a file path, use that CSV.
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]

    if csv_file:
        csv_path = Path(csv_file)

        if not csv_path.exists():
            print(f"Error: File not found: {csv_path}")
            return

        print(f"Using CSV file: {csv_path}")
        raw_data = pd.read_csv(csv_path)

    else:
        print("Using built-in sample data.")
        raw_data = create_sample_data()

    try:
        cleaned_data = clean_data(raw_data)
    except ValueError as error:
        print(f"Data error: {error}")
        return

    analysed_data = analyse_models(
        cleaned_data,
        production_threshold=90.0
    )

    results = perform_basic_operations(
        analysed_data
    )

    print_heading("ORIGINAL CLEANED DATA")
    print(
        cleaned_data.to_string(index=False)
    )

    print_heading("1. SELECT MODELID AND ACCURACY")
    print(
        results["selected_columns"]
        .to_string(index=False)
    )

    print_heading(
        "2. FILTER MODELS WITH ACCURACY GREATER THAN 90%"
    )
    print(
        results["models_above_90"][
            ["ModelID", "Algorithm", "Accuracy"]
        ].to_string(index=False)
    )

    print_heading(
        '3. ADD STATUS WITH DEFAULT "PRODUCTION READY"'
    )
    print(
        results["status_table"]
        .to_string(index=False)
    )

    print_heading("4. SORT MODELS BY ACCURACY")
    print(
        results["sorted_models"][
            ["ModelID", "Algorithm", "Accuracy"]
        ].to_string(index=False)
    )

    print_heading("5. CALCULATE AVERAGE MODEL ACCURACY")
    print(
        f'Average model accuracy: '
        f'{results["average_accuracy"]:.2f}%'
    )

    print_heading("MODEL RANKING")
    print(
        analysed_data[
            [
                "Rank",
                "ModelID",
                "Algorithm",
                "PreviousAccuracy",
                "Accuracy",
                "Improvement",
                "Status"
            ]
        ].to_string(index=False)
    )

    print_heading("ALGORITHM PERFORMANCE COMPARISON")
    algorithm_summary = create_algorithm_summary(
        analysed_data
    )

    print(
        algorithm_summary.to_string(index=False)
    )

    print_heading("ACCURACY IMPROVEMENT TRACKING")
    print(
        analysed_data[
            [
                "ModelID",
                "PreviousAccuracy",
                "Accuracy",
                "Improvement",
                "ImprovementStatus"
            ]
        ].to_string(index=False)
    )

    report = create_report(
        analysed_data,
        production_threshold=90.0
    )

    print_heading("AUTOMATED EVALUATION REPORT")
    print(report)

    # Save analysed data.
    analysed_data.to_csv(
        "console_ai_model_results.csv",
        index=False
    )

    # Save the report.
    with open(
        "console_ai_model_report.txt",
        "w",
        encoding="utf-8"
    ) as report_file:
        report_file.write(report)

    print_heading("FILES CREATED")
    print("console_ai_model_results.csv")
    print("console_ai_model_report.txt")


if __name__ == "__main__":
    main()