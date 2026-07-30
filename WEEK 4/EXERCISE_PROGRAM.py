import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def print_heading(title):
    print("\n" + "=" * 100)
    print(title)
    print("=" * 100)


# 1. Workforce dataset stored locally as a Python dictionary.
employee_data = {
    "OvertimeHours": [5, 12, 18, 26, 8, 32, 15, 28, 10, 24, 35, 6, 20, 34, 38],
    "JobSatisfactionScore": [5, 4, 3, 2, 4, 1, 3, 2, 5, 2, 1, 4, 3, 3, 2],
    "SalaryLevel": [5, 4, 3, 2, 4, 1, 3, 2, 5, 4, 1, 4, 3, 2, 2],
    "TrainingHours": [40, 35, 28, 16, 34, 10, 24, 18, 45, 30, 8, 38, 26, 12, 14],
    "WorkLifeBalance": [5, 4, 3, 2, 4, 1, 3, 2, 5, 3, 1, 4, 3, 2, 2],
    "YearsAtCompany": [10, 7, 5, 2, 8, 1, 4, 3, 11, 6, 1, 9, 6, 2, 2],
    "PromotionCount": [3, 2, 1, 0, 2, 0, 1, 0, 3, 1, 0, 2, 1, 0, 0],
    "AttritionStatus": [
        "No", "No", "No", "Yes", "No", "Yes", "No", "Yes",
        "No", "No", "Yes", "No", "No", "Yes", "Yes"
    ]
}

# 2. Create and display the DataFrame.
df = pd.DataFrame(employee_data)
df.index = range(1, len(df) + 1)
df.index.name = "Employee"

print_heading("ORIGINAL WORKFORCE DATAFRAME")
print(df.to_string())
print("\nDataFrame Shape:", df.shape)

# 3. Feature engineering and workforce segmentation.
df["Log_OvertimeHours"] = np.log(df["OvertimeHours"]).round(3)
df["EmployeeCategory"] = pd.cut(
    df["JobSatisfactionScore"],
    bins=[0, 2, 3, 5],
    labels=["Disengaged", "Satisfied", "Highly Engaged"],
    include_lowest=True
)
df["AttritionFlag"] = df["AttritionStatus"].map({"No": 0, "Yes": 1})

print_heading("FEATURE ENGINEERING AND EMPLOYEE SEGMENTATION")
print(df[[
    "OvertimeHours", "Log_OvertimeHours", "JobSatisfactionScore",
    "EmployeeCategory", "AttritionStatus"
]].to_string())

# 4. Correlation analysis.
numeric_columns = [
    "OvertimeHours", "JobSatisfactionScore", "SalaryLevel",
    "TrainingHours", "WorkLifeBalance", "YearsAtCompany",
    "PromotionCount", "Log_OvertimeHours", "AttritionFlag"
]
correlation_matrix = df[numeric_columns].corr()

print_heading("CORRELATION MATRIX")
print(correlation_matrix.round(3).to_string())

# 5. Workforce trend analysis.
overall_attrition_rate = df["AttritionFlag"].mean() * 100
category_summary = (
    df.groupby("EmployeeCategory", observed=False)
    .agg(
        EmployeeCount=("AttritionFlag", "size"),
        AttritionCount=("AttritionFlag", "sum"),
        AverageOvertime=("OvertimeHours", "mean"),
        AverageSalaryLevel=("SalaryLevel", "mean")
    )
    .reset_index()
)
category_summary["AttritionRatePercent"] = (
    category_summary["AttritionCount"]
    / category_summary["EmployeeCount"] * 100
).round(2)
category_summary["AverageOvertime"] = category_summary["AverageOvertime"].round(2)
category_summary["AverageSalaryLevel"] = category_summary["AverageSalaryLevel"].round(2)

status_summary = df.groupby("AttritionStatus")[[
    "OvertimeHours", "JobSatisfactionScore", "SalaryLevel",
    "TrainingHours", "WorkLifeBalance", "YearsAtCompany",
    "PromotionCount"
]].mean().round(2)

print_heading("WORKFORCE TREND ANALYSIS")
print("Overall Attrition Rate: {:.2f}%".format(overall_attrition_rate))
print("\nEmployee Category Summary")
print(category_summary.to_string(index=False))
print("\nAverage Workforce Indicators by Attrition Status")
print(status_summary.to_string())

# 6. Rule-based attrition risk analysis.
df["RiskScore"] = (
    (df["OvertimeHours"] >= 25).astype(int)
    + (df["JobSatisfactionScore"] <= 2).astype(int)
    + (df["SalaryLevel"] <= 2).astype(int)
    + (df["WorkLifeBalance"] <= 2).astype(int)
    + (df["PromotionCount"] == 0).astype(int)
)
df["AttritionRisk"] = pd.cut(
    df["RiskScore"], bins=[-1, 1, 4, 5], labels=["Low", "Medium", "High"]
)
high_risk_employees = df[df["AttritionRisk"] == "High"][[
    "OvertimeHours", "JobSatisfactionScore", "SalaryLevel",
    "WorkLifeBalance", "PromotionCount", "RiskScore",
    "AttritionRisk", "AttritionStatus"
]]

print_heading("ATTRITION RISK ANALYSIS")
print("Risk Category Distribution")
print(df["AttritionRisk"].value_counts().sort_index().to_string())
print("\nHigh-Risk Employees")
print(high_risk_employees.to_string())

# 7. Treemap visualization using proportional Matplotlib rectangles.
total_employees = category_summary["EmployeeCount"].sum()
fig, ax = plt.subplots(figsize=(11, 6))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
x_position = 0.0
grayscale_colors = ["#2F2F2F", "#555555", "#7A7A7A"]

for index, row in category_summary.iterrows():
    width = row["EmployeeCount"] / total_employees
    ax.add_patch(Rectangle(
        (x_position, 0), width, 1,
        facecolor=grayscale_colors[index], edgecolor="white", linewidth=2
    ))
    label = (
        f'{row["EmployeeCategory"]}\n'
        f'Employees: {int(row["EmployeeCount"])}\n'
        f'Attrition Rate: {row["AttritionRatePercent"]:.1f}%'
    )
    ax.text(
        x_position + width / 2, 0.5, label,
        color="white", ha="center", va="center",
        fontsize=12, fontweight="bold"
    )
    x_position += width

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
ax.set_title(
    "Treemap of Employee Engagement Categories",
    color="white", fontsize=16, fontweight="bold", pad=18
)
plt.tight_layout()
plt.savefig(
    "hr_employee_category_treemap.png",
    dpi=300, facecolor="black", bbox_inches="tight"
)
plt.show()

# 8. Final interpretation.
attrition_correlations = (
    correlation_matrix["AttritionFlag"]
    .drop("AttritionFlag")
    .sort_values(ascending=False)
)

print_heading("FINAL WORKFORCE INSIGHTS")
print("Correlation of Workforce Indicators with Attrition")
print(attrition_correlations.round(3).to_string())
print("\nInterpretation:")
print(
    "1. Higher overtime is associated with greater attrition risk.\n"
    "2. Lower job satisfaction, salary level, work-life balance, training,\n"
    "   tenure, and promotion opportunities are associated with attrition.\n"
    "3. Disengaged employees show the highest attrition rate.\n"
    "4. Retention strategies should prioritize workload control, employee\n"
    "   engagement, career growth, training, and work-life balance."
)