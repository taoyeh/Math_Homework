import numpy as np

L = np.array([[1, 0.5, 0], [0, 0.5, 1], [0, 0, 0]])
a, p = np.linalg.eig(L)
print('打印特征值a：\n{}'.format(a))
print('打印特征向量b：\n{}'.format(p))
a=np.array([[1, 0, 0], [0, 0.5, 0], [0, 0, 0]])
Reverse_p = np.linalg.inv(p)
print("n为1时")
c=np.mat(p) *np.mat(a)*np.mat(Reverse_p)
print(c)
for i in range(3):
    a=np.mat(a)*np.mat(a)
print("n为8时")
c=np.mat(p) *np.mat(a)*np.mat(Reverse_p)
print(c)

print("n为16时")
c=np.mat(p) *np.mat(a)*np.mat(a)*np.mat(Reverse_p)
print(c)


