s = input()
l = int(input())
maxi = 0
count = 0
for i in range(len(s)):
    if(i%l==0):
        maxi = max(maxi,count)
        count = 0
    if(s[i]=="a"):
        count+=1
        #print(count)
maxi = max(count,maxi)
print(maxi)