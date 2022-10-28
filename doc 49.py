a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
i=0
while i<len(a):
    if a[i]=="f":
        b=i
    elif a[i]=="c":
        c=i
    elif a[i]=="k":
        d=i
    elif a[i]=="w":
        e=i
    i=i+1
print("last occurence of f is",b)
print("last occurence of c is",c)
print("last occurence of k is",d)
print("last occurence of w is",e)
