import random

def jacobi(a, n):
    if n == 1:
        return 1
    rezultat = 1
    while a != 0:
        while a % 2 == 0:
            a = a // 2
            if n % 8 == 3 or n % 8 == 5:
                rezultat = -rezultat
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            rezultat = -rezultat
        a = a % n
    if n == 1:
        return rezultat
    return 0

def solovay_strassen(n, k):
    for i in range(k):
        b = random.randint(1, n-1)
        if pow(b, (n-1)//2, n) != jacobi(b, n) % n:
            return "compus"
    return "probabil prim"


n = 11
rezultat = solovay_strassen(n, 5)
print("Numarul este:", rezultat)