def digisum(x):
    temp = x
    sum1 = 0
    while(temp>0):
        digi = temp%10
        sum1+=digi
        temp=temp//10
    return sum1

def sumi(x,r):
    if(r==0):
        return 0
    else:
        return r*x

n = int(input())
r = int(input())
x = digisum(n)
ans = sumi(x,r)
print(digisum(ans))
