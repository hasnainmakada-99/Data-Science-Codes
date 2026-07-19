# Import the required libraries
import pandas as pd
import numpy as np

# Step 1: Create a personalized dataset with missing values
student_data = [
    ["Hasnain Makada", 20, "Delhi"],
    ["Tim", np.nan, "Mumbai"],
    [np.nan, 25, "Pune"],
    ["Cook", 30, np.nan],
    ["Nolan", np.nan, "Chennai"],
        ["Heisenberg", 35, "Delhi"],
    ["True Detective", 40, "Jaipur"],
    ["Casio", 45, "Surat"],
    ["MSI", 50, np.nan]
]

# Step 2: Convert the dataset into a DataFrame
student_df = pd.DataFrame(student_data, columns=["Name", "Age", "City"])

# Display the original DataFrame
print("Original DataFrame")
print(student_df)

# Step 3: Calculate the mean age
mean_age = student_df["Age"].mean()

# Fill missing values in the Age column with the mean age
student_df["Age"] = student_df["Age"].fillna(mean_age)
print("\nAfter filling missing Age values")
print(student_df)

# Step 4: Drop rows where Name or City is missing
student_df = student_df.dropna(subset=["Name", "City"]).copy()
print("\nAfter dropping rows with missing Name or City")
print(student_df)

# Step 5: Convert the Age column to integer type
student_df["Age"] = student_df["Age"].astype(int)
print("\nAfter converting Age to integer")
print(student_df)

# Step 6: Normalize the Age column using Min-Max Scaling
min_age = student_df["Age"].min()
max_age = student_df["Age"].max()

student_df["Normalized_Age"] = (
    (student_df["Age"] - min_age) / (max_age - min_age)
)

# Display the final DataFrame
print("\nFinal cleaned and normalized DataFrame")
print(student_df)
