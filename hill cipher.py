
import numpy as np

A = np.array([[1, 2, 1], [2, 5, 3], [2, 3, 2]])
B = np.array([[19, 4, 14], [5, 13, 5], [14, 15, 25]])
C = np.mat(A) *np.mat(B)
print("矩阵A乘矩阵B的结果：")
print(C)
Reverse_A = np.linalg.inv(A)
print("矩阵A逆为：")
print(Reverse_A)
ans = np.mat(Reverse_A) *np.mat(C)
print("解密完成之后：")
print(ans)

