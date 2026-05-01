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


def teorema_chineza_a_resturilor(resturi, moduli):
    P = 1
    for m in moduli:
        P = P * m
    x = 0
    for i in range(len(resturi)):
        P_i = P // moduli[i]
        inv_P_i = invers(P_i, moduli[i])
        x = (x + resturi[i] * P_i * inv_P_i) % P
    return x


def gaseste_g_ns(n, phi_n, prime_mici):
    g = 2
    while g < n:
        ok = True
        for pi in prime_mici:
            putere = phi_n // pi
            if a_la_b_mod_c(g, putere, n) == 1:
                ok = False
                break
        if ok:
            return g
        g += 1
    return None


def generare_chei_ns(p, q, prime_mici):
    n = p * q
    phi_n = (p - 1) * (q - 1)

    sigma = 1
    for pi in prime_mici:
        sigma *= pi

    g = gaseste_g_ns(n, phi_n, prime_mici)

    return n, g, sigma, phi_n


def criptare_ns(m, n, g, sigma, x):
    x_la_sigma = a_la_b_mod_c(x, sigma, n)
    g_la_m = a_la_b_mod_c(g, m, n)
    c = (x_la_sigma * g_la_m) % n
    return c


def decriptare_ns(c, n, g, phi_n, prime_mici):
    resturi = []

    for pi in prime_mici:
        putere = phi_n // pi
        c_i = a_la_b_mod_c(c, putere, n)

        m_i = 0
        for j in range(pi):
            test_val = a_la_b_mod_c(g, putere * j, n)
            if test_val == c_i:
                m_i = j
                break
        resturi.append(m_i)

    m = teorema_chineza_a_resturilor(resturi, prime_mici)
    return m


prime_mici = [3, 5, 7]
p = 13
q = 71

n, g, sigma, phi_n = generare_chei_ns(p, q, prime_mici)
print(f"Cheia publica: n = {n}, g = {g}, sigma = {sigma}")
print(f"Cheia privata: p = {p}, q = {q}, phi_n = {phi_n}")

mesaj = 42
x = 17

criptat = criptare_ns(mesaj, n, g, sigma, x)
print(f"Mesaj original: {mesaj}")
print(f"Mesaj criptat: {criptat}")

decriptat = decriptare_ns(criptat, n, g, phi_n, prime_mici)
print(f"Mesaj decriptat: {decriptat}")