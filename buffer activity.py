def squareperi(x):
    perimeter=4*xprint("perimeter of square is",perimeter)
def rectangleperi(l,b):
    perimeter=2*(l+b)
    return perimeter
def circumference(r):
    c=2*3.14*r
    print("the circumference of circle is",c)

r=int(input("enter raduis of circle: "))
circumference(r)
x=int(input("enter side of square->"))
squareperi(x)
l=int(input("enter the length of rectangle->"))
b=int(input("enter the breadth of rectangle->"))
print(rectangleperi(l,b))