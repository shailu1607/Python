def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

def peterson(a):
    sum1 = 0
    tem = a
    while (tem>0):
        digi = tem%10
        sum1 = sum1+ fact(digi)
        tem = tem//10
    return sum1

a = int(input())
print(peterson(a))