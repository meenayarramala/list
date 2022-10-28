a=["https://www.w3resource.com/python-exercises/list/"]
b=['.com', '.edu', '.tv']
for i in a:
    for j in b:
        print(j)
        if j in i:
            print(True)
        else:
            print(False)

            