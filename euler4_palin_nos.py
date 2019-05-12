# euler 4

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palin(num):
    N = str(num)
    ln = len(N)
    ln2 = int(ln/2)
    if len(N)%2 == 0:
        A, B = N[:ln2], N[ln2:][::-1]
    else:
        A, B = N[:ln2], N[ln2+1:][::-1]
    if A == B:
        return True
    return False

palin_list = []
for i in range(800,1000):
    for j in range(800, 1000):
        candidate = i*j
        if is_palin(candidate):
            palin_list.append(candidate)

print(max(palin_list))