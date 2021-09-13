# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0009&lang=jp
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
prime_list = Eratosthenes(10**6)
cnt = [0] * (10**6+1)
for i in range(10**6):
    cnt[i+1]=cnt[i]
    if prime_list[i+1]:cnt[i+1]+=1
while True:
    try:
        n=int(input())
    except:
        exit()
    print(cnt[n])