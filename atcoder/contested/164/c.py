N=int(input())
cnt = {}
for _ in range(N):
    s = input().rstrip()
    cnt[s]=1
print(len(cnt))