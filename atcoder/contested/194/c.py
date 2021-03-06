import sys
input = sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
sum_n=0
tmp=0
for a in A:
    sum_n+=a*a*(N-1)
    tmp+=a
for i in range(N):
    tmp-=A[i]
    sum_n -= 2*A[i]*tmp
print(sum_n)