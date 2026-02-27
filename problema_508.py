def litera_to_num(l):
    return ord(l.upper()) - ord('A')

def num_to_litera(n):
    return chr(n + ord('A'))

# 1. Adunare în baza 26
def adunare(a, b):
    max_len = max(len(a), len(b))
    a = a.rjust(max_len, 'A')
    b = b.rjust(max_len, 'A')
    rez = ""
    carry = 0
    for i in range(max_len - 1, -1, -1):
        s = litera_to_num(a[i]) + litera_to_num(b[i]) + carry
        rez = num_to_litera(s % 26) + rez
        carry = s // 26
    if carry > 0:
        rez = num_to_litera(carry) + rez
    return rez

# 2. Scădere în baza 26
def scadere(a, b):
    max_len = max(len(a), len(b))
    a = a.rjust(max_len, 'A')
    b = b.rjust(max_len, 'A')
    rez = ""
    borrow = 0
    for i in range(max_len - 1, -1, -1):
        x = litera_to_num(a[i])
        y = litera_to_num(b[i])
        if x - borrow >= y:
            diff = x - borrow - y
            borrow = 0
        else:
            diff = x - borrow + 26 - y
            borrow = 1
        rez = num_to_litera(diff) + rez
    rez = rez.lstrip('A')
    if rez == "":
        rez = 'A'
    return rez

# 3. Înmulțire în baza 26
def inmultire(a, b):
    a = a[::-1]
    b = b[::-1]
    res = ['A'] * (len(a) + len(b))
    for i in range(len(a)):
        carry = 0
        for j in range(len(b)):
            total = litera_to_num(a[i]) * litera_to_num(b[j]) + litera_to_num(res[i+j]) + carry
            res[i+j] = num_to_litera(total % 26)
            carry = total // 26
        res[i + len(b)] = num_to_litera(litera_to_num(res[i + len(b)]) + carry)
    res = "".join(res[::-1]).lstrip('A')
    if res == "":
        res = 'A'
    return res

# 4. Împărțire în baza 26 (simplificat)
def word_to_num(word):
    n = 0
    for c in word:
        n = n * 26 + litera_to_num(c)
    return n

def num_to_word(n):
    if n == 0:
        return 'A'
    res = ""
    while n > 0:
        res = num_to_litera(n % 26) + res
        n //= 26
    return res

def impartire(a, b):
    n1 = word_to_num(a)
    n2 = word_to_num(b)
    q = n1 // n2
    r = n1 % n2
    return num_to_word(q), num_to_word(r)

# Exemple
print(adunare("ZECE", "ZECE"))
print(scadere("CAB", "BA"))
print(inmultire("BAC", "D"))
q,r= impartire("CAB", "CAB")
print(q) #doar catul
print(q,r) #catul si restul