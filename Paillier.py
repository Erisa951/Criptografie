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


def L(x, n):
    return (x - 1) // n


def generare_chei_paillier(p, q):
    n = p * q
    n_patrat = n * n
    lam = cmmmc(p - 1, q - 1)

    g = n + 1

    g_la_lam = a_la_b_mod_c(g, lam, n_patrat)
    l_val = L(g_la_lam, n)
    mu = invers(l_val, n)

    return n, g, lam, mu


def criptare_paillier(m, n, g, r):
    n_patrat = n * n
    g_la_m = a_la_b_mod_c(g, m, n_patrat)
    r_la_n = a_la_b_mod_c(r, n, n_patrat)
    c = (g_la_m * r_la_n) % n_patrat
    return c


def decriptare_paillier(c, lam, mu, n):
    n_patrat = n * n
    c_la_lam = a_la_b_mod_c(c, lam, n_patrat)
    l_val = L(c_la_lam, n)
    m = (l_val * mu) % n
    return m


p = 17
q = 19

n, g, lam, mu = generare_chei_paillier(p, q)
print(f"Cheia publica: n = {n}, g = {g}")
print(f"Cheia privata: lam = {lam}, mu = {mu}")

mesaj = 42
r = 23

criptat = criptare_paillier(mesaj, n, g, r)
print(f"Mesaj original: {mesaj}")
print(f"Mesaj criptat: {criptat}")

decriptat = decriptare_paillier(criptat, lam, mu, n)
print(f"Mesaj decriptat: {decriptat}")