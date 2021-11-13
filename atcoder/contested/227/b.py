N=int(input())
S=list(map(int, input().split()))
can_list = [False] * 1001
for a in range(1,500):
    for b in range(1,500):
        tmp = 4*a*b + 3*a + 3*b
        if tmp <= 1000:can_list[tmp] = True
ng = 0
for s in S:
    if not can_list[s]:ng+=1
print(ng)