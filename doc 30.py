a=[2, -7, 5, -64, -14]
count=0
sum=0
i=0
while i<len(a):
    num=a[i]
    if num>0:
        count+=1
    else:
        sum+=1
    i=i+1
print(count,"positive number")
print(sum,"negative number")