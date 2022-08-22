n = int(input())
temp = n
prod = 1
while(temp>0):
    digi = temp%10
    prod = prod*digi
    temp=temp//10
    #print(digi)
print(prod)