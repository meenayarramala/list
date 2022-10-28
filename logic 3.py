a=[2,0,4,0,0,1,3,0]
i=0
index=0
c=[]
d=[]
while i<len(a):
    n=a[i]
    if n>=a[index]and n!=0:
        c.append(n)
    elif n==0:
        d.append(n)
    i=i+1
    index+=1
c.extend(d)
print(c)