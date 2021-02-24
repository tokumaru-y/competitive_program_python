import math
N=int(input())
X=list(map(lambda x : abs(int(x)),input().split()))
print(sum(X))
print(math.sqrt(sum(map(lambda x : x**2,X))))
print(max(X))