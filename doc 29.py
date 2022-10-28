a=[5,6,[],3,[],[],9]
i=0
b=[]
while i<len(a):
    num=a[i]
    if a[i]==num and num!=[]:
        b.append(num)
    i=i+1
print(b)