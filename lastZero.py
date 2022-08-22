n = int(input())
l = list(map(int,input().split()))[:n]
x = []
count = 0
for i in range(n):
    if(l[i]!=0):
        temp = l[i]
        x.append(temp)
    else:
        count=count+1
for j in range(count):
    x.append(0)
print(" ".join(map(str,x)))