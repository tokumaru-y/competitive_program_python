N=int(input())
A=list(map(int,input().split()))
left=A[:(2**N)//2]
right=A[(2**N)//2:]
ans = min(max(left),max(right))
print(A.index(ans)+1)