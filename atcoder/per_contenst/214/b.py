N=int(input())
A=list(map(int,input().split()))
d=[]
for i in range(N):
    d.append([A[i],i+1])
d.sort(reverse=True)
print(d[1][1])