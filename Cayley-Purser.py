def a_la_b_mod_c(a, b, c):
    p = 1
    while b:
        if b % 2 == 1:
            p = (p * a) % c
        a = (a * a) % c
        b //= 2
    return p


def invers(a, N):
    copy_N = N
    x1 = 1
    x2 = 0
    while N:
        r = a % N
        x = x1 - (a // N) * x2
        x1 = x2
        x2 = x
        a = N
        N = r
    if a == 1:
        return x1 % copy_N
    return None


def inmultire_matrice(A, B, n):
    C = [[0, 0], [0, 0]]
    C[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % n
    C[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % n
    C[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % n
    C[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % n
    return C


def putere_matrice(A, k, n):
    P = [[1, 0], [0, 1]]
    B = [[A[0][0], A[0][1]], [A[1][0], A[1][1]]]

    while k > 0:
        if k % 2 == 1:
            P = inmultire_matrice(P, B, n)
        B = inmultire_matrice(B, B, n)
        k //= 2
    return P


def invers_matrice(A, n):
    det = (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % n
    det_inv = invers(det, n)
    if det_inv is None:
        return None

    B = [[0, 0], [0, 0]]
    B[0][0] = (A[1][1] * det_inv) % n
    B[0][1] = (-A[0][1] * det_inv) % n
    B[1][0] = (-A[1][0] * det_inv) % n
    B[1][1] = (A[0][0] * det_inv) % n

    B[0][1] = (B[0][1] + n) % n
    B[1][0] = (B[1][0] + n) % n
    return B


def generare_chei_cp(p, q, alpha, chi, r):
    n = p * q
    inv_chi = invers_matrice(chi, n)

    beta_temp = inmultire_matrice(inv_chi, alpha, n)
    beta = inmultire_matrice(beta_temp, chi, n)

    gamma = putere_matrice(chi, r, n)

    return n, beta, gamma


def criptare_cp(mu, n, alpha, beta, s):
    epsilon = putere_matrice(alpha, s, n)
    kappa = putere_matrice(beta, s, n)

    C_temp = inmultire_matrice(kappa, mu, n)
    C = inmultire_matrice(C_temp, kappa, n)

    return epsilon, C


def decriptare_cp(epsilon, C, n, chi):
    inv_chi = invers_matrice(chi, n)

    kappa_temp = inmultire_matrice(inv_chi, epsilon, n)
    kappa = inmultire_matrice(kappa_temp, chi, n)

    inv_kappa = invers_matrice(kappa, n)

    mu_temp = inmultire_matrice(inv_kappa, C, n)
    mu = inmultire_matrice(mu_temp, inv_kappa, n)

    return mu


p = 11
q = 13
alpha = [[2, 3], [1, 4]]
chi = [[5, 2], [3, 7]]
r = 4

n, beta, gamma = generare_chei_cp(p, q, alpha, chi, r)
print(f"Cheia publica: n={n}, alpha={alpha}, beta={beta}, gamma={gamma}")
print(f"Cheia privata: chi={chi}")

mu = [[7, 8], [9, 10]]
s = 5

epsilon, C = criptare_cp(mu, n, alpha, beta, s)
print(f"Mesaj original (matrice): {mu}")
print(f"Mesaj criptat: epsilon={epsilon}, C={C}")

mu_decriptat = decriptare_cp(epsilon, C, n, chi)
print(f"Mesaj decriptat (matrice): {mu_decriptat}")