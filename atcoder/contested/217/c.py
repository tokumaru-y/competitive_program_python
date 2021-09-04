N=int(input())
L = list(map(int, input().split()))
ll = [0] * N
for idx, l in enumerate(L):
    ll[l-1]=idx+1
print(*ll)