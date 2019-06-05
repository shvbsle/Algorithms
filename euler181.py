# Euler 181
# gonna be auite challenging but let's give it a try atleast

'''
Having three black objects B and one white object W they can be grouped in 7 ways like this:

(BBBW)	(B,BBW)	(B,B,BW)	(B,B,B,W)	(B,BB,W)	(BBB,W)	(BB,BW)
In how many ways can sixty black objects B and forty white objects W be thus grouped?

This is definitely a counting problem. I just don't know how to count yet. So I'm gonna 
start brute force first
'''

nB, nW = 6,1

def unq(n):
    if n == 0:
        return 1
    ans = 0
    for i in range(1, int(n/2)+1):
        non_key = n-i
        ans+=unq(int(non_key/i))
    return 1+ans

print(unq(8))
