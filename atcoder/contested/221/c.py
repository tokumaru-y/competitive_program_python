import itertools
C=list(input())
ans = 0
for l in itertools.permutations(C):
    for i in range(1,len(C)):
        a = l[:i]
        b = l[i:]
        ans = max(ans, int("".join(a)) * int("".join(b)))
print(ans)