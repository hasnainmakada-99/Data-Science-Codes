import pandas as pd
import streamlit as st

from analysis_core import (
    analyse_models,
    clean_data,
    create_algorithm_summary,
    create_report,
    create_sample_data,
    perform_basic_operations
)


# ============================================================
# PAGE SETTINGS
# These settings control the Streamlit browser page.
# ============================================================
st.set_page_config(
    page_title="AI Model Evaluation Dashboard",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# PAGE TITLE
# ============================================================
st.title("🤖 AI Model Evaluation Dashboard")

st.write(
    "Analyse, rank and compare machine learning models "
    "using Pandas and Streamlit."
)


# ============================================================
# SIDEBAR CONTROLS
# ============================================================
st.sidebar.header("Dashboard Controls")

data_source = st.sidebar.radio(
    "Choose data source",
    ["Use sample data", "Upload CSV"]
)


# ============================================================
# LOAD DATA
# ============================================================
if data_source == "Upload CSV":
    uploaded_file = st.sidebar.file_uploader(
        "Upload AI model CSV",
        type=["csv"]
    )

    if uploaded_file is None:
        st.info("Upload a CSV file to continue.")
        st.stop()

    try:
        raw_data = pd.read_csv(uploaded_file)
    except Exception as error:
        st.error(f"Could not read the CSV file: {error}")
        st.stop()

else:
    raw_data = create_sample_data()


# ============================================================
# CLEAN DATA
# ============================================================
try:
    cleaned_data = clean_data(raw_data)
except ValueError as error:
    st.error(str(error))
    st.stop()

if cleaned_data.empty:
    st.error("No valid model records are available.")
    st.stop()


# ============================================================
# ANALYSIS SETTINGS
# ============================================================
production_threshold = st.sidebar.slider(
    "Production-ready threshold",
    min_value=0.0,
    max_value=100.0,
    value=90.0,
    step=0.5
)

analysed_data = analyse_models(
    cleaned_data,
    production_threshold
)

available_algorithms = sorted(
    analysed_data["Algorithm"].unique().tolist()
)

selected_algorithms = st.sidebar.multiselect(
    "Select algorithms",
    options=available_algorithms,
    default=available_algorithms
)

minimum_accuracy = st.sidebar.slider(
    "Minimum displayed accuracy",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=0.5
)


# ============================================================
# FILTER DATA
# ============================================================
filtered_data = analysed_data[
    analysed_data["Algorithm"].isin(selected_algorithms)
    & (analysed_data["Accuracy"] >= minimum_accuracy)
].copy()

filtered_data = filtered_data.sort_values(
    by="Accuracy",
    ascending=False
).reset_index(drop=True)

filtered_data["Rank"] = range(
    1,
    len(filtered_data) + 1
)

if filtered_data.empty:
    st.warning("No models match the selected filters.")
    st.stop()


# ============================================================
# DASHBOARD METRICS
# ============================================================
average_accuracy = filtered_data["Accuracy"].mean()
best_model = filtered_data.iloc[0]

production_ready_count = (
    filtered_data["Status"] == "Production Ready"
).sum()

metric_1, metric_2, metric_3, metric_4 = st.columns(4)

metric_1.metric(
    "Models Analysed",
    len(filtered_data),
    border=True
)

metric_2.metric(
    "Average Accuracy",
    f"{average_accuracy:.2f}%",
    border=True
)

metric_3.metric(
    "Best Model",
    best_model["ModelID"],
    delta=f'{best_model["Accuracy"]:.2f}% accuracy',
    border=True
)

metric_4.metric(
    "Production Ready",
    int(production_ready_count),
    border=True
)


# ============================================================
# DASHBOARD TABS
# ============================================================
(
    basic_tab,
    ranking_tab,
    algorithm_tab,
    improvement_tab,
    report_tab,
    data_tab
) = st.tabs(
    [
        "Basic Operations",
        "Model Rankings",
        "Algorithm Comparison",
        "Improvement Tracking",
        "Automated Report",
        "Complete Data"
    ]
)


# ============================================================
# TAB 1: BASIC OPERATIONS
# ============================================================
with basic_tab:
    results = perform_basic_operations(
        filtered_data
    )

    st.subheader("1. Select ModelID and Accuracy")

    st.dataframe(
        results["selected_columns"],
        hide_index=True
    )

    st.code(
        'selected_columns = data[["ModelID", "Accuracy"]]',
        language="python"
    )

    st.subheader(
        "2. Filter Models with Accuracy Greater Than 90%"
    )

    st.dataframe(
        results["models_above_90"][
            ["ModelID", "Algorithm", "Accuracy"]
        ],
        hide_index=True
    )

    st.code(
        'models_above_90 = data[data["Accuracy"] > 90]',
        language="python"
    )

    st.subheader(
        '3. Add Status with Default "Production Ready"'
    )

    st.dataframe(
        results["status_table"],
        hide_index=True
    )

    st.code(
        'data["Status"] = "Production Ready"',
        language="python"
    )

    st.subheader("4. Sort Models by Accuracy")

    st.dataframe(
        results["sorted_models"][
            ["ModelID", "Algorithm", "Accuracy"]
        ],
        hide_index=True
    )

    st.code(
        'sorted_models = data.sort_values('
        'by="Accuracy", ascending=False)',
        language="python"
    )

    st.subheader("5. Calculate Average Model Accuracy")

    st.success(
        f'{results["average_accuracy"]:.2f}%'
    )

    st.code(
        'average_accuracy = data["Accuracy"].mean()',
        language="python"
    )


# ============================================================
# TAB 2: MODEL RANKINGS
# ============================================================
with ranking_tab:
    st.dataframe(
        filtered_data[
            [
                "Rank",
                "ModelID",
                "Algorithm",
                "PreviousAccuracy",
                "Accuracy",
                "Improvement",
                "Status"
            ]
        ],
        hide_index=True
    )

    chart_data = filtered_data[
        ["ModelID", "Accuracy"]
    ].set_index("ModelID")

    st.bar_chart(chart_data)


# ============================================================
# TAB 3: ALGORITHM COMPARISON
# ============================================================
with algorithm_tab:
    algorithm_summary = create_algorithm_summary(
        filtered_data
    )

    st.dataframe(
        algorithm_summary,
        hide_index=True
    )

    chart_data = algorithm_summary[
        ["Algorithm", "AverageAccuracy"]
    ].set_index("Algorithm")

    st.bar_chart(chart_data)


# ============================================================
# TAB 4: IMPROVEMENT TRACKING
# ============================================================
with improvement_tab:
    st.dataframe(
        filtered_data[
            [
                "ModelID",
                "Algorithm",
                "PreviousAccuracy",
                "Accuracy",
                "Improvement",
                "ImprovementStatus"
            ]
        ],
        hide_index=True
    )

    comparison_data = filtered_data[
        [
            "ModelID",
            "PreviousAccuracy",
            "Accuracy"
        ]
    ].set_index("ModelID")

    st.line_chart(comparison_data)

    improvement_data = filtered_data[
        ["ModelID", "Improvement"]
    ].set_index("ModelID")

    st.bar_chart(improvement_data)


# ============================================================
# TAB 5: AUTOMATED REPORT
# ============================================================
with report_tab:
    report = create_report(
        filtered_data,
        production_threshold
    )

    st.text(report)

    st.download_button(
        "Download Evaluation Report",
        data=report,
        file_name="ai_model_evaluation_report.txt",
        mime="text/plain"
    )

    st.download_button(
        "Download Analysed CSV",
        data=filtered_data.to_csv(index=False),
        file_name="analysed_ai_models.csv",
        mime="text/csv"
    )


# ============================================================
# TAB 6: COMPLETE DATA
# ============================================================
with data_tab:
    st.dataframe(
        filtered_data,
        hide_index=True
    )

    st.write(
        f"Rows: {filtered_data.shape[0]}"
    )

    st.write(
        f"Columns: {filtered_data.shape[1]}"
    )

    st.write(
        f"Algorithms: "
        f"{filtered_data['Algorithm'].nunique()}"
    )