l=["mom"]
i=0
s=0
while i<len(l):
    n=l[i]
    r=n[::-1]
    if l[i]==r:
        print(r,"is pallindrome")
        s=s+1
    else:
        print(r,"is not pallindrome")
    i=i+1