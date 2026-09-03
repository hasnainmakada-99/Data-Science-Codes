import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 1. CREATE DATASET IN DICTIONARY FORMAT
# ------------------------------------------------------------
data = {
    "Feature1": [
        5, 8, 12, 15, 18,
        22, 25, 30, 35, 40,
        45, 50, 55, 60, 70
    ],

    "Feature2": [
        10, 18, 15, 25, 30,
        28, 35, 40, 38, 45,
        50, 55, 60, 65, 75
    ],

    "Target": [
        0, 0, 1, 0, 1,
        1, 0, 1, 1, 0,
        1, 1, 0, 1, 1
    ]
}


# ------------------------------------------------------------
# 2. CONVERT DICTIONARY INTO DATAFRAME
# ------------------------------------------------------------
df = pd.DataFrame(data)

print("\nORIGINAL DATAFRAME")
print("=" * 60)
print(df)


# ------------------------------------------------------------
# 3. CREATE LOGARITHMIC FEATURE FROM FEATURE1
# ------------------------------------------------------------
df["Log_Feature1"] = np.log(df["Feature1"])

print("\nDATAFRAME AFTER CREATING LOG FEATURE")
print("=" * 60)
print(df)


# ------------------------------------------------------------
# 4. BIN FEATURE2 INTO LOW, MEDIUM AND HIGH CATEGORIES
# ------------------------------------------------------------
df["Feature2_Category"] = pd.cut(
    df["Feature2"],
    bins=3,
    labels=["Low", "Medium", "High"]
)

print("\nDATAFRAME AFTER BINNING FEATURE2")
print("=" * 60)
print(df)


# ------------------------------------------------------------
# 5. CALCULATE CORRELATION MATRIX
# Only numeric columns are included.
# ------------------------------------------------------------
correlation_matrix = df[
    ["Feature1", "Feature2", "Target", "Log_Feature1"]
].corr()

print("\nCORRELATION MATRIX")
print("=" * 60)
print(correlation_matrix.round(3))


# ------------------------------------------------------------
# 6. DISPLAY CATEGORY-WISE COUNT
# ------------------------------------------------------------
category_count = df["Feature2_Category"].value_counts().sort_index()

print("\nFEATURE2 CATEGORY COUNT")
print("=" * 60)
print(category_count)


# ------------------------------------------------------------
# 7. CREATE SCATTER PLOT
# Feature1 is shown on the X-axis.
# Feature2 is shown on the Y-axis.
# Point colour represents Target.
# ------------------------------------------------------------
plt.figure(figsize=(8, 6))

scatter_plot = plt.scatter(
    df["Feature1"],
    df["Feature2"],
    c=df["Target"],
    s=100,
    edgecolors="black"
)

plt.title("Feature1 vs Feature2 Coloured by Target")
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.grid(True, alpha=0.3)

legend = plt.legend(
    *scatter_plot.legend_elements(),
    title="Target"
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 8. INTERPRET VISIBLE PATTERNS
# ------------------------------------------------------------
feature_correlation = df["Feature1"].corr(df["Feature2"])

print("\nPATTERN INTERPRETATION")
print("=" * 60)

print(
    "Correlation between Feature1 and Feature2:",
    round(feature_correlation, 3)
)

if feature_correlation > 0.7:
    print(
        "Feature1 and Feature2 show a strong positive relationship. "
        "As Feature1 increases, Feature2 generally increases."
    )

elif feature_correlation > 0.3:
    print(
        "Feature1 and Feature2 show a moderate positive relationship."
    )

elif feature_correlation < -0.7:
    print(
        "Feature1 and Feature2 show a strong negative relationship."
    )

elif feature_correlation < -0.3:
    print(
        "Feature1 and Feature2 show a moderate negative relationship."
    )

else:
    print(
        "Feature1 and Feature2 show a weak relationship."
    )

print(
    "The scatter plot also shows how Target values are distributed "
    "across different combinations of Feature1 and Feature2."
)