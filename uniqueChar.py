s = "some money are mystery apart"
a = list(s.split())
x = []
print(a)

for i in range(len(a)):
    temp = a[i]
    x.append(temp[0])
print(x)

d = {} 
for i in x:
    if i in d:
        d[i] += 1
    else:
        d[i] =1
print(d)

for i in d:
    if(d[i] == 1):
        print(i)