def factorizare(n):
    descompunere = [[], []]
    if n % 2 == 0:
        descompunere[0].append(2)
        exp = 0
        while n % 2 == 0:
            exp += 1
            n //= 2
        descompunere[1].append(exp)

    i = 3
    while i <= n:
        if n % i == 0:
            descompunere[0].append(i)
            exp = 0
            while n % i == 0:
                exp += 1
                n //= i
            descompunere[1].append(exp)
        i += 2

    return descompunere


n = 45
a = factorizare(n)
for i in range(len(a[0])):
    print(f"{a[0][i]} la puterea {a[1][i]}")