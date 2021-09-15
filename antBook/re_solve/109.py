# https://atcoder.jp/contests/abc032/tasks/abc032_c
N,K=list(map(int, input().split()))
S=[]
for _ in range(N):
    tmp = int(input())
    if tmp == 0:
        print(N)
        exit()
    S.append(tmp)
ans = 0
right = 0
sum = 1
for left in range(N):
    while right < N and sum * S[right] <= K:
        sum *= S[right]
        right += 1
    ans = max(ans, right - left)
    if left == right:
        right += 1
    else:
        sum //= S[left]
print(ans)