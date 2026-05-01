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


def generare_chei_bg(p, q):
    N = p * q
    return N


def criptare_bg(mesaj_biti, N, r0):
    L = len(mesaj_biti)
    cifrat = []
    r = r0

    for i in range(L):
        r = (r * r) % N
        b = r % 2
        c = (mesaj_biti[i] + b) % 2
        cifrat.append(c)

    y = (r * r) % N
    return cifrat, y


def decriptare_bg(cifrat, y, p, q):
    L = len(cifrat)
    N = p * q

    baza_p = (p + 1) // 4
    dp = a_la_b_mod_c(baza_p, L + 1, p - 1)

    baza_q = (q + 1) // 4
    dq = a_la_b_mod_c(baza_q, L + 1, q - 1)

    u = a_la_b_mod_c(y, dp, p)
    v = a_la_b_mod_c(y, dq, q)

    inv_q = invers(q, p)
    inv_p = invers(p, q)

    r0 = (u * q * inv_q + v * p * inv_p) % N

    decriptat = []
    r = r0

    for i in range(L):
        r = (r * r) % N
        b = r % 2
        m = (cifrat[i] + b) % 2
        decriptat.append(m)

    return decriptat


p = 11
q = 19

N = generare_chei_bg(p, q)
print(f"Cheia publica: N = {N}")
print(f"Cheia privata: p = {p}, q = {q}")

mesaj_biti = [1, 0, 1, 1, 0, 0, 1]
r0 = 17

criptat, y = criptare_bg(mesaj_biti, N, r0)
print(f"Mesaj original (biti): {mesaj_biti}")
print(f"Mesaj criptat: C = {criptat}, y = {y}")

decriptat = decriptare_bg(criptat, y, p, q)
print(f"Mesaj decriptat (biti): {decriptat}")