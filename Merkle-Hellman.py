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

def binar_pe_k_biti(numar, k):
    biti = []
    while numar > 0:
        biti.append(numar % 2)
        numar = numar // 2

    while len(biti) < k:
        biti.append(0)

    biti_inversati = []
    for i in range(len(biti) - 1, -1, -1):
        biti_inversati.append(biti[i])

    return biti_inversati


def transforma_din_binar_in_10(biti):
    rezultat = 0
    for bit in biti:
        rezultat = rezultat * 2 + bit
    return rezultat


def rezolva_rucsac(V, v):
    k = len(v)
    biti = [0] * k

    v_copie = []
    for x in v:
        v_copie.append(x)

    for pas in range(k):
        max_val = -1
        max_idx = -1

        for i in range(k):
            if v_copie[i] > max_val:
                max_val = v_copie[i]
                max_idx = i

        if V >= max_val:
            biti[max_idx] = 1
            V = V - max_val

        v_copie[max_idx] = -1

    return biti

def generare_cheie_publica(v, a, m):
    w = []
    for v_i in v:
        w.append((v_i * a) % m)
    return w

def refacere_sir_supercrescator(w, b, m):
    v = []
    for w_i in w:
        v.append((w_i * b) % m)
    return v

def criptare_mh(mesaj, w, alfabet):
    k = len(w)
    cifrat = []

    for litera in mesaj:
        idx = alfabet.index(litera)
        biti = binar_pe_k_biti(idx, k)
        c = 0
        for i in range(k):
            c = c + (biti[i] * w[i])
        cifrat.append(c)
    return cifrat


def decriptare_mh(cifrat, b, m, v, alfabet):
    decriptat = ""

    for c in cifrat:
        V = (c * b) % m
        biti = rezolva_rucsac(V, v)
        idx = transforma_din_binar_in_10(biti)
        decriptat += alfabet[idx]
    return decriptat

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

v_joi = [2, 7, 11, 21, 42]
m_joi = 881
a_joi = 588
mesaj_joi = "JOI"

w_joi = generare_cheie_publica(v_joi, a_joi, m_joi)

cifrat_joi = criptare_mh(mesaj_joi, w_joi, alfabet)
print(f"Mesaj in clar: {mesaj_joi}")
print(f"Mesaj criptat: {cifrat_joi}\n")

w_2 = [57, 14, 3, 24, 8]
b_2 = 23
m_2 = 61
cifrat_2 = [14, 25, 89, 3, 65, 24, 3, 49, 89, 24, 41, 25, 68, 41, 71]

v_2 = refacere_sir_supercrescator(w_2, b_2, m_2)

decriptat_2= decriptare_mh(cifrat_2, b_2, m_2, v_2, alfabet)

print(f"Mesaj cifrat primit: {cifrat_2}")
print(f"Mesaj decriptat rezultat: {decriptat_2}")