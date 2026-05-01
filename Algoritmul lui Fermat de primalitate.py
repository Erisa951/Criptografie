import random

def cmmdc(a, b):
    if a<0: a = -a
    if b<0: b = -b
    if a==0 or b==0: return a+b
    while (b):
        r = a%b; a = b; b = r
    return a

def a_la_b_mod_c(a,b,c):
    a%= c
    p = 1
    while b:
        if b%2==1:
            p = (p*a)%c;
        a = (a*a)%c;
        b //= 2
    return p

def test_Fermat(n, nr_incercari):
    if (n == 2): return True
    if (n % 2 == 0): return False
    for i in range(nr_incercari):
        b = random.randint(2,n-2)
        if (cmmdc(b, n) != 1): return False
        if (a_la_b_mod_c(b, n - 1, n) != 1): return False
    return 1

n = int(input("Dati numarul n:"))
nr_incercari = int(input("Dati numarul de incercari:"))
if (test_Fermat(n, nr_incercari)):
    print(f"\nNumarul {n} poate fi prim")
else:
    print(f"\nNumarul {n} este compus")