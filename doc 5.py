# l = [1, 2, 2, 5, 8, 4, 4, 8]
# l1 = []
# count = 0
# for item in l:
#     if item not in l1:
#         count += 1
#         l1.append(item)
# print("No of unique items are:", count)




l=[1,2,2,5,8,4,4,8]
i=0
a=[]
while i<len(l):
    b=l[i]
    if b not in a:
        a.append(b)
    i=i+1
print(a)
