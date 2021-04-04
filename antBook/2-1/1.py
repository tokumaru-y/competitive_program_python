S=input().rstrip()
ans = 0
for bit in range(1<<(len(S)-1)):
    pre = 0
    for i in range(len(S)-1):
        if bit & 1<<i:
            ans += int(S[pre:i+1])
            pre = i+1
    ans += int(S[pre:])
print(ans)