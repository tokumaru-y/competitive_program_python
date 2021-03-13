N=int(input())
A=list(map(int,input().split()))
all_num = 0
for a in A:
    all_num^=a
ans = []
for a in A:
    ans.append(all_num^a)
print(*ans)