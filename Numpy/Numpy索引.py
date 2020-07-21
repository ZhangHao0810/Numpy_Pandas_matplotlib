import numpy as np

A = np.arange(3, 15)
print(A)

print(A[3])

# 矩阵形式
A = np.arange(3, 15).reshape((3, 4))
print(A)
print(A[2])
print(A[1][1])
# 新的写法
print(A[1, 1])
# 用 :  表示所有数
print(A[2, :])
print(A[:, 1])
# 第一行 从第一列到第二列.( : 是左开右闭的)
print(A[1, 1:2])

# 循环
for row in A:
    print(row) # 迭代的是每一行

for col in A.T:
    print(col) # 迭代列 输出的是每一列  通过转置矩阵来实现.

# 将二维数组转为一维
print(A.flatten())
for item in A.flat:
    print(item)  # 迭代每一个元素.
