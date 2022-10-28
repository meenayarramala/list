n=int(input("no"))
i=0
s=0
while i<=n:
    r=n%10
    i=r**2
    n=n//10
    print(i,end=" ")