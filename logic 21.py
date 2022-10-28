a=[3,5,2,1,6,9]
i=0
b=[]
while i<len(a):
          k=str(a[i])+str(a[i+1])
          b.append(int(k))
          i=i+2
print(b)

