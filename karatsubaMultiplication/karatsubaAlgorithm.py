from math import *


# Karatsuba multiplication algorithm for two integers
# Complexity (worse case) is O(n^[log2(3)]) where n is the the number of digits in x or y (whichever is lowest)
def karatsuba(_x, _y):
    # 0. Base case

    if _x == 0 or _y == 0:
        return 0
    if _x < 10 or _y < 10:
        return _x * _y

    # 1. Split ints

    n_x = floor(log(_x, 10)) + 1  # number of digits in x
    n_y = floor(log(_y, 10)) + 1

    n = min(n_x, n_y)

    b = _x % (10 ** (n // 2))
    a = _x // (10 ** (n // 2))  # Regular division doesn't work (mantissa too small)
    d = _y % (10 ** (n // 2))
    c = _y // (10 ** (n // 2))

    # 2. Recursive calls

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    kara = karatsuba((a + b), (c + d))  # Trick to spare a recursive call

    res = ac * (10 ** (2 * (n // 2))) + (kara - ac - bd) * (10 ** (n // 2)) + bd
    # Note: Cannot use ac * (10 ** n), wrong when x or y have an odd number of digits

    return res


x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
a = karatsuba(x, y)
print(a)
print(a == x * y)