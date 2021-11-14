# https://atcoder.jp/contests/agc014/tasks/agc014_b
N,M=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(M)]
cnt = [0] * N
for a,b in AB:
    a-=1
    b-=1
    cnt[a]+=1
    cnt[b]+=1
for i in range(N):
    if cnt[i]%2==1:
        print("NO")
        exit()
print("YES")