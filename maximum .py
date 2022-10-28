a=[10,45,60,70,56,89]
i=0
max1=a[0]
max2=a[0]
max3=a[0]
while i<len(a):
    if a[i]>max1:
        max1=a[i]
    i=i+1
j=0
while j<len(a):
    if a[j]>max2 and a[j]!=max1:
        max2=a[j]
    j=j+1
k=0
while k<len(a):
    if a[k]>max3 and a[k]!=max2 and a[k]!=max1:
        max3=a[k]     
    k=k+1
print(max1)
print(max2)
print(max3)