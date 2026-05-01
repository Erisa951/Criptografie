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


def generare_chei_dj(p, q, s):
    n = p * q
    lam = cmmmc(p - 1, q - 1)

    n_la_s = n ** s
    inv_lam = invers(lam, n_la_s)

    d = lam * inv_lam
    g = n + 1

    return n, g, s, d


def criptare_dj(m, n, g, s, r):
    n_la_s = n ** s
    n_la_s_plus_1 = n ** (s + 1)

    g_la_m = a_la_b_mod_c(g, m, n_la_s_plus_1)
    r_la_ns = a_la_b_mod_c(r, n_la_s, n_la_s_plus_1)

    c = (g_la_m * r_la_ns) % n_la_s_plus_1
    return c


def decriptare_dj(c, d, n, s):
    n_la_s_plus_1 = n ** (s + 1)
    A = a_la_b_mod_c(c, d, n_la_s_plus_1)

    i = 0
    for k in range(1, s + 1):
        n_la_k_plus_1 = n ** (k + 1)
        n_la_k = n ** k
        n_la_k_minus_1 = n ** (k - 1)

        t1 = A % n_la_k_plus_1
        t2 = a_la_b_mod_c(n + 1, i, n_la_k_plus_1)

        diff = (t1 - t2) % n_la_k_plus_1
        c_val = (diff // n_la_k) % n

        i = i + c_val * n_la_k_minus_1

    return i


p = 17
q = 19
s = 2

n, g, s_ales, d = generare_chei_dj(p, q, s)
print(f"Cheia publica: n = {n}, g = {g}, s = {s_ales}")
print(f"Cheia privata: d = {d}")

mesaj = 42000
r = 23

criptat = criptare_dj(mesaj, n, g, s_ales, r)
print(f"Mesaj original: {mesaj}")
print(f"Mesaj criptat: {criptat}")

decriptat = decriptare_dj(criptat, d, n, s_ales)
print(f"Mesaj decriptat: {decriptat}")