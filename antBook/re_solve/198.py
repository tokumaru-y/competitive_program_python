# https://yukicoder.me/problems/199
N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
from itertools import permutations
total = 0
ans = 0
for a in permutations(A):
    for b in permutations(B):
        total += 1
        win_cnt = 0
        lose_cnt = 0
        for x,y in zip(a,b):
            if x<y:
                lose_cnt += 1
            elif x>y:
                win_cnt += 1
        if win_cnt > lose_cnt:ans+=1
print(ans/total)