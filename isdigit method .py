str="meena223uma"
b=[]
i=0
while i<len(str):
    if str[i].isdigit():
        b.append(str[i])
    i=i+1
p="".join(b)
print(p)
