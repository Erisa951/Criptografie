def a_la_b_mod_c(a,b,c):
    a%= c
    p = 1
    while b:
        if b%2==1:
            p = (p*a)%c;
        a = (a*a)%c;
        b //= 2
    return p

print(a_la_b_mod_c(9,15,7))