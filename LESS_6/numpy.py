import numpy as np
import time
import random 
def bubble_sort(arr):
    last_index=len(arr)-1
    for i in range (last_index):
        for j in range(last_index):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    # print(arr)
path= 'less6/files/array.txt'
def write_to_file(path_to_file,arr):
    with open (path_to_file,'w') as f:
        for i in arr:
            f.write(str(i)+'\n')
def read_from_file(path_to_file,arr):
    with open (path_to_file, 'r') as f:
        for i in f:
            arr.append(int(i))
N=10000
st0=time.time()
et0=time.time()
fr0=et0-st0

# arr =[random.randint(0,1000) for i in range(100)]
# arr_numpy=np.array(arr)
# bubble_sort(arr)