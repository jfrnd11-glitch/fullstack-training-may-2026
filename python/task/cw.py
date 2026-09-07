
def square():
    side = int(input("Enter side: "))
    area = side * side
    print("Area of Square =", area)

def rectangle():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print("Area of Rectangle =", area)

def triangle():
    base = int(input("Enter base: "))
    height = int(input("Enter height: "))
    area = base * height / 2
    print("Area of Triangle =", area)

square()
rectangle()
triangle()

    