s =109
v =int(input('v:'))
t =int(input('t:'))
s0=t*v
if s0//109<1:
    s1=s0-109
else: s1= s0//109
print(s0%s)