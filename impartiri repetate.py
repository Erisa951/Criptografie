import math

def prim(n):
    if n in [0,1]: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3,math.floor(n**0.5),2):
        if n % i == 0: return False
    return True


print(prim(25))