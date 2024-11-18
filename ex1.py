import numpy as np

arr1 = np.zeros(10)
print(arr1)

arr2 = np.full(10, 2.5)
print(arr2)

arr3 = np.zeros(10)
arr3[4] = 1
print(arr3)

arr4 = np.arange(10, 50)
print(arr4)

arr5=np.array([1.,2.,0.,0.,4.,0])
arr5_new=np.where(arr5 == 0)
print(arr5_new)

arr6=np.eye(3)
print(arr6)

arr7=np.random.sample((10,10))
arr7 = np.round(arr7, 3)
print(arr7)
print(f"Max:",arr7.max())
print(f"Min:",arr7.min())

arr8=np.random.sample(30)
arr8=np.round(arr8, 3)
print(arr8)
arr8_mean=np.mean(arr8)
print(arr8_mean)

arr9 = np.zeros((8,8))
arr9[1::2, ::2]=1
arr9[::2, 1::2]=1
print(arr9)

arr10 = np.random.sample((5,3))
arr10 = np.round(arr10, 3)
arr11 = np.random.sample((3,2))
arr11 = np.round(arr11, 3)
arr12=np.dot(arr10, arr11)
print(arr12)

arr13=np.array((1.,1.,3))
arr14=np.array((1.,2.,3))
is_equals=np.array_equal(arr13,arr14)
print(is_equals)

print(arr7)
print("\n\n")
arr7[arr7 == arr7.max()]=0
print(arr7)

arr15 = np.array([1, 2, 3, 4, 4, 2, 6, 3, 4, 5, 1, 2, 2])

unique, counts = np.unique(arr15, return_counts=True)
print("-------------", unique, counts)

most_frequent_value = unique[np.argmax(counts)]
frequency = counts[np.argmax(counts)]
print(f"Наиболее частое значение: {most_frequent_value} (встречается {frequency} раз)")

n = 3
top_n_values = np.partition(arr15, -n)[-n:]
print(f"{n} наибольших значений: {top_n_values}")





