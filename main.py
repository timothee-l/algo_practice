from math import *


def karatsuba(x, y):
    # 0. Base case

    if x <= 10 or y <= 10:
        # Base case
        return x * y

    # 1. Split ints

    n_x = ceil(log(x, 10))  # Nb of digits in x
    n_y = ceil(log(y, 10))

    n = max(n_x, n_y)

    b = x % (10 ** (n // 2))
    a = x // (10 ** (n // 2))  # si int(x / (10** (n//2))) => perte de précision sur le float d'où résultat
    # erronné si nombre très grand (imprécision sur la mantisse)
    d = y % (10 ** (n // 2))
    c = y // (10 ** (n // 2))
    #On peut aussi utiliser divmod

    # 2. Recursive calls

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    kara = karatsuba((a + b), (c + d))

    res = ac * (10 ** (2 * (n // 2))) + (kara - ac - bd) * (10 ** (n // 2)) + bd
    # ac * (10 ** (n//2)) ne fonctionne pas, pourquoi?

    return res


if __name__ == '__main__':
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    a = karatsuba(x, y)
    print(a)
    print(a == x * y)