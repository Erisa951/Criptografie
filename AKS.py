import math

def cmmdc(a, b):
    if a < 0: a = -a
    if b < 0: b = -b
    if a == 0 or b == 0: return a + b
    while b:
        a, b = b, a % b
    return a

def euler_phi(n):
    rezultat = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            rezultat = rezultat // p * (p - 1)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        rezultat = rezultat // n * (n - 1)
    return rezultat

def este_putere(n):
    for b in range(2, int(math.log2(n)) + 1):
        a = int(round(n ** (1 / b)))
        if a ** b == n:
            return True
    return False

def reducere_modulo(baza, puterea, n):
    rezultat = 1
    while puterea > 0:
        if puterea % 2 == 1:
            rezultat = rezultat * baza % n
        baza = baza * baza % n
        puterea //= 2
    return rezultat

def cauta_R(n):
    maxK = int(math.log2(n) ** 2)
    r = 1
    while True:
        r += 1
        ok = True
        for k in range(1, maxK + 1):
            val = reducere_modulo(n, k, r)
            if val == 0 or val == 1:
                ok = False
                break
        if ok:
            return r

def inmulteste_polinoame(a, b, mod, r):
    rezultat = [0] * r
    for i in range(len(a)):
        for j in range(len(b)):
            rezultat[(i + j) % r] = (rezultat[(i + j) % r] + a[i] * b[j]) % mod
    return rezultat

def reducere_modulo_polinoame(base, power, r, mod, a):
    rezultat = [0] * r
    rezultat[0] = 1
    while power > 0:
        if power % 2 == 1:
            rezultat = inmulteste_polinoame(rezultat, base, mod, r)
        base = inmulteste_polinoame(base, base, mod, r)
        power //= 2
    rezultat[0] = (rezultat[0] - a) % mod
    rezultat[mod % r] = (rezultat[mod % r] - 1) % mod
    return rezultat

def aks(n):
    if este_putere(n):
        return "compus"
    r = cauta_R(n)
    for a in range(2, min(r, n)):
        if cmmdc(a, n) > 1:
            return "compus"
    if n <= r:
        return "prim"
    limita = int(math.sqrt(euler_phi(r)) * math.log2(n))
    for a in range(1, limita + 1):
        base = [a, 1] + [0] * (r - 2)
        x = reducere_modulo_polinoame(base, n, r, n, a)
        if any(coef != 0 for coef in x):
            return "compus"
    return "prim"

print(aks(2**61 - 1))