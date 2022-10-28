a="my name is meena"
b=a.split()
i=0
c=[]
l=""
while i<len(b):
    d=b[i]
    e=d[0].upper()
    k=d.replace(d[0],e)
    l=l+k
    l=l+" "
    i=i+1
c.append(l)
print(c)

    
        
