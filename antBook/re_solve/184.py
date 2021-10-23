# https://atcoder.jp/contests/abc002/tasks/abc002_4
N,M=list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(M)]
graph = [[False] * N for _ in range(N)]
for x,y in XY:
    x,y=x-1,y-1
    graph[x][y] = True
    graph[y][x] = True
for i in range(N):
    graph[i][i]=True
ans = 0
for bit in range(1,1<<N):
    member_cnt = 0
    member_list = []
    for i in range(N):
        if bit & (1<<i):
            member_list.append(i)
            member_cnt+=1
    is_correct = True
    for i in range(member_cnt):
        x = member_list[i]
        for j in range(i+1,member_cnt):
            y = member_list[j]
            if not graph[x][y]:is_correct=False
    if is_correct:ans=max(ans,member_cnt)
print(ans)