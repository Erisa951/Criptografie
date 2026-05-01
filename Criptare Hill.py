from sympy import Matrix

def citeste_alfabet(fisier_alfabet):
    with open(fisier_alfabet, "r", encoding="utf-8") as f:
        alfabet = f.read().strip()
    return tuple(alfabet)

def criptare_Hill(text, n, a, b, alfabet):
    N = len(alfabet)
    char_to_index = {c: i for i, c in enumerate(alfabet)}
    if len(text) % n != 0:
        text += alfabet[0] * (n - len(text) % n)
    rezultat = ""

    for j in range(0, len(text), n):
        bloc = text[j:j + n]
        mesaj = Matrix([char_to_index[c] for c in bloc])
        criptat = (a * mesaj + b) % N
        for c in criptat:
            rezultat += alfabet[int(c)]
    return rezultat

alfabet = citeste_alfabet("alfabet.txt")
text = "NOANSWER"
a = Matrix([[2, 3],
            [7, 8]])
b = Matrix([[0],
            [0]])
criptare = criptare_Hill(text, 2, a, b, alfabet)
print("Criptat:", criptare)
N = len(alfabet)
a_prim = a.inv_mod(N)
b_prim = (-a_prim * b) % N
decriptare = criptare_Hill(criptare, 2, a_prim, b_prim, alfabet)
print("Decriptat:", decriptare)