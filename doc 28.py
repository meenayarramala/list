a=[1, 1, 2, 3, 4, 5, 1, 2] 
i=0
n=1
b=[]
while i<len(a):
    num=a[i]
    if i==num and i!=n:
        b.append(num)
    i=i+1
print(b)