l=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
min=10
max=0
while i<len(l):
    d=len(l[i])
    if d>max:
        max=d
        r=l[i]
    if d<min:
        min=d
        h=l[i]
    i=i+1
n=max,r
k=min,h
print(tuple(k))
print(tuple(n))



# a=[[1,3],[0],[9,11],[13,15,17]]
# i=0
# max=0
# min=10
# while i<len(a):
#     c=len(a[i])
#     if c>max:
#         max=c
#         e=a[i]
#     elif c<min:
#         min=c
#         f=a[i]
#     i=i+1
# print("list maximum is","(",max,",",e,")")
# print("list minimum is","(",min,",",f,")")