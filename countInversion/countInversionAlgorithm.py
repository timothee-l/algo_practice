import numpy as np

A = np.loadtxt("IntegerArray.txt", dtype="int").tolist()
n = len(A)
D = np.linspace(1, n, n)  # D = [1, 2, ..., n]


# Function splits array L in half. If L is of uneven size, second half is larger.
def split_array(L, m):
    half = int(m // 2)
    odd = 0
    if m % 2 != 0:
        odd = 1
    return L[:half], L[half:], odd


# Function uses Merge Sort algorithm's merge step to count split inversions
# Split inversions are any (i,j) where sB[i] > sC[j]
def merge_count(sB, sC, m):
    i, j = 0, 0  # indexes for B and C respectively
    iMax, jMax = len(sB), len(sC)
    splitInv = 0
    sL = []  # Merged list
    for k in range(0, m):
        if i == iMax:
            sL.append(sC[j])
            j += 1
        elif j == jMax:
            sL.append(sB[i])
            i += 1
        elif sB[i] < sC[j]:
            sL.append(sB[i])
            i += 1
        else:  # sB[i] > sC[j]
            sL.append(sC[j])
            j += 1
            splitInv += iMax - i  # For every p in [i;iMax[, (sC[j], sB[p]) is an inversion.
    return sL, splitInv


# Algorithm counts inversions in L recursively
# Inversions are any (i,j), i < j, where L[i] > L[j]
# Complexity (worse case) is O(n*log(n))
def count_inv(L, m):
    if m == 1:  # Base case
        return L, 0
    else:  # Other cases
        B, C, odd = split_array(L, m)
        sB, x = count_inv(B, m // 2)  # Counts inversions in B
        sC, y = count_inv(C, odd + (m // 2))  # Counts inversions in C
        sL, z = merge_count(sB, sC, m)  # Counts split inversions between sorted B and sorted C
    return sL, (x + y + z)


inv = count_inv(A, n)[1]
print("Inversions in list: ", inv)
