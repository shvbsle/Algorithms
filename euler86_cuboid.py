# euler 86

"""
Damnn this problem taught me a alotttt. Damnnnn OMfucking geeeee Damnnnn nibbazzz! figured it out mother fuckerssssss!!!!
Okay here is the theory behind the problem and how I solved it. I just needed to sit in a place and think properly for a sec...

For any triple P Q R, where P < Q <R; we wanna express P and Q as (a,b,c) such that a<=b<=c

Now, the shortest dist pair will be sqrt((a+b)**2+ c**2) because of our condition. So we don't really have to compute the distance as long
as abc are sorted.

if P & Q are less than the upper limit M:
    P can be expressed as: (a+b) and Q can be c
    or similarly
    P can be expressed as a and Q can be expressed as (b+c)
    for P, we can express a total of floor(P/2) unique splits
    and for Q we can express a total of floor(Q/2) unique splits

    but for Q we have to aware of a condition where, the splits of Q are smaller than P (cuz of a<=b<=c condition)
    so we eliminate all pairs for Q where smallest value is greater than P.

    For example:

    consider the triple (P,Q,R) == (6,8,10)

    P can be split into a total of floor(P/2) ways (3 ways):
    (1, 5)
    (2, 4)
    (3, 3)

    then pick any pair and it will satisfy the condition of:
    (a+b)**2+c**2 = R**2
    (1+5)**2+8**2 = 10**2

    But for splits of Q, we can see:
    (1,7) --> (1,7,6) (a<=b<=c fails here)
    (2,6) --> (2,6,6) a<=b<=c
    (3,5) --> (3,5,6) a<=b<=c
    (4,4) --> (4,4,6) a<=b<=c

    So we can't split Q as 1,7 as that will violate the condition.
    To count that out it is easy to see that No.of ways to skip = Q-P-1

    in this case it is: 8-6-1 = 1
    so total ways for Q = floor(Q/2)-(Q-P-1) = (8/2)-(1) = 3

    SO total unique pairs that can be generated for (6,8,10) is 3(for P) + 3(forQ) = 6

    if Q-P-1 <0 then don't count Q at all 
"""
import time
def pythagoreanTriplets(limits) : 
    c, m = 0, 2
    while c < limits : 
        for n in range(1, m) : 
            a = m * m - n * n 
            b = 2 * m * n 
            c = m * m + n * n 
            if c > limits : 
                break
            yield (a, b, c) 
        m = m + 1

start = time.time()
upper_lim = 1818

def count_combs(A, B, U):
    temp = 0
    if A<=U and B<=U:
        temp+=int(A/2)
        ways = B-A-1
        if (int(B/2)-ways)>=0:
            temp+=(int(B/2)-ways)
    if A<=U and B>U and int(B/2) <=U:
        ways = B-A-1
        if (int(B/2)-ways)>=0:
            temp+=(int(B/2)-ways)
    if A>U:
        temp =0
    return temp

is_triples={}
total_count = 0
xs = []
m2=set()
for a, b, c in pythagoreanTriplets(6700):
    S = [a,b,c]
    S.sort()
    for i in range(1,1000):
        A,B = i*S[0], i*S[1]
        if (A,B) in is_triples:
            continue
        X = count_combs(A, B, upper_lim)
        xs.append(X)
        total_count+=X
        is_triples[A,B]=True
print(total_count)
print("finished in: ", time.time()-start)