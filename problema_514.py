def euler_phi(n):
    rezultat = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            rezultat = rezultat // p * (p - 1)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        rezultat = rezultat // n * (n - 1)
    return rezultat

print(euler_phi(123456789))
print(euler_phi(987654321098765))
print(euler_phi(1000000000039))
print(euler_phi(100))