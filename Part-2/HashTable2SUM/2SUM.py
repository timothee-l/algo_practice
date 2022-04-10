import bisect as bi

A = set()  # Set of input numbers (ignores duplicates)

with open('input.txt', 'r') as file:
    for line in file:
        A.add(int(line))

tMin = -10000
tMax = 10000

# Goal : find all t in T = [|-tMin, tMax|] where t is the sum of 2 values

# All values of A not in T
B = [i for i in A if i > 0]  # Positive values
B = sorted(B)
C = [i for i in A if i < 0]  # Negative values
C = sorted(C)
# So any t must be the sum of b + c, with b,c in B,C

validTargets = set()  # No duplicates (ignores additional pairs)

for b in B:  # O(n)
    # Using bisect :
    #   - search for first index i in C where C[i]+b >= tMin
    #   - search for last index j in C where C[j]+b <= tMax
    i = bi.bisect_right(C, tMin - b)  # O(log n)
    j = bi.bisect_left(C, tMax - b)  # O(log n)
    for c in C[i:j]:  # O(1)
        # For all i<=k<j, insert C[k] in validTargets
        validTargets.add(b + c)  # O(1) insert

print(len(validTargets))

# Running time is O(n*log(n))
