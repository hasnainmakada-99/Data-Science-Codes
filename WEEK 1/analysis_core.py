import pandas as pd


# ============================================================
# SAMPLE DATA
# This function creates sample AI model performance records.
# Both the console program and dashboard use this data.
# ============================================================
def create_sample_data():
    model_data = {
        "ModelID": [
            "M101", "M102", "M103", "M104", "M105",
            "M106", "M107", "M108", "M109", "M110",
            "M111", "M112"
        ],
        "Algorithm": [
            "Logistic Regression",
            "Decision Tree",
            "Random Forest",
            "Support Vector Machine",
            "K-Nearest Neighbors",
            "Random Forest",
            "Decision Tree",
            "Neural Network",
            "Logistic Regression",
            "Neural Network",
            "Gradient Boosting",
            "Gradient Boosting"
        ],
        "PreviousAccuracy": [
            84.5, 87.0, 90.2, 88.5, 82.5,
            91.0, 85.5, 92.0, 86.0, 93.1,
            89.4, 91.8
        ],
        "Accuracy": [
            87.2, 89.5, 93.8, 91.4, 85.6,
            94.5, 88.3, 96.1, 90.8, 95.4,
            92.7, 94.1
        ]
    }

    return pd.DataFrame(model_data)


# ============================================================
# DATA CLEANING
# This function prepares either sample data or uploaded CSV data.
# ============================================================
def clean_data(raw_data):
    data = raw_data.copy()

    # Remove unnecessary spaces from column names.
    data.columns = data.columns.str.strip()

    # These columns must be present.
    required_columns = ["ModelID", "Algorithm", "Accuracy"]

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

    # Clean the text columns.
    data["ModelID"] = (
        data["ModelID"]
        .astype(str)
        .str.strip()
    )

    data["Algorithm"] = (
        data["Algorithm"]
        .astype(str)
        .str.strip()
    )

    # Convert accuracy values into numbers.
    # Invalid values become NaN.
    data["Accuracy"] = pd.to_numeric(
        data["Accuracy"],
        errors="coerce"
    )

    # PreviousAccuracy is used to calculate improvement.
    # If it is missing, copy the current Accuracy.
    if "PreviousAccuracy" not in data.columns:
        data["PreviousAccuracy"] = data["Accuracy"]
    else:
        data["PreviousAccuracy"] = pd.to_numeric(
            data["PreviousAccuracy"],
            errors="coerce"
        )

    # Remove rows with missing important values.
    data = data.dropna(
        subset=[
            "ModelID",
            "Algorithm",
            "Accuracy",
            "PreviousAccuracy"
        ]
    )

    # Keep only valid percentage values.
    data = data[
        data["Accuracy"].between(0, 100)
        & data["PreviousAccuracy"].between(0, 100)
    ]

    # Remove duplicate Model IDs.
    data = data.drop_duplicates(
        subset="ModelID",
        keep="first"
    )

    return data.reset_index(drop=True)


# ============================================================
# MODEL ANALYSIS
# This function adds Status, Improvement and Rank.
# ============================================================
def analyse_models(data, production_threshold=90.0):
    analysed_data = data.copy()

    # Add the required default status.
    analysed_data["Status"] = "Production Ready"

    # Models below the threshold need improvement.
    analysed_data.loc[
        analysed_data["Accuracy"] < production_threshold,
        "Status"
    ] = "Needs Improvement"

    # Calculate the change in accuracy.
    analysed_data["Improvement"] = (
        analysed_data["Accuracy"]
        - analysed_data["PreviousAccuracy"]
    ).round(2)

    # Add a readable improvement label.
    analysed_data["ImprovementStatus"] = "No Change"

    analysed_data.loc[
        analysed_data["Improvement"] > 0,
        "ImprovementStatus"
    ] = "Improved"

    analysed_data.loc[
        analysed_data["Improvement"] < 0,
        "ImprovementStatus"
    ] = "Declined"

    # Sort models from highest accuracy to lowest accuracy.
    analysed_data = analysed_data.sort_values(
        by="Accuracy",
        ascending=False
    ).reset_index(drop=True)

    # Add model rank.
    analysed_data["Rank"] = range(
        1,
        len(analysed_data) + 1
    )

    return analysed_data


