import random
def a_la_b_mod_c(a,b,c):
    a%= c
    p = 1
    while b:
        if b%2==1:
            p = (p*a)%c;
        a = (a*a)%c;
        b //= 2
    return p

def test_Miller_Rabin(n, nr_incercari):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for _ in range(nr_incercari):
        s = 0
        t = n - 1
        b = random.randint(2, n - 2)
        while t % 2 == 0:
            s += 1
            t //= 2
        t = a_la_b_mod_c(b, t, n)
        if t != 1:
            while t != n - 1 and s > 1:
                t = (t * t) % n
                s -= 1
                if t == 1:
                    return False
            if t != n - 1:
                return False
    return True


n = int(input("Dati un numar natural nenul:"))
nr_incercari = int(input("Dati numarul maxim de incercari:"))
if test_Miller_Rabin(n, nr_incercari):
 print(f"Numarul {n} poate fi prim")
else:
 print(f"Numarul {n} nu este prim")