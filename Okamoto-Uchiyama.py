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


def functie_L(x, p):
    return (x - 1) // p


def generare_chei_ou(p, q, g):
    n = p * p * q
    h = a_la_b_mod_c(g, n, n)
    return n, h


def criptare_ou(m, n, g, h, r):
    g_la_m = a_la_b_mod_c(g, m, n)
    h_la_r = a_la_b_mod_c(h, r, n)
    c = (g_la_m * h_la_r) % n
    return c


def decriptare_ou(c, p, g):
    p_patrat = p * p

    c_p = a_la_b_mod_c(c, p - 1, p_patrat)
    g_p = a_la_b_mod_c(g, p - 1, p_patrat)

    a = functie_L(c_p, p)
    b = functie_L(g_p, p)

    inv_b = invers(b, p)
    m = (a * inv_b) % p
    return m


p = 17
q = 19
g = 2

n, h = generare_chei_ou(p, q, g)
print(f"Cheia publica: n = {n}, g = {g}, h = {h}")
print(f"Cheia privata: p = {p}, q = {q}")

mesaj = 10
r = 5

cifrat = criptare_ou(mesaj, n, g, h, r)
print(f"Mesaj original: {mesaj}")
print(f"Mesaj criptat: {cifrat}")

decriptat = decriptare_ou(cifrat, p, g)
print(f"Mesaj decriptat: {decriptat}")