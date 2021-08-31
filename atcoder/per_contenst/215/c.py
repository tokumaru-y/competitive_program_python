from itertools import permutations
S,K=input().split()
K=int(K)
l = []
for v in permutations(list(S)):
    l.append(v)
l=list(set(l))
l.sort()
ans = "".join(l[K-1])
print(ans)