# Number of vowels in given string
def vowel(n, v):
    counts = {}.fromkeys(v, 0)
    n = n.casefold()
    for character in n:
        if character in counts:
            counts[character] += 1
    return counts


n = input()
v = 'aeiou'
print(vowel(n, v))
