import pandas as pd
import numpy as np
students = [
    ["john", 20 , 85],
    ['mary', 20, 67],
    ['David', 19, 78]
]

df = pd.DataFrame(students, columns = ['Name', "Age", 'Marks'])

# print(df)

single_name = df['Name']
# Row by Label

row_label = df.loc[0];

# print("Row by label ", row_label)


# print(single_name)

# print("Row by Position \n", df.iloc[1])

# print('Shape ',df.shape)
# print('Index ', df.index)
# print('Columns ', df.columns)
# print("Data type ", df.dtypes)
# print("Number of dimensions ", df.ndim)

data = {
    'Name': ['John', 'Mary', "David"],
    'Marks': [85, np.nan, 78]
}

df1 = pd.DataFrame(data)
print(df1)
