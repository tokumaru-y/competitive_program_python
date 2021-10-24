# https://atcoder.jp/contests/abc084/tasks/abc084_d
def Eratosthenes(num):
    """エラトステネスのふるい"""
    res = [True] * (num+1)
    res[0]=False
    res[1]=False
    for i in range(2, num + 1):
        if res[i]:
            k = i+i
            while k <= num:
                res[k]=False
                k+=i
    return res
Q=int(input())
prime_list = Eratosthenes(10**5)
cnt = [0] * (10**5+1)
for i in range(10**5):
    cnt[i+1] = cnt[i]
    if prime_list[i+1] and prime_list[(i+2)//2]:cnt[i+1]+=1
for _ in range(Q):
    l,r = list(map(int, input().split()))
    print(cnt[r] - cnt[l-1])
