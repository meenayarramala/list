a=int(input("enter the number"))
sum=0
while a>0:
    b=a%10
    sum=sum+b
    a=a//10
print(sum)
j=1
count=0
while j<=sum:
    if sum%j==0:
        count+=1
    j=j+1
if count==2:
    print("prime number")
else:
    print("not prime number")