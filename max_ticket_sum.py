# what an easy problem lol

a = "-1 7 8 -5 4"
a = "5 10 70 50 100 20 10 50"
a ="4 5 4 3"
# a = "3 2 1 -1"
# a= "11 12 -2 -1"
a = "2 0 5 7 -1 0 8 4 1 3 -2 0 0 2 -2"
# a = "-4 -5 -6 -7"/\
a = list(map(int, a.split()))

memo = {}
def msum(i, arr):
    if i<0:
        return (0, [])
    if i in memo:
        return memo[i]
    n1 = (arr[i], [arr[i]])
    n2_arr = msum(i-2, arr)
    n2 = (arr[i]+sum(n2_arr[1]), [arr[i]]+n2_arr[1])
    n3_arr = msum(i-1, arr)
    n3 = (sum(n3_arr[1]), n3_arr[1])
    memo[i] = max(n1, n2, n3)    
    return memo[i]

ans = msum(len(a)-1, a)
print(ans)
print(''.join(list(map(str, ans[1]))))
