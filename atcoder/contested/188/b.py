N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
s=0
for i in range(N):
    s+=A[i]*B[i]
print("Yes" if s == 0 else "No")