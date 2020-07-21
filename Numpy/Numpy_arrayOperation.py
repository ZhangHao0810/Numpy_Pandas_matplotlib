import numpy as np

"""array 的合并 """
A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

# 上下合并 vertical stack 两个一维 合并 成 一个二维
print(np.vstack((A, B)))

# 左右合并 horizontal stack 两个一维, 合并成 一个长的一维. 两个列同理.
print(np.hstack((A, B)))

"""一行array 变成 一列."""

print(A.T)  # 不能将序列转为竖着的一列.
print(A[np.newaxis, :])  # 对A 在行这方面加了一个维度.
print(A[:, np.newaxis])  # 对A 在列这方面加了一个维度.

A = np.array([1, 1, 1])[:, np.newaxis]  # 变成一列了.
B = np.array([2, 2, 2])[:, np.newaxis]  # 变成一列了.

print(A)
print(B)

# 指定 多个array 的纵向和横向的合并. 用axis 来定义.
C = np.concatenate((A, B, B, A), axis=1)
print(C)

"""array的分割."""
A = np.arange(12).reshape(3, 4)
print(A)

# 按照列来分割, 两列为一组.  但是只能是等量的分割. axis=1 按列割 axis=0 按行割
print(np.split(A, 2, axis=1))
# 不等量的分割
print(np.array_split(A, 3, axis=1))

# 横向分割 分三块
print(np.vsplit(A, 3))
# 竖向分割 分两块
print(np.hsplit(A, 2))

"""深拷贝和浅拷贝"""
a = np.array([1, 2, 3])
b = a # 浅拷贝 引用指向同一个地址.
b is a  # 返回 True or  False , True 表示两个引用到同一个地址.

b=a.copy() # deep copy 只是单纯的copy值  这才是深拷贝.