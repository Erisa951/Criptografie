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


def hash_cs(u1, u2, e, q):
    return (u1 + u2 + e) % q


def generare_chei_cs(p, g1, g2, x1, x2, y1, y2, z):
    c1 = a_la_b_mod_c(g1, x1, p)
    c2 = a_la_b_mod_c(g2, x2, p)
    c = (c1 * c2) % p

    d1 = a_la_b_mod_c(g1, y1, p)
    d2 = a_la_b_mod_c(g2, y2, p)
    d = (d1 * d2) % p

    h = a_la_b_mod_c(g1, z, p)

    return c, d, h


def criptare_cs(m, p, q, g1, g2, c, d, h, k):
    u1 = a_la_b_mod_c(g1, k, p)
    u2 = a_la_b_mod_c(g2, k, p)

    h_la_k = a_la_b_mod_c(h, k, p)
    e = (m * h_la_k) % p

    alpha = hash_cs(u1, u2, e, q)

    c_la_k = a_la_b_mod_c(c, k, p)
    d_la_k_alpha = a_la_b_mod_c(d, k * alpha, p)
    v = (c_la_k * d_la_k_alpha) % p

    return u1, u2, e, v


def decriptare_cs(u1, u2, e, v, p, q, x1, x2, y1, y2, z):
    alpha = hash_cs(u1, u2, e, q)

    exp1 = x1 + y1 * alpha
    exp2 = x2 + y2 * alpha

    u1_la_exp1 = a_la_b_mod_c(u1, exp1, p)
    u2_la_exp2 = a_la_b_mod_c(u2, exp2, p)
    v_verificare = (u1_la_exp1 * u2_la_exp2) % p

    if v != v_verificare:
        return None

    u1_la_z = a_la_b_mod_c(u1, z, p)
    inv_u1_la_z = invers(u1_la_z, p)

    m = (e * inv_u1_la_z) % p
    return m


p = 23
q = 11
g1 = 2
g2 = 4

x1 = 3
x2 = 4
y1 = 5
y2 = 6
z = 7

c, d, h = generare_chei_cs(p, g1, g2, x1, x2, y1, y2, z)
print(f"Cheia publica: c = {c}, d = {d}, h = {h}")
print(f"Cheia privata: x1 = {x1}, x2 = {x2}, y1 = {y1}, y2 = {y2}, z = {z}")

mesaj = 8
k = 2

u1, u2, e_criptat, v = criptare_cs(mesaj, p, q, g1, g2, c, d, h, k)
print(f"Mesaj original: {mesaj}")
print(f"Mesaj criptat: u1 = {u1}, u2 = {u2}, e = {e_criptat}, v = {v}")

decriptat = decriptare_cs(u1, u2, e_criptat, v, p, q, x1, x2, y1, y2, z)
if decriptat is None:
    print("Mesajul a fost respins (verificare esuata).")
else:
    print(f"Mesaj decriptat: {decriptat}")