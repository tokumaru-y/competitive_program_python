# https://atcoder.jp/contests/arc088/tasks/arc088_b
S=input()
ans = float("inf")
for i in range(1,len(S)):
    if S[i] != S[i-1]:
        ans = min(ans, max(i, len(S)-i))
print(ans if ans != float("inf") else len(S))