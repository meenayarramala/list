a=[3,6,2,7,4,9]
a.sort()
i=0
j=-1
sum=0
while i<len(a)/2:
    k=a[i]*a[j]
    sum=sum+k
    i=i+1
    j=j-1
print(sum)