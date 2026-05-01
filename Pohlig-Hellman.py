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

def descompunere_in_factori_primi(n):
    factori = []
    d = 2
    while n > 1:
        e = 0
        while n % d == 0:
            e += 1
            n = n // d
        if e > 0:
            factori.append((d, e))
        d += 1
        if d * d > n:
            if n > 1:
                factori.append((n, 1))
            break
    return factori

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

def cauta_logaritm_baza(baza, tinta, p, q):
    valoare = 1
    for d_k in range(q):
        if valoare == tinta:
            return d_k
        valoare = (valoare * baza) % p
    return None

def pohlig_hellman_pe_factor(g, h, p, N, q, e):
    c = a_la_b_mod_c(g, N // q, p)
    x_qi = 0
    q_la_k = 1
    h_k = h
    for k in range(e):
        putere_h = N // (q_la_k * q)
        tinta = a_la_b_mod_c(h_k, putere_h, p)
        d_k = cauta_logaritm_baza(c, tinta, p, q)
        if d_k is None:
            return None
        x_qi = x_qi + d_k * q_la_k
        putere_g = d_k * q_la_k
        termen_de_scazut = a_la_b_mod_c(g, putere_g, p)
        inv_termen = invers(termen_de_scazut, p)
        h_k = (h_k * inv_termen) % p
        q_la_k = q_la_k * q
    return x_qi

def pohlig_hellman(g, h, p):
    N = p - 1
    factori = descompunere_in_factori_primi(N)
    resturi = []
    moduli = []
    for factor in factori:
        q = factor[0]
        e = factor[1]
        x_qi = pohlig_hellman_pe_factor(g, h, p, N, q, e)
        modul_curent = 1
        for i in range(e):
            modul_curent = modul_curent * q
        resturi.append(x_qi)
        moduli.append(modul_curent)
    return teorema_chineza_a_resturilor(resturi, moduli)

def generare_chei_elgamal(p, g, x_privat):
    h = a_la_b_mod_c(g, x_privat, p)
    return h

def criptare_elgamal(m, p, g, h_public, k_aleator):
    C1 = a_la_b_mod_c(g, k_aleator, p)
    h_la_k = a_la_b_mod_c(h_public, k_aleator, p)
    C2 = (m * h_la_k) % p
    return C1, C2

def decriptare_elgamal(C1, C2, p, x_privat):
    C1_la_x = a_la_b_mod_c(C1, x_privat, p)
    inv_C1_la_x = invers(C1_la_x, p)
    m_decriptat = (C2 * inv_C1_la_x) % p
    return m_decriptat

p = 53
g = 5
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

x_Alice = 17
h_Alice = generare_chei_elgamal(p, g, x_Alice)
print(f"[ALICE] A generat cheia publică: h = {h_Alice}")

mesaj = 7
k_Bob = 11

C1, C2 = criptare_elgamal(mesaj, p, g, h_Alice, k_Bob)
print(f"[BOB] A criptat mesajul si a obtinut: C1={C1}, C2={C2}")

m_legitim = decriptare_elgamal(C1, C2, p, x_Alice)
print(f"[ALICE] A decriptat legitim pachetul si a obtinut litera index: {m_legitim}")

x_furat = pohlig_hellman(g, h_Alice, p)
print(f"[HACKER] A ghicit cheia privată folosind Pohlig-Hellman: x = {x_furat}")

if x_furat is not None:
    m_furat = decriptare_elgamal(C1, C2, p, x_furat)
    print(f"[HACKER] A decriptat mesajul interceptat si a obtinut litera index: {m_furat}")