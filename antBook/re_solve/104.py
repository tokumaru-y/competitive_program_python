# https://atcoder.jp/contests/tenka1-2012-qualc/tasks/tenka1_2012_9
def Eratosthenes(num):
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
N=int(input())
prime = Eratosthenes(N)
prime[N]=False
ans = prime.count(True)
print(ans)