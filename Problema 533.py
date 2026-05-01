import math

def fermat(n):
    t = int(math.sqrt(n))
    if t * t == n:
        return t, t
    t = t + 1
    while True:
        d = t*t - n
        s = int(math.sqrt(d))
        if s*s == d:
            a = t - s
            b = t + s
            return a, b
        else:
            t = t + 1


n = 40723
a, b = fermat(n)
print( n, "=", a, "*", b)