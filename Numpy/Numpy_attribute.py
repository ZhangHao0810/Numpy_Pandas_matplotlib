import numpy as np
#列表转化为矩阵
array = np.array([[1,2,3],
                 [2,3,4]])
print(array)

#输出维度
print('number of dim:', array.ndim)
#输出形状(行,列)
print("shape",array.shape)
#总共有多少元素
print("size:",array.size)