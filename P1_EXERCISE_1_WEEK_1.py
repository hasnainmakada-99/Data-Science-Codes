# Load Necessary Packages
import pandas as pd

# Step 1: Create Dataset
dataframe1 = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [23, 30, 28, 35, 22],
    "City": ["New York", "London", "Paris", "Tokyo", "Sydney"]
}

# Step 2: Create DataFrame
df = pd.DataFrame(dataframe1)

print("Original DataFrame")
print(df)
print()

# Step 3: Select Name and Age Columns
name_age = df[["Name", "Age"]]

print("Name and Age")
print(name_age)
print()

# Step 4: Filter Rows where Age > 25
filtered_df = df[df["Age"] > 25]

print("Age > 25")
print(filtered_df)
print()

# Step 5: Add Country Column
df["Country"] = "India"

print("Country Added")
print(df)
print()

# Step 6: Sort by Age in Descending Order
sorted_df = df.sort_values(by="Age", ascending=False)

print("Sorted Data")
print(sorted_df)
print()

# Step 7: Calculate Mean Age
mean_df = df["Age"].mean()

print("Mean Age")
print(mean_df)