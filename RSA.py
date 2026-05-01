import random
import math
from collections import namedtuple

def citeste_alfabet(fisier_alfabet):
    with open(fisier_alfabet, "r", encoding="utf-8 ") as f:
        alfabet = f.read().strip()
    alfabet = tuple(alfabet)
    return alfabet

def cmmdc(a, b):
    if a < 0: a = -a
    if b < 0: b = -b
    if a == 0 or b == 0: return a + b
    while b:
        r = a % b
        a = b
        b = r
    return a

def a_la_b_mod_c(a, b, c):
    a %= c
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
    if n == 0 or n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True

def test_Fermat(n, nr_incercari):
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(nr_incercari):
        b = random.randint(2, n - 1)
        if cmmdc(b, n) != 1: return False
        if a_la_b_mod_c(b, n - 1, n) != 1: return False
    return True

def check_prime(n, nr_incercari=3):
    return test_Fermat(n, nr_incercari) and prim(n)

def give_prime(minim, maxim, value):
    if minim > maxim: return None
    if minim == maxim:
        if check_prime(minim): return minim
        else: return None
    nrAleator = random.randint(minim, maxim)
    for p in range(nrAleator, maxim + 1):
        if check_prime(p) and p != value: return p
    for p in range(minim, maxim):
        if check_prime(p) and p != value: return p
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

RSAKey = namedtuple("RSAKey", ["n", "e", "d", "l", "j", "alfabet"])

def generare_RSAkey(j=0, l=0, alfabet=None):
    p = give_prime(2, 100000, 2)
    q = give_prime(2, 100000, p)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(3, phi - 1)
    d = invers(e, phi)
    while d is None:
        e += 1
        d = invers(e, phi)
    if alfabet is not None and (j == 0 and l == 0):
        N = len(alfabet)
        j = int(math.log(n, N))
        l = j + 1
    cheie = RSAKey(n=n, e=e, d=d, j=j, l=l, alfabet=alfabet)
    return cheie


def RSA(text, key):
    rezultat = ""
    if len(text) % key.j != 0:
        text += key.alfabet[0] * (key.j - len(text) % key.j)
    for k in range(0, len(text), key.j):
        bloc = text[k:k + key.j]
        m = transforma_in_baza_10(bloc, key.alfabet)
        m = a_la_b_mod_c(m, key.e, key.n)
        m = transforma_din_baza_10(m, key.alfabet)
        if len(m) != key.l:
            m = key.alfabet[0] * (key.l - len(m)) + m
        rezultat += m
    return rezultat

def RSA_decrypt(text, key):
    rezultat = ""
    if len(text) % key.l != 0:
        return None
    for k in range(0, len(text), key.l):
        bloc = text[k:k + key.l]
        m = transforma_in_baza_10(bloc, key.alfabet)
        m = a_la_b_mod_c(m, key.d, key.n)
        m = transforma_din_baza_10(m, key.alfabet)
        if len(m) != key.j:
            m = key.alfabet[0] * (key.j - len(m)) + m
        rezultat += m
    return rezultat


n=2733
e=3
j=2
d=0
l=3
alfabet=citeste_alfabet("alfabet2.txt")
text="OK"
key=RSAKey(n,e,d, l, j, alfabet)
print(RSA(text,key))