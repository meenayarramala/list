a=['1', '2', '3', '4', '5', '6', '7', '8']
i=0
b=[]
index=1
while i<len(a):
    n=a[i]
    c=n+a[index]
    b.append(c)
    index+=2
    i=i+2
print(b)


