# euler 6 to 10

# euler 6

N = 100
sum_sqr = sum([i*i for i in range(1, 101)])
sqr_sum = sum([i for i in range(1, 101)])**2
print("Euler 6:", sqr_sum - sum_sqr)

# euler 7


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    D = {}
    q = 2    
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1

counter = 0

# euler 8

input_str = """73167176531330624919225119674426574742355349194934,
96983520312774506326239578318016984801869478851843,
85861560789112949495459501737958331952853208805511,
12540698747158523863050715693290963295227443043557,
66896648950445244523161731856403098711121722383113,
62229893423380308135336276614282806444486645238749,
30358907296290491560440772390713810515859307960866,
70172427121883998797908792274921901699720888093776,
65727333001053367881220235421809751254540594752243,
52584907711670556013604839586446706324415722155397,
53697817977846174064955149290862569321978468622482,
83972241375657056057490261407972968652414535100474,
82166370484403199890008895243450658541227588666881,
16427171479924442928230863465674813919123162824586,
17866458359124566529476545682848912883142607690042,
24219022671055626321111109370544217506941658960408,
07198403850962455444362981230987879927244284909188,
84580156166097919133875499200524063689912560717606,
05886116467109405077541002256983155200055935729725,
71636269561882670428252483600823257530420752963450""".split(",\n")

input_str = ''.join(input_str)
n_list = []
for ind, char in enumerate(input_str):
    if ind <= len(input_str)-14:
        nums = list(input_str[ind: ind+13])
        num_prod = list(map(int, nums))
        N = 1
        for i in num_prod:
            N*=i
        n_list.append(N)
print("euler 8:",max(n_list))

# euler 9

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def is_py_trip(a, b, c):
    if a**2+b**2 == c**2:
        return [a,b,c]
    return False

N = 1000
trips = []
for i in range(1, 1000):
    right_half = N-i
    offset = i
    if i < int(N/2)+1:
        for j in range(1, 1002):
            mid_part = j+offset
            part3 = right_half-mid_part
            if mid_part < int(part3)+1:
                trips.append([i, mid_part, part3])
                if is_py_trip(i, mid_part, part3):
                    print("Euler 9:", i*mid_part*part3)
                    break

# Euler 10

up_lim = 2000000
# up_lim = 10
p_list = []
for p in gen_primes():
    if p<up_lim:
        p_list.append(p)
    else:
        break

print("Euler 10:", sum(p_list))



