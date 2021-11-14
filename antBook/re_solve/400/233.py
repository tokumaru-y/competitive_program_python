# https://atcoder.jp/contests/abc022/tasks/abc022_b
N=int(input())
S=[int(input()) for _ in range(N)]
passed = [False] * (10**5+1)
ans = 0
for s in S:
    s-=1
    if passed[s]:ans+=1
    passed[s]=True
print(ans)