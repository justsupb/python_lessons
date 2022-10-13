import random
def quick_sort(arr):
    if len(arr)>1:
        elem=arr[random.randint(0,len(arr)-1)]
        low=[u for u in arr if u<elem]
        eq = [u for u in arr if u==elem]
        max = [u for u in arr if u>elem]
        arr=quick_sort(low)+eq+quick_sort(max)
    return arr
arr=[3,2,1]
print(quick_sort(arr))