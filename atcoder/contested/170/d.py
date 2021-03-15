N=int(input())
A=list(map(int,input().split()))
MAX_A=10**6
cnt = [0]*(MAX_A+1)
for a in A:
    cnt[a]+=1

for i in range(1,MAX_A+1):
    if cnt[i]==0:continue
    if cnt[i]>1:cnt[i]=0
    for j in range(i*2,MAX_A+1, i):
        cnt[j]=0
ans = 0
for i in range(1,MAX_A+1):
    ans+=cnt[i]
print(ans)