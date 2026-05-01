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

def decripteaza_matriceal(text, alfabet, idx):
    N = len(alfabet)

    chars = [ch for ch in text if ch in idx]

    # daca avem lungime impara, completam
    if len(chars) % 2 != 0:
        chars.append(alfabet[0])

    rezultat_plain = []

    for i in range(0, len(chars), 2):
        C1 = idx[chars[i]]
        C2 = idx[chars[i+1]]

        # Sistemul de criptare:
        #prin mai multe calcule si teste am ajuns la forma:
        #
        # C1 = 72*P1 + 1*P2 + 63 (mod N)
        # C2 =  0*P1 + 1*P2 + 62 (mod N)
        #
        # forma matriceala:
        # [C1]   [72 1] [P1] + [63]
        # [C2] = [0  1] [P2]   [62]
        #
        # Pas 1: eliminam vectorul constant:
        # C2 - 62 = P2  => putem afla direct P2
        #
        # Pas 2: inlocuim P2 in prima ecuatie:
        # C1 - 63 = 72*P1 + P2
        # => 72*P1 = C1 - 63 - P2
        #
        # Pas 3: inmultim cu inversul lui 72 mod N
        #
        # Observatie:
        # 72 ≡ -1 (mod 73)
        # inversul lui -1 este tot -1 => 72
        #
        # => P1 = 72 * (C1 - 63 - P2) mod N
        #

        # calcul P2
        P2 = (C2 - 62) % N

        # calcul P1
        P1 = (72 * (C1 - 63 - P2)) % N

        rezultat_plain.append(alfabet[P1])
        rezultat_plain.append(alfabet[P2])

    rezultat = []
    j = 0
    for ch in text:
        if ch in idx:
            rezultat.append(rezultat_plain[j])
            j += 1
        else:
            rezultat.append(ch)

    return ''.join(rezultat)

alfabet = citeste_alfabet("alfabet1.txt")
text = get_text("sursa.txt")

idx = {ch: i for i, ch in enumerate(alfabet)}

mesaj = decripteaza_matriceal(text, alfabet, idx)

write_text("decriptat.txt", mesaj)


#text criptat:
"""
cbK3!X9PbTuPld8PsPfX!iS8Q3sPuPrjR3Fg-X939PyTXPuTe39g.XcU9R!d2X(3GXZRuPCjT3;R?ae3zPW3Lk7PrjR3CgJia3zPW3zPyT939PyTbTuPfX eHgJifX!iS8Q3BasPqiHgg5jb-XaSBeHgsPsP(3GXfX eHgJi2a93CgJi?aa3Fg-X2azX93xTkc3b7PSKDg:TaX eHgJi:31XfX eHgJi2aSKDg:TkcK3Lk7PcU9R!d2X93!Xkc3b-XcUFib4JB2a0XXP6XqiyTIjuPiae37X;azRaSa39P1SXP;T:iW3CgJiW3?jjb-XXP(juPme2X4TV3e3xTfX!iBa6XXPzP1S5X(3IPuPskDg)X93 S5Re3(T!X g)XZRuPCj'jW31XcUFi?aa3.bwPuP:j'jY5kcK3xTskPo9ha36X!X0SJie3:TZRDcb3DgKjbTX4PHW3Ihe3uT6XfX eyTBjuPyTe3:Tkc5RW3.bwPuP:jT3'TxSa3?jZR4c.hwTe32T(d0XW3tPY5kc5RW3Fg-X2akcBexPwT4TphBaY1me'c9gK39PqiHge3,cZRHga3.bwPuPwTe3CgJi?aa3;TT3zPW3zPyTbTuPqizRzPW30PldjbHg;X2TXPmeCbDc:j'jY5phW3Fg-Xe3Ah:j aBaL30PldXP-ie3zP0V,cb4PHW3Fe5X930TskyT7X4TXP;T4Tg5jb-XqixPwTqiHg aa3DgKjYQDc:jBia3:TogPoDd-Xa3BgBoLkc5aS j-j2X4Tmea3Fea31Xmea39h9PL3DgKjme(i,cZR4c.hIjwTphW3'dHgwTfX0R8g9PwTphW3:TXP;T7PkcK3xTme(i7PZRBaJi gW3Ihe3:Trj7dN31XcUHge3;g.b,Y,XW39PfXR3uXrPaSa3IhsPuX(3GXZR,ca3FetRe3e3xTaStRa30TXP:j0RW3,c9ggdmeHgwTXPia3b)XXP:TxT gW3HjM3uPzP2Te3wPyPiae3;dHgwT)4(3
"""

#text decriptat:
"""
Amu cica era odata intr-o tara un crai, care avea trei feciori.
Si craiul acela mai avea un frate mai mare, care era imparat intr-o alta tara, mai departata.
Si imparatul, fratele craiului, se numea Verde-imparat; si imparatul Verde nu avea feciori, ci numai fete.
Multi ani trecura la mijloc de cand acesti frati nu mai avura prilej a se intalni amandoi.
Iara verii, adica feciorii craiului si fetele imparatului, nu se vazuse niciodata de cand erau ei.
Si asa veni imprejurarea de nici imparatul Verde nu cunostea nepotii sai, nici craiul nepoatele sale:
pentru ca tara in care imparatea fratele cel mai mare era tocmai la o margine a pamantului,
si craia istuilalt la o alta margine.
Si apoi, pe vremile acelea, mai toate tarile erau bantuite de razboaie grozave,
drumurile pe ape si pe uscat erau putin cunoscute si foarte incurcate
si de aceea nu se putea calatori asa de usor si fara primejdii ca in ziua de astazi.
Si cine apuca a se duce pe atunci intr-o parte a lumii adeseori dus ramanea pana la moarte...
"""