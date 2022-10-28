str="meena223mani"
b=[]
i=0
p=" "
while i<len(str):
    if str[i].isalpha():
        b.append(str[i])
    i=i+1
p="".join(b)
print(p)
