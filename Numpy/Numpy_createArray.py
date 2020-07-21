import numpy as np

#  array 没有逗号来分隔,  长得和列表很像.
a=np.array([2,23,4])
print(a)

#Type 用dtype标签来表示  我这里默认是int32 可以设置为int64 更精确 占用空间也会更大 ,
# int可以换成float等等. dtpye=np.float
a=np.array([2,23,4],dtype=np.int)
# a=np.array([2,23,4],dtype=np.int64)
print(a.dtype)

# 二维
a=np.array([[1,2,3],
           [4,5,6]])
print(a)

#零矩阵 里面是一个元组, 表示矩阵的行和列.
a=np.zeros((3,4))
print(a)

#一矩阵  可以定义 dtpye  , 有了一矩阵, 就可以定义任意数字的矩阵.
a=np.ones((3,4) ,dtype=np.int16)
print(a)

#empty
b=np.empty((3,4))
print(b)

# 控制 arange
a=np.arange(12).reshape((3,4))
print(a)

# 生成数列段,  从1 到 10  一共 20段
a=np.linspace(1,10,5)
print(a)
a=np.linspace(1,10,6).reshape((2,3))
print(a)