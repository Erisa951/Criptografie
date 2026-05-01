def cmmdc(a, b):
    if a<0: a = -a
    if b<0: b = -b
    if a==0 or b==0: return a+b
    while (b):
        r = a%b; a = b; b = r
    return a

print(cmmdc(21,5))