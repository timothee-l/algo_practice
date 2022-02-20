# Goal: Compute number of comparisons
# to sort list with QuickSort and compare different
# methods to choose a pivot.

# Count comparisons : Add m-1 to the comparison count
# for every recursive call of length m.

import numpy as np

A = np.loadtxt("QuickSort.txt", dtype="int").tolist()
n = len(A)
total = 0  # Global number of comparisons


# 1. Pivot is always first element of the array
def choose_pivot_1(f, k):
    return f


# 2. Pivot is always last element of the array
def choose_pivot_2(f, k):
    return f + k - 1


# 3. Median of three
def choose_pivot_3(f, k):
    P = [A[f], A[f + ((k - 1) // 2)], A[f + k - 1]]
    # Median value is chosen as pivot
    P.sort()
    if P[1] == A[f]:
        return f
    elif P[1] == A[f + k - 1]:
        return f + k - 1
    else:
        return f + ((k - 1) // 2)


def quick_sort(f, k):
    if k <= 1:
        return
    global total
    global A
    total += k - 1

    l = choose_pivot_3(f, k)

    # Swap pivot in first place
    A[f], A[l] = A[l], A[f]

    # Partition subroutine
    p = A[f]
    r = f + k - 1
    i = f + 1
    for j in range(f + 1, r + 1):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1

    # Swap pivot again
    A[f], A[i - 1] = A[i - 1], A[f]

    # Recursive calls
    fA, fB = f, i
    lenA = i - 1 - f
    lenB = r - i + 1
    # print("first call: first=", fA, " len=", lenA)
    # print("second call: second=", fB, " len=", lenB)
    quick_sort(fA, i - 1 - f)
    quick_sort(fB, r - i + 1)


def check_sort():
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            print("err")


f0 = 0
k0 = len(A)
quick_sort(f0, k0)
check_sort()
# 1. 162085 comparisons
# 2. 164123
# 3. 138382
print(total)
