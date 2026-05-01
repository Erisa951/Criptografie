from collections import Counter

def citeste_alfabet(fisier_alfabet):
    with open(fisier_alfabet, "r", encoding="utf-8") as f:
        alfabet = f.read().strip()  # eliminam newline de la final
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


def vigenere_decrypt(text, cheie, alfabet):
    N = len(alfabet)
    rezultat = ""
    j = 0
    for ch in text:
        if ch in alfabet:
            x = alfabet.index(ch)
            k = alfabet.index(cheie[j % len(cheie)])
            rezultat += alfabet[(x - k) % N]
            j += 1
        else:
            rezultat += ch
    return rezultat


def gaseste_lungime_cheie(text, alfabet, lungime_max=20):
    chars = [ch for ch in text if ch in alfabet]

    best_lungime = 1
    best_ioc = 0

    for k in range(1, lungime_max + 1):
        subfluxuri = [[] for _ in range(k)]
        for i, ch in enumerate(chars):
            subfluxuri[i % k].append(ch)

        ioc_total = 0
        for subflux in subfluxuri:
            n = len(subflux)
            if n < 2:
                continue
            frecvente = Counter(subflux)
            ioc = sum(f * (f - 1) for f in frecvente.values()) / (n * (n - 1))
            ioc_total += ioc
        ioc_mediu = ioc_total / k

        if ioc_mediu > best_ioc:
            best_ioc = ioc_mediu
            best_lungime = k

    return best_lungime


def gaseste_cheie(text, lungime_cheie, alfabet):
    # Presupunem ca cel mai frecvent caracter din fiecare subflux = spatiu in clar
    N = len(alfabet)
    chars = [ch for ch in text if ch in alfabet]

    cheie = ""
    for i in range(lungime_cheie):
        subflux = [chars[j] for j in range(i, len(chars), lungime_cheie)]

        frecvente = get_frequencies(subflux)
        cel_mai_frecvent = frecvente.most_common(1)[0][0]

        y = alfabet.index(cel_mai_frecvent)
        x = alfabet.index(' ')  # spatiul e cel mai frecvent in romana
        k = (y - x) % N

        cheie += alfabet[k]

    return cheie


def vigenere_break(fisier_criptat, alfabet):
    text = get_text(fisier_criptat)

    #  gasim lungimea cheii
    lungime_cheie = gaseste_lungime_cheie(text, alfabet)

    chars = [ch for ch in text if ch in alfabet]
    for k in range(1, lungime_cheie):
        if lungime_cheie % k == 0:
            subfluxuri = [[] for _ in range(k)]
            for i, ch in enumerate(chars):
                subfluxuri[i % k].append(ch)
            ioc_total = 0
            for subflux in subfluxuri:
                n = len(subflux)
                if n < 2:
                    continue
                frecvente = Counter(subflux)
                ioc = sum(f * (f - 1) for f in frecvente.values()) / (n * (n - 1))
                ioc_total += ioc
            if ioc_total / k > 0.07:
                lungime_cheie = k
                break


    # gasim cheia
    cheie = gaseste_cheie(text, lungime_cheie, alfabet)

    # decriptam
    mesaj_clar = vigenere_decrypt(text, cheie, alfabet)

    write_text("destinatie_finala.txt", mesaj_clar)


alfabet = citeste_alfabet("alfabet1.txt")
vigenere_break("sursa.txt", alfabet)

#textul criptat:

