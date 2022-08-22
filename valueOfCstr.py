s = "HipHop ---value of cstr"
a = s.replace(" ---value of cstr","")
l = list(a)
#print(l)
for i in range(len(l)):
    temp = l[i]
    if(temp.isupper()):
        if(i>1):
            if(l[i-1]==" "):
                l[i]=l[i].lower()
            else:
                l[i]=" "+l[i].lower()
        else:
            l[i]=l[i].lower()

print(''.join(map(str,l)))