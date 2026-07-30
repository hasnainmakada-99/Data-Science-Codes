import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dict={
    "StudentID": ["S101", "S102", "S103", "S104", "S105", "S106", "S107", "S108", "S109", "S110"],
    "StudyHours": [12, 8, 10, 15, 6, 7, 14, 9, 11, 13],
    "QuizScore": [85, 65, 78, 92, 55, 60, 88, 72, 80, 95]    
}  # Creating the dataset first

df = pd.DataFrame(dict) # creating the dataframe

df["LogStudyHours"] = np.log(df["StudyHours"]) # adding a new column named LogStudyHours

df['PerformanceLevel'] = pd.cut(df['QuizScore'], bins=[0, 60, 80, 100], labels=["Needs Support", "Progressing", "Excelling"]) # Defining the performance level

print(df) # printing the df


print("correlation matrix") 

print(df[['StudyHours', "QuizScore", 'LogStudyHours']].corr()) # printing the correlation matrix


plt.scatter(df["StudyHours"], df["QuizScore"]) # defining the plot columns, x & y

plt.xlabel("Study Hours")  # label 1

plt.ylabel("Quiz Score") # label 2

plt.title("Study Hours vs Quiz Score") 

plt.show()




#### MENU Driven (Optional One)

while True:
    print("Studen performance analysis menu")
    print('1. original dataset')
    print('2. Show Log_StudyHours feature')
    print('3. Show  Performace Catagories')
    print('4. Display Correlation matrix')
    print('5. Display Scatter Plot')
    print('6. Show Interpreter')
    print('7. Exit')
    
    choice = int(input("Enter your choice\n"))
    
    if(choice ==1):
        print(df[['StudentID','StudyHours', 'QuizScore']])
    elif(choice ==2):
        print(df[['StudentID', 'StudyHours', 'LogStudyHours']])
    elif(choice == 3):
        print(df[['StudentID', 'QuizScore', 'PerformanceLevel']])
    elif(choice == 4):
        print(df[['StudyHours', 'QuizScore', 'LogStudyHours']].corr())
    elif(choice == 5):
        plt.scatter(df['StudyHours'], df['QuizScore'])
        
        plt.xlabel("Study hours")
        plt.ylabel("Quiz Score")
        
        plt.title('Study Hours vs Quiz Score')
        
        plt.show()
        
    elif(choice == 7):
        print('Program Ended')
        break;
    
    else:
        print('Invalid Choice, Please enter a number from 1 to 7')