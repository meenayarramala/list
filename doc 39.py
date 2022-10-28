a=[[0,1,2,"",""],
[2,3,4,"",""],
[3,4,5,6,""],
[7,8,9,10,11],
[12,13,14,"",""]]
i=0
c=[]
while i<len(a):
    j=0
    sum=0
    k=0
    while j<len(a):
        b=a[j][i]
        if type(b)==int:
            sum=sum+b
        if b=="":
            k=k+0
        else:
            k=k+1
        j=j+1
    avg=sum/k
    c.append(avg)
    i=i+1
print(c)

