a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i=0
d=[]
b=[]
while i<len(a):
    n=a[i]
    if n>a[2]:
        d.append(n)
    else:
        b.append(n)
    i=i+1
list3=d+b
print(list3)
