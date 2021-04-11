# 難しい
N,K=list(map(int, input().split()))
S=input().rstrip()
ans = ''
al_list = []
for s in S:
    al_list.append(s)
al_list.sort()
used = [False] * N
def check(s,a,left):
    tmp = s
    cnt = K
    for i in range(len(s)):
        if not S[i] == tmp[i]:
            cnt -= 1
    for i in range(len(s)+1,N):
        if S[i] not in left:
            cnt -= 1
    # 文字列作成
    for i in range(N):
        if i <= len(s) - 1:
            if not S[i] == tmp[i]:
                pass


    if cnt < 0:
        return [False, '']
    else:
        return [True, ]

for i in range(N):
    for j in range(N):
        if check(ans+al_list[j],al_list[j],al_list[j+1:]) and not used[j]:
            used[j] = True
            ans += al_list[j]
            break
print(ans)
if len(ans) < N:
    ans += S[len(ans):]
print(ans)