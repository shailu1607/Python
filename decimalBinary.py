def dectobin(n):
    return bin(n).replace("0b","")

def bintodec(n):
    return int(n,2)

n = int(input())
b = dectobin(n)
s = str("".join(map(str,b)))
x = s[::-1]
d = bintodec(x)
print(d)