# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# e=[]
# while a<=b:
#     i=1
#     c=0
#     while i<=a:
#         if a%i==0:
#             c=c+1
#         i=i+1
#     if c==2:
#         e.append(a)
#     a=a+1
# print(e)
# k=0
# h=[]
# while k<len(e):
#     g=e[k]
#     j=0
#     while g>0:
#         r=g%10
#         j=j*10+r
#         g=g//10
#     i=1
#     c=0
#     while i<=j:
#         if j%i==0:
#             c=c+1
#         i=i+1
#     if c==2:
#         v=e[k],j
#         h.append(list(v))
#     k=k+1
# print(h)



a=int(input("enter the number:"))
b=int(input("enter the number:"))
e=[]
while a<=b:
    i=1
    c=0
    while i<=a:
        if a%i==0:
            c=c+1
        i=i+1
    if c==2:
        e.append(a)
    a=a+1
print(e)
k=0
h=[]
while k<len(e):
    g=e[k]
    j=0
    while g>0:
        r=g%10
        j=j*10+r
        g=g//10
    l=e[k],j
    h.append(list(l))
    k=k+1
print(h)