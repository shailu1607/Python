n = int(input())
l = list(map(int,input().split()))[:n]
count = 1
for i in range(n-1):
    if(l[i]<l[i+1]):
        count+=1
print(count)