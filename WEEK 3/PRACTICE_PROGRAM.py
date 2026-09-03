import numpy as np


# ------------------------------------------------------------
# 1. CREATE PREDEFINED DATA IN DICTIONARY FORMAT
# ------------------------------------------------------------
array_data = {
    "Array1": [
        [2, 5, 7, 1],
        [8, 3, 6, 4],
        [9, 0, 5, 2]
    ],

    "Array2": [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [2, 3, 4]
    ]
}


# ------------------------------------------------------------
# 2. CONVERT DICTIONARY VALUES INTO NUMPY ARRAYS
# ------------------------------------------------------------
array1 = np.array(array_data["Array1"])

array2 = np.array(array_data["Array2"])


# ------------------------------------------------------------
# 3. DISPLAY ORIGINAL ARRAY
# ------------------------------------------------------------
print("\nORIGINAL 2D ARRAY")
print("=" * 50)

print(array1)

print("\nShape of Array:", array1.shape)


# ------------------------------------------------------------
# 4. CALCULATE MEAN OF THE ENTIRE ARRAY
# ------------------------------------------------------------
mean_value = np.mean(array1)

print("\nMEAN OF THE ENTIRE ARRAY")
print("=" * 50)

print("Mean:", round(mean_value, 2))


# ------------------------------------------------------------
# 5. CALCULATE STANDARD DEVIATION
# ------------------------------------------------------------
standard_deviation = np.std(array1)

print("\nSTANDARD DEVIATION OF THE ENTIRE ARRAY")
print("=" * 50)

print(
    "Standard Deviation:",
    round(standard_deviation, 2)
)


# ------------------------------------------------------------
# 6. SLICE FIRST TWO ROWS AND LAST TWO COLUMNS
# ------------------------------------------------------------
sliced_array = array1[:2, -2:]

print("\nFIRST TWO ROWS AND LAST TWO COLUMNS")
print("=" * 50)

print(sliced_array)


# ------------------------------------------------------------
# 7. RESHAPE ARRAY FROM (3, 4) TO (4, 3)
# ------------------------------------------------------------
reshaped_array = array1.reshape(4, 3)

print("\nRESHAPED ARRAY")
print("=" * 50)

print(reshaped_array)

print(
    "\nShape After Reshaping:",
    reshaped_array.shape
)


# ------------------------------------------------------------
# 8. DISPLAY SECOND ARRAY
# ------------------------------------------------------------
print("\nSECOND ARRAY")
print("=" * 50)

print(array2)

print("\nShape of Second Array:", array2.shape)


# ------------------------------------------------------------
# 9. PERFORM ELEMENT-WISE MULTIPLICATION
# ------------------------------------------------------------
multiplied_array = reshaped_array * array2

print("\nELEMENT-WISE MULTIPLICATION")
print("=" * 50)

print(multiplied_array)


# ------------------------------------------------------------
# 10. DISPLAY FINAL SUMMARY
# ------------------------------------------------------------
print("\nFINAL SUMMARY")
print("=" * 50)

print("Original Array Shape:", array1.shape)

print("Mean:", round(mean_value, 2))

print(
    "Standard Deviation:",
    round(standard_deviation, 2)
)

print(
    "Sliced Array Shape:",
    sliced_array.shape
)

print(
    "Reshaped Array Shape:",
    reshaped_array.shape
)

print(
    "Multiplied Array Shape:",
    multiplied_array.shape
)