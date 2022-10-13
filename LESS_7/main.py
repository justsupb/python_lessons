
from multiprocessing.sharedctypes import RawValue
import time
import random
def bSort(array):
    # определяем длину массива
    length = len(array)
    #Внешний цикл, количество проходов N-1
    for i in range(length):
        # Внутренний цикл, N-i-1 проходов
        for j in range(0, length-i-1):
            #Меняем элементы местами
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array
# arr=[random.randint(1,1000000) for i in range(5000)]
# print(bSort(arr))
path100 = 'LESS_7/arr100.txt'
path1000 = 'LESS_7/arr1000.txt'
path5000 = 'LESS_7/arr5000.txt'
path10000 = 'LESS_7/arr10000.txt'
path100000 = 'LESS_7/arr100000.txt'

# def write_to_file(arr,path):
#     with open(path,'w') as wf:
#         for i in range (len(arr)):
#             wf.write(str(arr[i])+'\n')
# write_to_file(arr,path5000)

def read_from_file(arr,path):
    with open(path,'r') as rf:
        for i in rf:
            arr.append(int(i))

# def comb_sort(arr):
#     step=int(len(arr)/1.247)
#     swap=1
#     while step > 1 or swap>0:
#         swap=0
#         i=0
#         while i+step < len(arr):
#             if arr[i] > arr[i+step]:
#                 arr[i], arr[i+step]=arr[i+step],arr[i]
#                 swap+=1
#             i+=1
#         if step >1:
#             step= int(step/1.247)
#     return arr





def quick_sort(arr):
    if len(arr)>1:
        elem=arr[random.randint(0,len(arr)-1)]
        low=[u for u in arr if u<elem]
        eq = [u for u in arr if u==elem]
        max = [u for u in arr if u>elem]
        arr=quick_sort(low)+eq+quick_sort(max)
    return arr
# arr=[3,2,1]
# print(quick_sort(arr))

arr1000=[]
read_from_file(arr1000,path1000)
st=time.time()
quick_sort(arr1000)
et=time.time()
ft=et-st
print(ft)

def get_time(iters):
    def dec(func):
        def wrapper(*args):
            it=iters
            sum=0
            while it!=0:

                st=time.time()
                rv=func(*args)
                et=time.time()
                ft=et-st
                sum=sum+ft
                it-=1
            finaltime=sum/iters
            print(finaltime)
            return rv
        return wrapper 
    return dec
@get_time(10000)
def comb_sort(arr):
    step=int(len(arr)/1.247)
    swap=1
    while step > 1 or swap>0:
        swap=0
        i=0
        while i+step < len(arr):
            if arr[i] > arr[i+step]:
                arr[i], arr[i+step]=arr[i+step],arr[i]
                swap+=1
            i+=1
        if step >1:
            step= int(step/1.247)
    return arr
read_from_file(arr1000,path1000)
comb_sort(arr1000)
