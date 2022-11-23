hours=input("enter hours")
h=float(hours)
x=input("enter the rate")
y=float(x)
if h<=40:
    print(h*y)
else:
    print(40*y+(h-40)*1.5*y)
