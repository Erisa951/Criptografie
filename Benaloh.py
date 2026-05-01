def a_la_b_mod_c(a, b, c):
    p = 1
    while b:
        if b % 2 == 1:
            p = (p * a) % c
        a = (a * a) % c
        b //= 2
    return p

def generare_chei_benaloh(p, q, r, y):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    exponent = phi_n // r
    x = a_la_b_mod_c(y, exponent, n)
    return n, phi_n, x

def criptare_benaloh(m, r, n, y, u):
    y_la_m = a_la_b_mod_c(y, m, n)
    u_la_r = a_la_b_mod_c(u, r, n)
    c = (y_la_m * u_la_r) % n
    return c

def decriptare_benaloh(c, r, n, phi_n, x):
    exponent = phi_n // r
    a = a_la_b_mod_c(c, exponent, n)
    for m in range(r):
        if a_la_b_mod_c(x, m, n) == a:
            return m
    return None

p = 11
q = 7
r = 5
y = 2

n, phi_n, x = generare_chei_benaloh(p, q, r, y)
print(f"Cheia publica: y = {y}, r = {r}, n = {n}")
print(f"Cheia privata: phi_n = {phi_n}, x = {x}")

mesaj = 3
u = 4

criptat = criptare_benaloh(mesaj, r, n, y, u)
print(f"Mesaj original: {mesaj}")
print(f"Mesaj criptat: {criptat}")

decriptat = decriptare_benaloh(criptat, r, n, phi_n, x)
print(f"Mesaj decriptat: {decriptat}")