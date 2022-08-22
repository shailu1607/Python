def rev(n):
    temp = n
    rev = 0
    while(temp>0):
        digi = temp%10
        rev = (rev*10)+digi
        temp = temp//10
    return rev

a = 100
b = 200
count = 0
'''for i in range(a,b,1):
    s = str(i)
    if(s==s[::-1]):
        print(i)
        count+=1
print(count)
'''
for i in range(a,b,1):
    rev1 = rev(i)
    if(i==rev1):
        print(i)