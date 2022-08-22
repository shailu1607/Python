a = [3,2,1,7,5,4]
e = []
o = []
for i in range(len(a)):
    if(i%2==0):
        e.append(a[i])
    else:
        o.append(a[i])
e.sort()
o.sort()
print(a)
print(e)
print(o)
print(e[1]+o[1])
