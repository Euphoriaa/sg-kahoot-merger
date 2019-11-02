import pandas as pd
data = pd.read_csv("Lecture 1.csv")
data = data.iloc[2:,1]
data = data.dropna()
print(data)
print(data.iloc[:10])
data = data.reset_index(drop = True)
print(data)
data2 = pd.read_csv("Lecture 1.csv")
data2 = data2.iloc[2:,1:5]
data2 = data2.dropna()
data2.columns =['Students','Total Score','Correct Answers','Incorrect Answers']
data2.to_csv("clean_lecture_1.csv",index=False)

print(data2)