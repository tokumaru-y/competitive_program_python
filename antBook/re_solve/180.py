# https://atcoder.jp/contests/arc037/tasks/arc037_c
S=input()
len_s = len(S)
ans = 0
for bit in range(1<<(len_s-1)):
    tmp = S[0]
    for i in range(len_s-1):
        if bit & (1<<i):
            ans += int(tmp)
            tmp = ""
        tmp += S[i+1]
    if len(tmp) > 0:
        ans+=int(tmp)
print(ans)