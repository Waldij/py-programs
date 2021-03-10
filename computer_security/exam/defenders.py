import math

def inverse(x, m):
    if x == 0:
        return None
    x = math.fmod(x, m)
    for i in range(1, int(m)):
        if x*i % m == 1:
            return i

def log(dig, osn, m):
    i = 1
    while osn**i % m != dig:
        i += 1
        if i > m*20:
            return 0
    return i

def sqrt(count, m, step = 2):
    result = []
    for dig in range(m):
        if dig**step % m == count:
            result.append(dig)
    return result

def delen(x, y, m):
    return x*inverse(y, m) % m


def summa(P, Q, p, a, b):
    if (P[0]==Q[0] and P[1]==Q[1]):
        lmb = "{}/{}".format((3*(P[0]**2)+a), (2*P[1]))
    else:
        lmb = "{}/{}".format((Q[1]-P[1]), (Q[0]-P[0]))
    lmb = lmb.split('/')
    if int(lmb[1]) % p == 0:
        return 0
    lmb = delen(int(lmb[0]), int(lmb[1]), p)
    x = lmb**2-P[0]-Q[0]
    y = -P[1]+lmb*(P[0]-x)
    x = x%p
    if x > p-x:
        x = x-p
    y = y%p
    if y > p-y:
        y = y-p
    return (x, y)

def mul(A, m, p, a, b):
    B = A
    for i in range(m-1):
        B = summa(A, B, p, a, b)
    return B

def get_dot_poryadok(A, p, a, b):
    m = 1
    B = 1
    while B != 0:
        B = mul(A, m, p, a, b)
        m += 1
    return m-1

def all_curve_dots(a, b, p):
    result = list()
    for x in range(p):
        y_2 = (x**3 + a*x + b) % p
        y = sqrt(y_2, p, step=2)
        result.append((x, y))
        print("x = {}, y^2 = {}, y = {}".format(x, y_2, y))
    return result

def GOST(Q, G, m, a, b, p, q, k):
    M = (0, 0)
    d = 1
    while M != Q and (M[0]%p, M[1]%p) != Q:
        M = mul(G, d, p, a, b)
        if M == 0:
            return None
        d += 1
    d -= 1
    print("Используя формулу Q = d*G перебором находим d = {}".format(d))
    C = mul(G, k, p, a, b)
    print("C = k*G = {}*{} = {}".format(k, G, C))
    r = (C[0] % p) % q
    print("r = x_c mod q = {} mod {} = {}".format(C[0]%p, q, r))
    e = m % q
    print("e = m mod q = {} mod {} = {}".format(m, q, e))
    s = (r*d + k*e) % q
    print("Подпись: s = (rd+ke) mod q = ({}*{} + {}*{}) mod {} = {}".format(r, d, k, e, p, s))
    return (C[0]%p, s)

def DiffieHelm(g, p, a, b):
    print("Alice private key = log_g(a) mod p = {}".format(log(a, g, p)))
    print("Bob private public key = log_g(b) mod p = {}".format(log(b, g, p)))
    return(log(a, g, p), log(b, g, p))

def elem_count(elem, x_1, x_2, x_3):
    return elem[0] * x_1 + elem[1] * x_2 + elem[2] * x_3 + elem[3]

def Blackley(first, second, third, p):
    for x_1 in range(p):
        for x_2 in range(p):
            for x_3 in range(p):
                if elem_count(first, x_1, x_2, x_3) % p == 0 and elem_count(second, x_1, x_2, x_3) % p == 0 and elem_count(third, x_1, x_2, x_3) % p == 0:
                    return (x_1, x_2, x_3)

def Shamir(teny, p):
    M = 0
    for i in range(len(teny)):
        mult = 1
        for j in range(len(teny)):
            if i == j:
                continue
            mult *= delen(teny[j][0], (teny[j][0]-teny[i][0]), p)
        M += teny[i][1]*mult % p
    return M % p


R = (16, 8) #dot1
P = (16, 8) #dot2
p = 17 #modul
a=-1 #1 coef of ellyptic curve
b=-4 #2 coef of ellyptic curve
print("poryadok", get_dot_poryadok(P, p, a, b))
print("summ", summa(P, R, p, a, b))
Q = (11, 6)
G = (7, 13)
q = 15
k = 4
m = 5
p = 17
a = -4
b = -10

print("GOST", GOST(Q, G, m, a, b, p, q, k))

g = 12
p = 17
a = 8
b = 3

DiffieHelm(g, p, a, b)
a = -12
b = -15
p = 17
print(all_curve_dots(a, b, p))

teny = ((3, 2), (4, 9), (5, 4))
p = 11
print("Shamir: ",Shamir(teny, p))