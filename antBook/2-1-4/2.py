import itertools
N=int(input())
K=int(input())
num = [input().rstrip() for _ in range(N)]
cnt = {}
for l in itertools.permutations(num):
    tmp = ''.join(l[:K]) 
    n=int(tmp)
    if n not in cnt:
        cnt[n]=1
print(len(cnt))