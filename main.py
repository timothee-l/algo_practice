# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def karatsuba(x, y, initial=False):
    # todo: séparer les ints en 2 moitiés
    # todo: appels récursifs
    # todo: cas élémentaire
    # int en base 10, multiple de 2
    x_str = str(x)
    y_str = str(y)
    array_x = [n for n in x_str]
    array_y = [n for n in y_str]
    div = False
    if len(array_x) < len(array_y):
        array_x.append(0)
        div = True
    elif len(array_x) > len(array_y):
        array_y.append(0)
        div = True
    if (len(array_x) == len(array_y)) and (len(array_x) == 1):
        # x et y < 10
        return x * y
    # split
    a = 0
    b = 0
    n = max(len(array_x),len(array_y))
    for index, i in enumerate(array_x):
        if index < math.floor(n / 2):
            a *= 10
            a += int(i)
            print("a ", a)
        else:
            b *= 10
            b += int(i)
            print("b ", b)
    c = 0
    d = 0
    for index, i in enumerate(array_y):
        if index < math.floor(n / 2):
            c *= 10
            c += int(i)
            print("c ", c)
        else:
            d *= 10
            d += int(i)
            print("d ", d)
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    print("----")
    alpha = karatsuba(a, c)
    beta = karatsuba(b, d)
    # karatsuba:
    # gamma = karatsuba(a+b,c+d)
    # delta = gamma-beta-alpha
    # classique:
    delta = karatsuba(a, d) + karatsuba(b, c)
    eq1 = alpha * pow(10, n)
    eq2 = delta * pow(10, n // 2)
    res = eq1 + eq2 + beta
    if div:
        res/=10
    if initial:
        print("n: ",n)
        print("alpha", alpha)
        print("beta", beta)
        print("delta", delta)
    return res


x = 224
y = 369
print(karatsuba(x, y, True))
