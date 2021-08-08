N=int(input())
dic = {}
A=list(map(int, input().split()))
for ind, e in enumerate(A):
    dic[e] = ind+1
A.sort(reverse=True)
print(dic[A[1]])