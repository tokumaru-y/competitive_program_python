N=int(input())
S=input().rstrip()
cnt = {"R":0, "G":0, "B":0}
for s in S:
    cnt[s]+=1
ans = cnt["R"] * cnt["G"] * cnt["B"]
for i in range(N):
    for j in range(i+1, N):
        if S[i] == S[j]: continue
        next_ind = 2*j-i
        if next_ind >= N or S[next_ind] == S[i] or S[next_ind] == S[j]:continue
        ans -= 1
print(ans)