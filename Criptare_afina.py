from collections import Counter

def citeste_alfabet(fisier_alfabet):
    with open(fisier_alfabet, "r", encoding="utf-8") as f:
        alfabet = f.read()
        alfabet = tuple(alfabet)
    return alfabet

def get_text(fisier_sursa):
    with open(fisier_sursa, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def write_text(fisier_destinatie, text):
    with open(fisier_destinatie, "w", encoding="utf-8") as f:
        f.write(text)

def get_frequencies(text):
    result = Counter()
    for ch in text:
        result[ch] += 1
    return result

def invers(a, N):
    x1 = 1; x2 = 0; copy = N
    while N:
        r = a % N
        x = x1 - (a // N) * x2; x1 = x2; x2 = x
        a = N; N = r
    if (a == 1): return x1 % copy
    return None

def affine_encrypt(text, a, b, alfabet):
    res = ""
    N = len(alfabet)
    for ch in text:
        x = alfabet.index(ch)
        res += alfabet[(a * x + b) % N]
    return res

def affine_break(fisier_criptat, alfabet):
    mesaj = get_text(fisier_criptat)
    frecvente = get_frequencies(mesaj).most_common()
    frecvent0 = frecvente[0][0]
    frecvent1 = frecvente[1][0]
    N = len(alfabet)

    y0 = alfabet.index(frecvent0)
    y1 = alfabet.index(frecvent1)
    x0 = alfabet.index(' ')
    x1 = alfabet.index('a')

    a = (invers((y0 - y1) % N, N) * (x0 - x1)) % N
    b = (x0 - a * y0) % N

    criptare = affine_encrypt(mesaj, a, b, alfabet)
    write_text("destinatie_finala.txt", criptare)
    print("Salvat în destinatie_finala.txt")

# Cod principal
# Cod principal
alfabet = citeste_alfabet("alfabet1.txt")

affine_break("sursa.txt", alfabet)