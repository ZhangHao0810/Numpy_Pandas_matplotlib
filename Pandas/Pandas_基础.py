import pandas as pd
import numpy as np

# nan 表示 空 ,NaN=none=Null
s=pd.Series([1,3,6,np.nan,44,1])
print(s)
"""
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
"""

#时间
dates=pd.date_range("20200206",periods=6)
print(dates)
"""
DatetimeIndex(['2020-02-06', '2020-02-07', '2020-02-08', '2020-02-09',
               '2020-02-10', '2020-02-11'],
              dtype='datetime64[ns]', freq='D')
"""



#格式化的 有名称的数据,  用 dates 定义行, 用 a b c d 来定义列.
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=["a",'b','c','d'])
print(df)
"""
                   a         b         c         d
2020-02-06 -2.026973  1.012125  0.965313 -1.846251
2020-02-07 -1.009839  0.677838  0.449233 -1.298469
2020-02-08  0.860675 -2.226091  1.343647 -0.638151
2020-02-09 -0.066648  0.617012 -1.317622  0.509106
2020-02-10  0.039526 -1.941651  0.003818 -0.410602
2020-02-11 -0.638393  1.534503 -1.290398 -0.137768
"""

# 默认情况下, 是用索引俩做为行列名的.
df1=pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)
"""
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
"""

#用字典的形式来定义数据
df2=pd.DataFrame({'A':1,
                  'B':np.array([3]*4),
                  'C':'foo',
                  'D': 6})
print(df2)
"""
   A  B    C  D
0  1  3  foo  6
1  1  3  foo  6
2  1  3  foo  6
3  1  3  foo  6
"""
print(df2.dtypes)
"""
A     int64
B     int32
C    object
D     int64
dtype: object
"""
print(df2.index)
"""RangeIndex(start=0, stop=4, step=1)"""
print(df2.columns) #打印列的名字
'''Index(['A', 'B', 'C', 'D'], dtype='object')'''
print(df2.values)
"""
[[1 3 'foo' 6]
 [1 3 'foo' 6]
 [1 3 'foo' 6]
 [1 3 'foo' 6]]
"""
print(df2.describe()) # 只能描述 数字类型的数据, 比如C列 就会自动省略了.
"""
         A    B    D
count  4.0  4.0  4.0
mean   1.0  3.0  6.0
std    0.0  0.0  0.0
min    1.0  3.0  6.0
25%    1.0  3.0  6.0
50%    1.0  3.0  6.0
75%    1.0  3.0  6.0
max    1.0  3.0  6.0
"""
print(df2.T) # 转置
"""
     0    1    2    3
A    1    1    1    1
B    3    3    3    3
C  foo  foo  foo  foo
D    6    6    6    6
"""
print(df2.sort_index(axis=1,ascending=False)) #按照列名 倒着排序
'''
   D    C  B  A
0  6  foo  3  1
1  6  foo  3  1
2  6  foo  3  1
3  6  foo  3  1
'''
print(df2.sort_values(by="A")) # 按照某一列的值进行排序.