a=[[8,3,4],
  [1,5,9],
  [6,7,2]]
i=0
while i<len(a):
    j=0
    sumr=0
    while j<len(a[i]):
        sumr=sumr+a[i][j]
        j+=1
    i+=1
print("sumr:",sumr)
i=0
while i<len(a):
    j=0
    sumc=0
    while j<len(a[i]):
        sumc=sumc+a[j][i]
        j+=1
    i+=1
print("sumc:",sumc)
i=0
r=2
m=0
while i<len(a):
    j=2
    while j<len(a):
        m+=a[i][r]
        j+=1
        r-=1
    i+=1
print("m:",m)
i=0
p=0
n=0
while i<len(a):
    j=2
    while j<len(a):
        n+=a[i][p]
        j+=1
        p+=1
    i+=1
print("n:",n)
print()
if sumr==sumc==m==n:
    print(a,"it is a magic square")
else:
    print(a,"it is not a magic square")