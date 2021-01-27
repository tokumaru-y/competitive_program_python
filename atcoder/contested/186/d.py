import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
A.sort()
sum_num=0
for i in range(N):
    sum_num+=i*A[i] - (N-1-i)*A[i]
print(sum_num)