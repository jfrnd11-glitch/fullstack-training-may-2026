def simple_interest(p=1000, r=5, t=2):
    si = (p * r * t) / 100
    return si

def main():
    principal =int(input("enter principal amount:"))
    rate = int(input("enter reat of interest:"))
    time =int(input("enter time (year):"))

    result = simple_interest(principal, rate, time)
    print("Simple Interest =", result)

    print("Default Simple Interest =", simple_interest())

main ()