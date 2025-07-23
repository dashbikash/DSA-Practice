import numpy as np
import sys
arr = np.random.randint(0, 20, size=10)
print("Unsorted: ",arr)
for p in range(0,len(arr)):
    min_index = p
    for i in range(p,len(arr)):
        if arr[min_index]>arr[i]:
            min_index=i
    arr[p],arr[min_index]=arr[min_index],arr[p]


print("Sorted:",arr)