def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

n = int(input())
x = n-1
a = fact(x)
print(a*2)