# sum = 0
# arr=[10,20,200,44,25,65,88]
# for i in arr:
#     sum+=i
# print(sum)
a=int(input())
b=int(input())
arr=[10,20,200,44,25,65,88]
arr[a],arr[b]=arr[b],arr[a]
print(arr)