import numpy as np
print(np.__version__)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
2.0.0

Process finished with exit code 0
'''
import numpy as np

a = np.array([1, 2, 3])
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[1 2 3]
(3,)
int64
1
3
8

Process finished with exit code 0
'''

import numpy as np

a = np.array([1, 2, 3])
print(a)

print(a[0])
a[0] = 10
print(a)

b = a * np.array([2, 0, 2])
print(b)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[1 2 3]
1
[10  2  3]
[20  0  6]

Process finished with exit code 0
'''

import numpy as np

l = [1, 2, 3]
a = np.array([1, 2, 3])

print(l)
print(a)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[1, 2, 3]
[1 2 3]

Process finished with exit code 0
'''

import numpy as np

l = [1, 2, 3]
a = np.array([1, 2, 3])

l = l + [4]
print(l)
a = a + np.array([4])
print(a)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[1, 2, 3, 4]
[5 6 7]

Process finished with exit code 0
'''

import numpy as np

l = [1, 2, 3]
a = np.array([1, 2, 3])

l = l * 2
print(l)
a = a * 2
print(a)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[1, 2, 3, 1, 2, 3]
[2 4 6]

Process finished with exit code 0
'''

import numpy as np

l = [1, 2, 3]
a = np.array([1, 2, 3])

a = np.sqrt(a)
print(a)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[1.         1.41421356 1.73205081]

Process finished with exit code 0
'''

import numpy as np

l = [1, 2, 3]
a = np.array([1, 2, 3])

a = np.log(a)
print(a)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[0.         0.69314718 1.09861229]

Process finished with exit code 0
'''

import numpy as np

l1 = [1, 2, 3]
l2 = [4, 5, 6]
a = np.array([1, 2, 3])

# dot product
dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
32

Process finished with exit code 0
'''

import numpy as np

l1 = [1, 2, 3]
l2 = [4, 5, 6]
a1 = np.array(l1)
a2 = np.array(l2)

# dot product
dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)

dot = np.dot(a1, a2)
print(dot)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
32
32

Process finished with exit code 0
'''

import numpy as np

l1 = [1, 2, 3]
l2 = [4, 5, 6]
a1 = np.array(l1)
a2 = np.array(l2)

# dot product
dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)

dot = np.dot(a1, a2)
print(dot)

sum1 = a1 * a2
dot = np.sum(sum1)
print(dot)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
32
32
32

Process finished with exit code 0
'''
import numpy as np

l1 = [1, 2, 3]
l2 = [4, 5, 6]
a1 = np.array(l1)
a2 = np.array(l2)

# dot product
dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)

dot = np.dot(a1, a2)
print(dot)

sum1 = a1 * a2
dot = (a1 * a2).sum()
print(dot)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
32
32
32

Process finished with exit code 0
'''

import numpy as np

l1 = [1, 2, 3]
l2 = [4, 5, 6]
a1 = np.array(l1)
a2 = np.array(l2)

# dot product

dot = np.dot(a1, a2)
print(dot)

dot = a1 @ a2
print(dot)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
32
32

Process finished with exit code 0
'''

import numpy as np

# speed test
from timeit import default_timer as timer

a = np.random.randn(1000)
b = np.random.randn(1000)

A = list(a)
B = list(b)

T = 1000


def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i] * B[i]
    return dot


def dot2():
    return np.dot(a, b)


start = timer()
for t in range(T):
    dot1()
end = timer()
t1 = end-start

start = timer()
for t in range(T):
    dot2()
end = timer()
t2 = end-start

print('list calculation', t1)
print('np.dot', t2)
print('ratio', t1/t2)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
list calculation 0.11217439999745693
np.dot 0.002779700000246521
ratio 40.354858433467136

Process finished with exit code 0
'''

import numpy as np

a = np.array([1, 2])
print(a.shape)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
(2,)

Process finished with exit code 0
'''

import numpy as np

a = np.array([[1, 2], [3,4]])
print(a)
print(a.shape)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[[1 2]
 [3 4]]
(2, 2)

Process finished with exit code 0
'''

import numpy as np

a = np.array([[1, 2, 6], [3, 4, 8]])
print(a)
print(a.shape)

print(a[0, :])
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[[1 2 6]
 [3 4 8]]
(2, 3)
[1 2 6]

Process finished with exit code 0
'''

import numpy as np

a = np.array([[1, 2, 6], [3, 4, 8]])
print(a)
print(a.shape)

print(a.T)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[[1 2 6]
 [3 4 8]]
(2, 3)
[[1 3]
 [2 4]
 [6 8]]

Process finished with exit code 0
'''

import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)
print(a.shape)

print(np.linalg.inv(a))
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[[1 2]
 [3 4]]
(2, 2)
[[-2.   1. ]
 [ 1.5 -0.5]]

Process finished with exit code 0
'''

import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)
print(a.shape)

print(np.linalg.det(a))
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[[1 2]
 [3 4]]
(2, 2)
-2.0000000000000004

Process finished with exit code 0
'''

import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)
print(a.shape)

print(np.diag(a))
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[[1 2]
 [3 4]]
(2, 2)
[1 4]

Process finished with exit code 0
'''

import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)
print(a.shape)

c = np.diag(a)
print(np.diag(c))
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[[1 2]
 [3 4]]
(2, 2)
[[1 0]
 [0 4]]

Process finished with exit code 0
'''

import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)

b = a[0, 1]
print(b)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[[1 2]
 [3 4]]
2

Process finished with exit code 0
'''

import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a)

b = a[0, 1:3]
print(b)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[[1 2 3 4]
 [5 6 7 8]]
[2 3]

Process finished with exit code 0
'''

import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a)

b = a[:, 1]
print(b)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[[1 2 3 4]
 [5 6 7 8]]
[2 6]

Process finished with exit code 0
'''

import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a)

b = a[-1, -1]
print(b)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[[1 2 3 4]
 [5 6 7 8]]
8

Process finished with exit code 0
'''

import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)

bool_idx = a > 2
print(bool_idx)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[[1 2]
 [3 4]
 [5 6]]
[[False False]
 [ True  True]
 [ True  True]]

Process finished with exit code 0
'''
import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)

bool_idx = a > 2
print(bool_idx)
print(a[bool_idx])
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[[1 2]
 [3 4]
 [5 6]]
[[False False]
 [ True  True]
 [ True  True]]
[3 4 5 6]

Process finished with exit code 0
'''

import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)

print(a > 2)
'''
D:\python\.venv\Scripts\python.exe D:\python\main.py 
[[1 2]
 [3 4]
 [5 6]]
[[False False]
 [ True  True]
 [ True  True]]

Process finished with exit code 0
'''













