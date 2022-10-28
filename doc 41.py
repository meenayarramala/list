a=[[1,2],
   [2,4]]
i=0
b=[]
while i<len(a):
    n=a[i]
    count=0
    j=0
    while j<len(n):
        count+=1
        j=j+1
    i=i+1
    b.append(count)
print(b)
