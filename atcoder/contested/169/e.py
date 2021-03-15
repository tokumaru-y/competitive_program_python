N=int(input())
A=[]
B=[]
for _ in range(N):
    a,b=list(map(int,input().split()))
    A.append(a)
    B.append(b)
A.sort()
B.sort()
if N%2==0:
    min_num = A[N//2-1]+A[N//2]
    max_num = B[N//2-1]+B[N//2]
    print(max_num - min_num + 1)
else:
    print(B[N//2] - A[N//2] + 1)