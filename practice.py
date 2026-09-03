import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# np.random().seed(42)

dictionary = {
    "Feature 1": np.random.randint(1, 100, 20),
    "Feature 2": np.random.randint(100, 200, 20),
    "Feature 3": np.random.randint(0, 2, 20)
}

dataFrame = pd.DataFrame(dictionary)

dataFrame['Log_Feature1'] = np.log( , dataFrame['Log_Feature1']) 

dataFrame['Feature2_Catafory'] = pd.cut( dataFrame[Feature2], bins = 3, labels = ['Low', 'Medium', 'High'])

corr_matrix = dataFrame['Feature 1', 'Feature 2', 'Target', "Log_Feature1"].corr()

print(corr_matrix)

plt.scatter(dataFrame['Feature 1'], dataFrame['Feature2'], c=dataFrame["Target"], cmap='virdis', s=100)

plt.xlabel('Feature 1')
plt.ylabel("Feature 2")

plt.show()





print("Data Frame: ", dataFrame)
# print(np.random.randint(1,100,5))