# ============================================================
# BASIC OPERATIONS
# These are the five required Pandas operations.
# ============================================================
def perform_basic_operations(data):
    # 1. Select ModelID and Accuracy.
    selected_columns = data[
        ["ModelID", "Accuracy"]
    ]

    # 2. Filter models with Accuracy greater than 90%.
    models_above_90 = data[
        data["Accuracy"] > 90
    ]

    # 3. Display the Status column.
    status_table = data[
        ["ModelID", "Accuracy", "Status"]
    ]

    # 4. Sort models by Accuracy.
    sorted_models = data.sort_values(
        by="Accuracy",
        ascending=False
    )

    # 5. Calculate average Accuracy.
    average_accuracy = data["Accuracy"].mean()

    return {
        "selected_columns": selected_columns,
        "models_above_90": models_above_90,
        "status_table": status_table,
        "sorted_models": sorted_models,
        "average_accuracy": average_accuracy
    }


# ============================================================
# ALGORITHM COMPARISON
# This function compares the performance of each algorithm.
# ============================================================
def create_algorithm_summary(data):
    summary = (
        data.groupby(
            "Algorithm",
            as_index=False
        )
        .agg(
            ModelCount=("ModelID", "count"),
            MinimumAccuracy=("Accuracy", "min"),
            MaximumAccuracy=("Accuracy", "max"),
            AverageAccuracy=("Accuracy", "mean"),
            AverageImprovement=("Improvement", "mean")
        )
    )

    number_columns = [
        "MinimumAccuracy",
        "MaximumAccuracy",
        "AverageAccuracy",
        "AverageImprovement"
    ]

    summary[number_columns] = (
        summary[number_columns]
        .round(2)
    )

    return summary.sort_values(
        by="AverageAccuracy",
        ascending=False
    ).reset_index(drop=True)


# ============================================================
# AUTOMATED REPORT
# This report is used by both console and dashboard programs.
# ============================================================
def create_report(data, production_threshold=90.0):
    if data.empty:
        return "No model records are available."

    average_accuracy = data["Accuracy"].mean()

    best_model = data.loc[
        data["Accuracy"].idxmax()
    ]

    lowest_model = data.loc[
        data["Accuracy"].idxmin()
    ]

    most_improved_model = data.loc[
        data["Improvement"].idxmax()
    ]

    production_ready_count = (
        data["Status"] == "Production Ready"
    ).sum()

    algorithm_summary = create_algorithm_summary(data)
    best_algorithm = algorithm_summary.iloc[0]

    report = f"""
AI MODEL EVALUATION REPORT
==================================================

SUMMARY
Total models analysed: {len(data)}
Production threshold: {production_threshold:.1f}%
Average model accuracy: {average_accuracy:.2f}%
Production-ready models: {production_ready_count}
Models needing improvement: {len(data) - production_ready_count}

BEST MODEL
Model ID: {best_model["ModelID"]}
Algorithm: {best_model["Algorithm"]}
Accuracy: {best_model["Accuracy"]:.2f}%

LOWEST-PERFORMING MODEL
Model ID: {lowest_model["ModelID"]}
Algorithm: {lowest_model["Algorithm"]}
Accuracy: {lowest_model["Accuracy"]:.2f}%

MOST IMPROVED MODEL
Model ID: {most_improved_model["ModelID"]}
Algorithm: {most_improved_model["Algorithm"]}
Improvement: {most_improved_model["Improvement"]:.2f} percentage points

BEST ALGORITHM
Algorithm: {best_algorithm["Algorithm"]}
Average accuracy: {best_algorithm["AverageAccuracy"]:.2f}%
"""

    return report.strip()