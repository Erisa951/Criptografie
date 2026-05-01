def cmmdc(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a == 0 or b == 0:
        return a + b
    while b:
        r = a % b
        a = b
        b = r
    return a

def cmmmc(a, b):
    return (a * b) // cmmdc(a, b)

def a_la_b_mod_c(a, b, c):
    p = 1
    while b:
        if b % 2 == 1:
            p = (p * a) % c
        a = (a * a) % c
        b //= 2
    return p

def invers(a, N):
    copy_N = N
    x1 = 1
    x2 = 0
    while N:
        r = a % N
        x = x1 - (a // N) * x2
        x1 = x2
        x2 = x
        a = N
        N = r
    if a == 1:
        return x1 % copy_N
    return None

def generare_chei_ss(p, q):
    N = p * p * q
    pq = p * q
    lam = cmmmc(p - 1, q - 1)
    d = invers(N, lam)
    return N, d, pq

def criptare_ss(m, N):
    c = a_la_b_mod_c(m, N, N)
    return c

def decriptare_ss(c, d, pq):
    m = a_la_b_mod_c(c, d, pq)
    return m

p = 7
q = 11

N, d, pq = generare_chei_ss(p, q)
print(f"Cheia publica: N = {N}")
print(f"Cheia privata: d = {d}, pq = {pq}")

mesaj = 42

criptat = criptare_ss(mesaj, N)
print(f"Mesaj original: {mesaj}")
print(f"Mesaj criptat: {criptat}")

decriptat = decriptare_ss(criptat, d, pq)
print(f"Mesaj decriptat: {decriptat}")