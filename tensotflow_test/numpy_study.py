#Load library
import cv2
import numpy as np

"""
#Create a vector as a row
vector_row = np.array([1, 2, 3])
print(vector_row)

#Create a vector as a column
vector_column = np.array([[1],
                          [2],
                          [3]])
print(vector_column)

matrix = np.array([[1, 2, 3],
                   [1, 2, 3],
                   [1, 2, 3]], dtype=np.uint8)
cv2.imshow("img", matrix)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""
a = np.ones(3)
b = np.zeros(3)
c = np.random.random(3)

print(a)
print(b)
print(c)
"""

"""
date = np.array([1, 2])
one = np.ones(2)
num = date + one
num = date * 2
print(num)
"""

"""
name = "a.jpg"
print(name[:-4])
"""

date = np.array([1, 2], [3, 4])
min = date.min()
max = date.max()
sum = date.sum()
print(min)
print(max)
print(sum)