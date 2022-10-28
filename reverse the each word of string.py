l=input("enter the sentence")
a=l.split()
b=[]
for i in a:
    b.append(i[::-1])
print(b)