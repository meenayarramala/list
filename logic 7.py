a=["p","q"]
i=0
b=[]
while i<len(a):
    j=1
    while j<=4:
        c=str(j)
        k=a[i]+c
        b.append(k)
        j=j+1
    i=i+1
print(b)