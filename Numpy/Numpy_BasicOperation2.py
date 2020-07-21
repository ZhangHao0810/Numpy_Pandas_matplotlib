import numpy as np

A = np.arange(2, 14).reshape((3, 4))
print(A)

# 输出最小值索引
print(np.argmin(A))
# 最大值索引
print(np.argmax(A))
# 矩阵平均值
# print(np.mean(A))
print(A.mean())  # 方法有这样的两种调用形式.
print(np.average(A))
# 中位数
print(np.median(A))
# 累加  返回[(矩阵每个位置)和(他之前的所有数)的和]. 返回一个列表.
print(np.cumsum(A))
# 累差 返回二维数组
print(np.diff(A))
# 找非零的数  返回两个列表来表示位置, 第一个表示行, 第二个表示列,
print(np.nonzero(A))
# 排序 默认从小到大
print(np.sort(A))
# 矩阵的转置
print(np.transpose(A))
print(A.T)
# 矩阵的乘法, 矩阵的转置乘以矩阵
print((A.T).dot(A))

# 让A中 所有小于5 的数 都等于5 . 所有大于9的数, 都等于9
print(np.clip(A, 5, 9))

# 基本上Numpy 的每个函数都可以指定 aixs = 0 / 1  指定对于列计算还是对行计算.
print(np.mean(A, axis=1))
