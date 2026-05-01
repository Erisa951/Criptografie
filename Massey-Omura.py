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


def transforma_din_baza_10(numar, alfabet):
    if numar == 0:
        return alfabet[0]
    rezultat = ""
    N = len(alfabet)
    while numar > 0:
        rezultat += alfabet[numar % N]
        numar = numar // N
    return rezultat[::-1]


def transforma_in_baza_10(numar, alfabet):
    rezultat = 0
    N = len(alfabet)
    for letter in numar:
        rezultat = rezultat * N + alfabet.index(letter)
    return rezultat


def massey_omura(text, p, eA, eB, alfabet):
    dA = invers(eA, p - 1)
    dB = invers(eB, p - 1)

    m = transforma_in_baza_10(text, alfabet)

    C1 = a_la_b_mod_c(m, eA, p)
    C2 = a_la_b_mod_c(C1, eB, p)
    C3 = a_la_b_mod_c(C2, dA, p)
    m_final = a_la_b_mod_c(C3, dB, p)

    text_final = transforma_din_baza_10(m_final, alfabet)

    return text_final


alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_?!."
p = 1000000007
eA = 3
eB = 5
mesaj = ("DA!")
rezultat = massey_omura(mesaj, p, eA, eB, alfabet)
print(f"Mesaj original: {mesaj}")
print(f"Mesaj obținut după algoritm: {rezultat}")