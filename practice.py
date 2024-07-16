import numpy as np
import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a, b)
toc = time.time()

print(c)
print("This took:" + str((toc - tic) * 1000) + "ms")

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()
print(c)
print("This took:" + str((toc - tic) * 1000) + "ms")

d = np.array([[50, 0, 4, 20],
             [1.2, 104, 58, 2.0],
             [1.3, 138, 99, .9]])
print(d)

cal = d.sum(axis=0)
print(cal)

# percentage = 100 * d/cal.reshape(1, 4)
# print(percentage)

# a = np.random.rand(1000000)
# b = np.random.rand(1000000)

# tic = time.time()
# c = np.dot(a, b)
# toc = time.time()

# print(c)
# print("This took:" + str((toc - tic) * 1000) + "ms")

# c = 0
# tic = time.time()
# for i in range(1000000):
#     c += a[i]*b[i]
# toc = time.time()
# print(c)
# print("This took:" + str((toc - tic) * 1000) + "ms")

# d = np.array([[50, 0, 4, 20],
#              [1.2, 104, 58, 2.0],
#              [1.3, 138, 99, .9]])
# print(d)

# cal = d.sum(axis=0)
# print(cal)

# percentage = 100 * d/cal.reshape(1, 4)
# print(percentage)


# wrong
# a = np.random.randn(5,)

# print(a)

# #right
# a = np.random.randn(5,1)

# print(a)

a=np.random.randn(3,3)
b=np.random.randn(2,1) 
c=a+b
print(c.shape())

a = np.random.randn(3, 4)
b = np.random.randn(4,1)
print(a)
print(a.T)
print(b)
print(b.T)


