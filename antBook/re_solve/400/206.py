# https://atcoder.jp/contests/abc009/tasks/abc009_3
N,K=list(map(int, input().split()))
import sys
sys.setrecursionlimit(10**9)
S=input()
s_list =[]
for _s in S:
    s_list.append(_s)
s_list.sort()
used = [False] * (len(s_list))
ans_list = []
def dfs(tmp_str,used,cnt):
    if len(tmp_str) == N:
        ans_list.append("".join(tmp_str))
        return
    for i in range(len(s_list)):
        if used[i]:continue
        used[i] = True
        tmp = tmp_str[:]
        tmp.append(s_list[i])
        if s_list[i] != S[len(tmp_str)]:
            if cnt+1>K:
                used[i]=False
                continue
            dfs(tmp,used,cnt+1)
        else:
            dfs(tmp,used,cnt)
        used[i] = False
for i in range(len(s_list)):
    used[i] = True
    cnt = 0
    if s_list[i] != S[0]:cnt+=1
    dfs([s_list[i]],used,cnt)
    used[i] = False
    if len(ans_list) > 0:
        print(ans_list[0])
        exit()