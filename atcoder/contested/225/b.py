N=int(input())
AB=[list(map(int,input().split())) for _ in range(N-1)]
graph = [[] for _ in range(N)]
for a,b in AB:
    a-=1
    b-=1
    graph[a].append(b) 
    graph[b].append(a)
for i in range(N):
    if len(graph[i]) == N-1:
        print("Yes")
        exit()
print("No")