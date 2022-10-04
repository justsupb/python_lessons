a=int(input())
b=int(input())
while a<=b:
    if a==4:
        print(a**3)
        a+=1
        continue
    elif a%2==0:
        print(a**2)
    a+=1