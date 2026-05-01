def citeste_alfabet(fisier_alfabet):
    with open(fisier_alfabet, "r", encoding="utf-8 ") as f:
        alfabet = f.read().strip()

    alfabet = tuple(alfabet)
    return alfabet


def transforma_din_baza_10(numar, alfabet) :
    rezultat = ""
    N = len(alfabet)
    while (numar > 0):
        rezultat += alfabet[numar % N]
        numar = numar // N
    return rezultat[::-1]

alfabet = citeste_alfabet("alfabet.txt")
print(transforma_din_baza_10(1041, alfabet))