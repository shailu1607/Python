a = [1,2,3,0,4,0,5,6,0]
#a.sort()
print(a)
for i in a:
    if(i == 0):
        a.append(0)
        a.remove(i)
print(a)