"""
53:66DyoLUx'WE;S1Ddt'6)Hyq,lxKOELf1Hyw:6tKdt'6vTywLU(TVGfUtnclffxnV5:eMCOELjtS0E Wx'yn,64'y4:jtncpfU0DKx:6)DjlKgtQOEJaMROE!SvDyx:aMLewK66NK0KWtpywLU('XofX1DMlIWM'VEJS;mynLeMSY2 WtLypL8MCOJ:65'SEDS(DyoISzTVEGWMHX4IWvTdpfU;n!lIa;BKGfk1nM5D6)EK2:atnP5Jm4nbzKa1pylJSRLSEJXtQKt:61MSx:)6nWtEWMCOE.jtFY3KWtn!lIa;BKti6f'b4FjMHWtfW)SOEpm5MO(,mPnctke1nKoLUM'WtElxnMlfgw'dlh66NK0KWtpyw:67nMw:UtnNpfVxYQs'gv'dEGS8Tcz'8MH3lD6)BY3fEtQS5 S1neyfk7'bp 6wHXEJS6pyn:jxnO2:6)sYE;SzDytE6uNKw,68Dym'S:'ynFh1KKGfVxnXJ:kMESE!g)SypL6tBYwF7Mx3lGg1nflISOnSyfr1KOw,6wDy3:ju'dz:jxpynL6yDdpCWMOOE S5OSph68DynFd6HMpfk1nWl'6tKO3fh(HXECm6BSw,6)HyoLeuQK6'dxnMpCWMOVtEWMCOEDS6CbpKWOnN5GSMBew,kMQKn-a:HMlfVxnPl m:nQlCTxMOw,8MRY6:j nNpfm5OV5K6yKY2'8MCex;jtUXt 6)Hy3LdvHXlfVxnZ5J68QSyKjxnc4IS1D0E a6Dy5DT4'2E1g Dc4,SMBKyKWvTV5'4MzKJDSOn8z:e6D0EMS4nNpflxHyd'65sK2Lfv'3yKjxnPpDW1qyd'8MRM5IltnfzITtpy5EVxnO2:mMSbp'8MDeE,jtLylC68'd2Ldx'zEpS(nMlEVM'e(,S5nNpfdxFKy:lMBY0'd;K0EEmMRdtL6vTWE'e1nfpEWtmyn:U1ndz etHy0,65HXpfUtYe3,68'MlKm4nclfX1Tyx:aMLK2,61Md2,6yQK4'7MHX3:6vDypISMRKE!SvHyn:fwndpfj7'QlfetLKIf,tQytE6?HelfSvDOlh61Myn:jxnWlfj;FK3,6x'0E,jtneyfkxMSyfhxnMpI6)HylJSMCOE!j;LY3fk1nNpfUtKNE:XtQKGfUtsdtfnxMOlfktndpfkv'V('68Dy5JUtS0E SMFKtEa4DzE7S?'XofW;nYEMjxLOE SM'c4:8M'WEJhtQVtK)7nVlfTtKdlh6vTyr:fwnblL6tRe0ISMLKx,aOnMlK61LSE,jtnNpfetLKEJaMCOEEWv'TtKSNn5o,ntQy3Gm6pyn:U1n85DfxYO5fWMCOlJm8QKHf,xnVlfgMUbpDWOnWlDSOnM2,rtMNE SRRy0Ia6nVtMSw'y5EVxUKGfaxROE:XtQKEJaMHXn,hxnKEJl(HQlh6wDyo:6wTR5C6wHX4I)1Mcld6bNKy,9M2YlEWPn;z:fxqyTFS6D1EJaM2Yyh68'Mpi6o'jlEVMDKE SMMeE.S;nblJh;McE.WMMSn:axQSGfdtRKEKgtSOE'fMOKx:f:nctfkxnSlfV;OKEDa6Dyw:6u'V4:8MTXo,6)SSlfUtnWlfV;BxEJaOnMlEVMBYwF8MLKEMWwDy4Fd7FS4h6vTy0'W4DKE?gtKKEGWMMS3'hOnMlK65Hy4')1nQw'YtMewe6tOYth61My0'U1NK2,8MSStEVMKKELjxBRtfUtSOJF64Dc0,b7'blfX1Dbm'f:Dyo,64'y3FS(D0E mM'br'f:nZ2'f:Q3tEkxKOGJaM'MtfktQOlD61Md2km6nZt a7Q0E:U1nSyfUxKKw:d:pyl aMOVp S5nMlGm4nSyfV(DK0KSMRSE'fMRdlEYtpy3Gm6'XofU;USyKW4DwEmm('cGfhtBe2:kOnCnFS:DylGSMCSyfm(DMs'8MwKEKaRNSE.SMOK2:dxnfp Z1myd'6:H3z'6)OKw:6vNPpCWM:SEKaRNym:lxnNz;W4D1E
"""
#textul decriptat:

"""
Asa ne duceam baietii si fetele unii la altii cu lucrul, ca sa ne luam de urat,
ceea ce la tara se cheama sezatoare si se face mai mult noaptea, lucrand fiecare
al sau; cum torceam eu, de-a mai mare dragul pe intrecute cu Mariuca, si cum
sfaraia fusul rotii, asa-mi sfaraia inima-n mine de dragostea Mariucai! Martor
imi este Dumnezeu! si-mi aduc aminte ca odata, noaptea, la o claca de dezghiocat
papusoi, i-am scos Mariucai un soarec din san, care era s-o bage in boale pe
biata copila, de n-as fi fost eu acolo.
D-apoi vara, in zilele de sarbatoare, cu fetele pe campie, pe colnice si mai ales
prin luncile si dumbravile cele pline de mandrete, dupa cules rachitica de facut
galbenele, sovarv de umplut flori, dumbravnic si sulcina de pus printre straie,
cine umbla? Povestea cantecului: Fa-ma, Doamne, val de tei Si m-arunca-ntre femei!
Si, scurta vorba, unde erau trei, eu eram al patrulea. Dar cand auzeam de leganat
copilul, nu stiu cum imi venea; caci tocmai pe mine cazuse pacatul sa fiu mai mare
intre frati. Insa ce era sa faci cand te roaga mama? Dar in ziua aceea, in care ma
rugase ea, era un senin pe cer si asa de frumos si de cald afara, ca-ti venea sa te
scalzi pe uscat, ca gainile.
Vazand eu o vreme ca asta, am sparlit-o la balta, cu gand rau asupra mamei, cat imi
era de mama si de necajita. Adevar spun, caci Dumnezeu e deasupra! De la o vreme,
mama, crezand ca-s prin livada undeva, iese afara si incepe a striga, de da duhul
dintr-insa: Ioane! Ioane! Ioane! Ioane! si Ion, pace!
Vazand ea ca nu dau raspuns de nicaieri, lasa toate in pamant si se ia dupa mine la
balta, unde stia ca ma duc; si, cand colo, ma vede tologit, cu pielea goala pe nisip,
cat mi ti-i gliganul; apoi, in picioare, tiind la urechi cate-o lespejoara fierbinte
de la soare, cu argint printr-insele, si aci saream intr-un picior, aci in celalalt,
aci plecam capul in dreapta si in stanga, spunand cuvintele:
Auras, pacuras,Scoate apa din urechi,Ca ti-oi da parale vechi;
Si ti-oi spala cofele Si ti-o bate dobele!
"""