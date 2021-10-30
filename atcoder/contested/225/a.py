S=list(input())
ll = []
from itertools import permutations
for l in permutations(S):
    tmp = "".join(l)
    ll.append(tmp)
ll = list(set(ll))
print(len(ll))