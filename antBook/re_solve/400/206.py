# https://atcoder.jp/contests/abc009/tasks/abc009_3
import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
N,K=list(map(int, input().split()))
S=input()
cnt_dict= defaultdict(int)
for _s in S:cnt_dict[_s]+=1
ls=len(S)
ans = list(S)
for i in range(ls):
    # i:=ansのi番目の文字について探索
    # now入れ替える予定のindex(0-index)
    now  = i
    for j in range(i+1,ls):
        # j:i番目以降の文字で条件を満たす小さい文字があるか
        if ans[now] > ans[j]:
            tmp_str = ans[:]
            tmp_str[i],tmp_str[j] = tmp_str[j],tmp_str[i]
            dif_cnt = 0
            for _d in range(ls):
                if tmp_str[_d] != S[_d]:dif_cnt+=1
            if dif_cnt<=K:
                now=j
    ans[now],ans[i] = ans[i],ans[now]
print("".join(ans))