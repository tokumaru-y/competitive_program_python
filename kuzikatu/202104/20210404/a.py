N=int(input())
A=list(map(int ,input().split()))
cnt=0
for a in A:
    if a%2==1:cnt+=1
print("NO" if cnt%2==1 else "YES")