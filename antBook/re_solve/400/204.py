# https://atcoder.jp/contests/abc076/tasks/abc076_c
import sys
sys.setrecursionlimit(10**9)
S=input()
T=input()
len_s=len(S)
len_t=len(T)
ans_list = []
for i in range(len_s-len_t+1):
    if S[i] == T[0] or S[i] == "?":
        for j in range(1,len_t):
            if not(S[i+j] == "?" or S[i+j] == T[j]):break
        else:
            ans = ""
            for m in range(i):ans += S[m] if S[m] != "?" else "a"
            ans += T
            for m in range(i+len_t,len_s):ans += S[m] if S[m] != "?" else "a"
            ans_list.append(ans)
if len(ans_list) == 0:
    print("UNRESTORABLE")
else:
    ans_list.sort()
    print(ans_list[0])