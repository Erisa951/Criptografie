from collections import Counter

def citeste_alfabet(fisier_alfabet):
    with open(fisier_alfabet, "r", encoding="utf-8") as f:
        alfabet = f.read().strip()
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

def cesar_encrypt(text, k, alfabet):
    res = ""
    N = len(alfabet)
    for ch in text:
        if ch in alfabet:
            res += alfabet[(alfabet.index(ch) + k) % N]
        else:
            res += ch
    return res

def cesar_break(fisier_criptat, alfabet):
    mesaj = get_text(fisier_criptat)
    frecvente = get_frequencies(mesaj)
    k = len(alfabet) - alfabet.index(max(frecvente, key=frecvente.get))
    criptare = cesar_encrypt(mesaj, k, alfabet)
    write_text("destinatie_finala.txt", criptare)

alfabet = citeste_alfabet("alfabet.txt")
k = int(input("Introdu cheia k: "))
mesaj = get_text("sursa.txt")
criptare = cesar_encrypt(mesaj, k, alfabet)
write_text("destinatie.txt", criptare)
print(criptare)

cesar_break("destinatie.txt", alfabet)