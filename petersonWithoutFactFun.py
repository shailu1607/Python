'''def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
'''
def peterson(a):
    sum1 = 0
    tem = a
    fact = 1
    while (tem>0):
        digi = tem%10
        if(digi>1):
            for i in range(1,digi+1):
                fact *=i
        sum1 = sum1+ fact
        #print(sum1)
        fact = 1
        tem = tem//10
    return sum1

a = int(input())
print(peterson(a))