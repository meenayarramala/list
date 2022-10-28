a=[50,40,23,70,56,12,5,10,7]
i=0
min=a[i]
max=0
secondmax=0
while i<len(a):
    num=a[i]
    if num>max:
        max=num
    elif num>secondmax:
        secondmax=num
    elif num<min:
        min=num
    i=i+1
print(max,"first maximum")
print(secondmax,"second maximum")
print(min,"minimum number")



