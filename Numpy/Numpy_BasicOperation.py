import numpy as np

'''Numpy 的基础运算'''

a = np.array([10, 20, 30, 40])
b = np.arange(4)
print(a,b)

#加减法 和数学的一致.
c=a-b
print(c)

# Python中的 平方用 ** 来表示
c=b**2
print(c)

#三角函数运算  都有 sin  cos tan 等等
c=10*np.sin(a)
print(c)

# 判断值的大小关系 输出布尔值.
print(b)
print(b<3)
print(b==3)

# 矩阵运算.
a=np.array([[1,2],
           [0,1]])
b=np.arange(4).reshape((2,2))
print(a)
print(b)

# 乘法:
# 依次相乘
c=a*b
print(c)
# 矩阵乘法  (机器学习, 图像等的都需要.)
c_dot=np.dot(a,b)
c_dot_2=a.dot(b)
print(c_dot)
print(c_dot_2)

#随机生成Array  注意 是random模块下的random函数.  有两个random
a= np.random.random((2,4))
print(a)
print(np.sum(a))
print(np.min(a))
print(np.max(a))
#axis  0=在列中求. 1=在行中求,
print(np.sum(a,axis=1))
