def euclid_extins(a, b):
    xa, ya = 1, 0
    xb, yb = 0, 1

    while b != 0:
        q = a // b

        r = a % b

        xr = xa - q * xb
        yr = ya - q * yb

        a, b = b, r

        xa, ya = xb, yb
        xb, yb = xr, yr

    return a, xa, ya


n1 = 360
n2 = 294
cmmdc, x, y = euclid_extins(n1, n2)

print(f"{(n1,n2)}: {cmmdc}")
print(f"{n1}*({x}) + {n2}*({y}) = {n1 * x + n2 * y}")