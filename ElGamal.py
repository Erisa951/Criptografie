import random


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


def prim(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def test_Fermat(n, nr_incercari):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(nr_incercari):
        b = random.randint(2, n - 1)
        if cmmdc(b, n) != 1:
            return False
        if a_la_b_mod_c(b, n - 1, n) != 1:
            return False
    return True


def check_prime(n, nr_incercari=3):
    return test_Fermat(n, nr_incercari) and prim(n)


def give_prime(minim, maxim, value):
    if minim > maxim:
        return None
    if minim == maxim:
        if check_prime(minim):
            return minim
        else:
            return None

    nrAleator = random.randint(minim, maxim)
    for p in range(nrAleator, maxim + 1):
        if check_prime(p) and p != value:
            return p

    for p in range(minim, maxim):
        if check_prime(p) and p != value:
            return p

    return None


def transforma_din_baza_10(numar, alfabet):
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


def get_text(fisier_sursa):
    with open(fisier_sursa, "r", encoding="utf-8") as f:
        text = f.read()
    return text


def write_text(fisier_destinatie, text):
    with open(fisier_destinatie, "w", encoding="utf-8") as f:
        f.write(text)


def generare_chei_ElGamal(p, g):
    a = random.randint(1, p - 2)
    alpha = a_la_b_mod_c(g, a, p)
    cheie_publica = (p, g, alpha)
    cheie_privata = a
    return cheie_publica, cheie_privata


def cripteaza_ElGamal(text, cheie_publica, alfabet, j=1, lungime_l=2, k_fixat=None):
    p, g, alpha = cheie_publica
    rezultat_u = ""
    rezultat_v = ""

    k = k_fixat

    if len(text) % j != 0:
        text += alfabet[0] * (j - len(text) % j)

    for idx in range(0, len(text), j):
        bloc_clar = text[idx: idx + j]
        m = transforma_in_baza_10(bloc_clar, alfabet)

        if k_fixat is None:
            k = random.randint(1, p - 2)
            while cmmdc(k, p - 1) != 1:
                k = random.randint(1, p - 2)

        u = a_la_b_mod_c(g, k, p)
        alpha_k = a_la_b_mod_c(alpha, k, p)
        v = (m * alpha_k) % p

        text_u = transforma_din_baza_10(u, alfabet)
        if len(text_u) != lungime_l:
            text_u = alfabet[0] * (lungime_l - len(text_u)) + text_u
        rezultat_u += text_u

        text_v = transforma_din_baza_10(v, alfabet)
        if len(text_v) != lungime_l:
            text_v = alfabet[0] * (lungime_l - len(text_v)) + text_v
        rezultat_v += text_v

    return rezultat_u, rezultat_v


# decriptare
def decripteaza_ElGamal(cripto_u, cripto_v, cheie_privata, p, alfabet, j=1, lungime_l=2):
    a = cheie_privata
    rezultat = ""
    for idx in range(0, len(cripto_u), lungime_l):
        bloc_u = cripto_u[idx: idx + lungime_l]
        bloc_v = cripto_v[idx: idx + lungime_l]

        u = transforma_in_baza_10(bloc_u, alfabet)
        v = transforma_in_baza_10(bloc_v, alfabet)

        w = a_la_b_mod_c(u, p - 1 - a, p)

        m = (v * w) % p

        bloc_m = transforma_din_baza_10(m, alfabet)
        if len(bloc_m) != j:
            bloc_m = alfabet[0] * (j - len(bloc_m)) + bloc_m

        rezultat += bloc_m

    return rezultat


p = 2357
g = 2

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"

print("\n--- 1. GENERARE CHEI ---")
cheie_pub, cheie_priv = generare_chei_ElGamal(p, g)
print(f"Cheia Publică (p={cheie_pub[0]}, g={cheie_pub[1]}, alpha={cheie_pub[2]}, a = {cheie_priv})")

mesaj = "ANA_ARE_PERE"
print(f"\nMesaj original: {mesaj}")

k_ales = 3
u2, v2 = cripteaza_ElGamal(mesaj, cheie_pub, alfabet, j=2, lungime_l=3, k_fixat=k_ales)

print(f"{u2}")
print(f"{v2}")

mesaj_dec2 = decripteaza_ElGamal(u2, v2, cheie_priv, p, alfabet, j=2, lungime_l=3)
print(f"Mesaj Decriptat: {mesaj_dec2}")
