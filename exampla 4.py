n=int(input("enter the number"))
a=[2,5,1,3,7,4,-1]
b=[]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]+a[j]==n:
            d=[a[i],a[j]]
            b.append(d)
        j+=1
    i+=1
print(b)
