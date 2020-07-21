import pandas as pd #加载模块

#读取csv 是excel的最简单的格式.
data = pd.read_csv('student.csv')

#打印出data
print(data)

#将资料存取成pickle ¶
data.to_pickle('student.pickle')

