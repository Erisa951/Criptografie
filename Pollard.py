import math

n = 10961

def cmmdc(a, b):
    if a < 0: a = -a
    if b < 0: b = -b
    if a == 0 or b == 0:
        return a + b
    while b:
        r = a % b
        a = b
        b = r
    return a


def f(x):
    return (x * x + 1) % n


x = 2
y = 2
d = 1

while d == 1:
    x = f(x)
    y = f(f(y))

    d = cmmdc(abs(x - y), n)

    print("x =", x, "y =", y, "cmmdc =", d)


if d == n:
    print("Nu am gasit factor")
else:
    print("Factor gasit:", d)
    print("Celalalt factor:", n // d)