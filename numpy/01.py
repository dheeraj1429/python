import numpy as np
from numpy import pi

# A = np.array([
#   [1,2,3],
#   [4,5,6]
# ])
# B = np.zeros((2, 3))
# C = np.ones((3, 3))
# I = np.eye(3)
# R = np.random.rand(2, 3)

# print("B", B)
# print("C", C)
# print("I", I)
# print("R", R)

# print("Shape of A:", A.shape)
# print("Dimensions:", A.ndim)

# A_reshaped = A.reshape(3, 2)
# print("Reshaped 3x2:\n", A_reshaped)

# A_flat = A.flatten()
# print("Flattened:", A_flat)

# b = np.arange(10).reshape(2, 5)
# print(b, b.size, b.dtype, b.shape)
# a = np.arange(15).reshape(3, 5)
# print(a, a.ndim, a.shape, a.size, a.dtype, a.itemsize)

# print(type(a))

# a =  np.array([(1.2, 2, 3), (4, 5, 6)])
# print(a)

# print(
#   np.array(
#     [
#       tuple(np.arange(10)),
#       tuple(np.arange(10)),
#       tuple(np.arange(10))
#     ]
#   )
# )

# print(np.array([[1, 2], [3, 4]], dtype=np.float32))
# print(np.array([[1, 2], [3, 4]], dtype=np.int32))

# print(np.zeros((3, 4)))
# print(np.zeros((2, 3, 4)))

# print(np.empty((2, 3)))
# print(np.arange(0, 2, .3))
# print(np.linspace(0, 2, 9))

# a = np.arange(10)
# print(a)
# print(5 <= a)

# a = np.array([10, 20, 30, 40])
# b = np.arange(4)
# print(a - b)

# a = np.array([0, pi/6, pi/4, pi/3, pi/2])
# print(10 * np.sin(a))
# print(np.sin(a))
# print(a)
# print(np.sin(a))
# print(np.cos(a))

# a = np.arange(12).reshape(3, 4)
# print(a.sum(axis=0))
# print(a.min(axis=0))
# print(a.min(axis=0))
# print(a)
# print(a.min(axis=0))
# print(a.min(axis=1))
# print(a)
# print(a.cumsum(axis=0))
# print(a.cumsum(axis=1))

# a = np.arange(10) ** 2
# print(a)
# print(a[0:])
# print(a[::-1])
# print(a[:6:2])

# a = np.arange(10).reshape(2, 5)
# print(a)
# print(a[::-1])

# for i in a.flat:
#   print(i)

# print(np.floor(10))

# a = np.arange(10).reshape(2, 5)
# print(a)
# a.resize((1, 10))
# print(a)

# class Solution:
#     def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
#         l: list[tuple[int]] = []

#         for idx, val in enumerate(growTime):
#             l.append((val, plantTime[idx])) # (growTime, plantTime)

#         l.sort(key=lambda x: x[0], reverse=True)
#         print(l)

#         day: int = 0
#         max_bloom_day: int = 0

#         for item in l:
#             bloom_day = item[1] + day + item[0]
#             day = item[1] + day
#             if bloom_day > max_bloom_day:
#                 max_bloom_day = bloom_day
#             print("bloom_day", bloom_day, "day", day)

#         return max_bloom_day


# print(Solution().earliestFullBloom(plantTime=[1,2,3,2], growTime=[2,1,2,1]))
# print(Solution().earliestFullBloom(plantTime=[1,4,3], growTime=[2,3,1]))
# print(Solution().earliestFullBloom(plantTime=[8,2], growTime=[1,1]))

