# l=[1234, 122, 1984, 19372, 100]
# l=[1234,922,1984,19372,100]
l=["abc","abc","ab","a"]
result=True
d=str(l[0])
for i in l:
    c=str(i)
    if d[0]!=c[0]:
        result=False
        break
    else:
        continue
print(result)
