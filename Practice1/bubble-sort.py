import numpy as np
arr = np.random.randint(0, 20, size=10)
print("Unsorted: ",arr)
for p in range(len(arr)-1,0,-1):
    for i in range(0,p):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            

print("Sorted:",arr)