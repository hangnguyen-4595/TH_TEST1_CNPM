def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

print("BCNN là:", lcm(a, b))
