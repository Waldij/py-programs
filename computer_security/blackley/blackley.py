import math
import numpy as np

def gcd_extended(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)

def mod (x, p):
    assert p > 0
    if (x > 0):
        return x % p
    else:
        return (x + p * (-x // p) + p) % p

def lcm (a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)

def blackley (x1, x2, x3, p):
    print ("Восстановим исходную координату и секрет:")

    print ("Получаем систему:")
    x1 = np.array (x1)
    x2 = np.array (x2)
    x3 = np.array (x3)
    m = np.array ([x1, x2, x3])
    for i in range (3):
        print ("{}x + {}y + {}z + {} = 0 mod{}".format(m[i][0], m[i][1], m[i][2], m[i][3], p))

    x1 = np.array (x1)
    x2 = np.array (x2)
    x3 = np.array (x3)
    m = np.array ([x1, x2, x3])
    for i in range (3):
        m[i][3] = mod (-m[i][3], p);
    print ("Или /*вместо квадратных скобок круглые, стоблец свободных членов отделять чертой как в линале*/:\n", m)

    print ("Решаем методом Гаусса:")
    str1 = [0, 0, 1, 2, 2, 1]
    str2 = [1, 2, 2, 1, 0, 0]
    row = [0, 0, 1, 2, 2, 1]

    print (m)
    print ("~")
    for i in range (6):
        if (m[str2[i]][row[i]]) == 0:
            continue
        step = lcm (m[str1[i]][row[i]], m[str2[i]][row[i]])
        m1 = step / m[str1[i]][row[i]]
        m2 = step / m[str2[i]][row[i]]
        for j in range (4):
            diff = m[str2[i]][j] * m2 - m[str1[i]][j] * m1
            m[str2[i]][j] = mod (diff, p)
        if (i != 0 and i != 3):
            print (m)
            if (i != 5):
                print ("~")

    print ("Осталось вычислить обратные элементы с помощью расширенного алгоритма Евклида:")
    ans = list ()
    for i in range (3):
        reverse = gcd_extended (m[i][i], p)[1]
        ans.append (mod (m[i][3] * reverse, p))
    print ("(x, y, z)^T = ", ans)
    return

def main ():
    print ("Схема Блэкли (разделение секрета):")
    #взять из условия задачи:
    x1 = [5, 10, 3, 3]  #след №1
    x2 = [8, 2, 10, 1]  #след №2
    x3 = [4, 9, 2, 8]  #след №3
    x4 = [2, 3, 4, 10]  #след №4, может быть в задаче, но всё равно не будет использоваться
    p = 11  #модуль, из условия

    blackley (x1, x2, x3, p)
    return

if __name__ == "__main__":
  main ()
