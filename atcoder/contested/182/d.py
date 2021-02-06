n=int(input())
A = list(map(int,input().split()))
S = [0] * (n+1)
M = [0] * (n+1)
for i in range(n):
    S[i+1]=S[i]+A[i]
    M[i+1]=max(M[i],S[i+1])
now_point=0
ans = 0 
for i in range(n):
    ans = max(ans,now_point+M[i+1])
    now_point+= S[i+1]
print(ans)