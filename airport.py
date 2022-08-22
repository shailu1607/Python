n = int(input())
l = list(map(int,input().split()))[:n]
l.sort()
print(" ".join(map(str,l)))