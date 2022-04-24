# mean,median,mode of a list
def mean(l, n):
    t = 0
    for i in range(n):
        t += l[i]
        i += 1
    return t / n


def median(l, n):
    if (n % 2 == 0):
        m1 = l[(n // 2) - 1]
        m2 = l[n // 2]
        return m1, m2
    else:
        x = n // 2
        m = l[x]
        return m


def mode(l):
    counts = {}
    for item in l:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return [key for key in counts.keys() if counts[key] == max(counts.values())]


n = int(input())
l = []
for i in range(n):
    x = int(input())
    l.insert(i, x)
print("MEAN = ", mean(l, n))
print("MEDIAN = ", median(l, n))
print("MODE = ", mode(l))
