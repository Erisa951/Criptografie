def a_la_b_mod_c(a, b, c):
    p = 1
    while b:
        if b % 2 == 1:
            p = (p * a) % c
        a = (a * a) % c
        b //= 2
    return p

def legendre(a, p):
    ls = a_la_b_mod_c(a, (p - 1) // 2, p)
    if ls == p - 1:
        return -1
    return ls

def gaseste_x(p, q):
    N = p * q
    x = 2
    while x < N:
        if legendre(x, p) == -1 and legendre(x, q) == -1:
            return x
        x += 1
    return None

def generare_chei_gm(p, q):
    N = p * q
    x = gaseste_x(p, q)
    return N, x

def criptare_gm(biti, N, x, y_list):
    cifrat = []
    for i in range(len(biti)):
        y = y_list[i]
        y_patrat = (y * y) % N
        if biti[i] == 1:
            c = (y_patrat * x) % N
        else:
            c = y_patrat
        cifrat.append(c)
    return cifrat

def decriptare_gm(cifrat, p, q):
    decriptat = []
    for c in cifrat:
        l = legendre(c, p)
        if l == 1:
            decriptat.append(0)
        else:
            decriptat.append(1)
    return decriptat

p = 7
q = 11

N, x = generare_chei_gm(p, q)
print(f"Cheia publica: N = {N}, x = {x}")
print(f"Cheia privata: p = {p}, q = {q}")

mesaj_biti = [1, 0, 1, 1, 0]
y_list = [15, 23, 31, 45, 50]

criptat = criptare_gm(mesaj_biti, N, x, y_list)
print(f"Mesaj original (biti): {mesaj_biti}")
print(f"Mesaj criptat: {criptat}")

decriptat = decriptare_gm(criptat, p, q)
print(f"Mesaj decriptat (biti): {decriptat}")