from heapq import heapify,heappop,heappush
N,K=list(map(int, input().split()))
in_list = [[] for _ in range(N)]
IN = []
for _ in range(K):
    inp = input().split()
    if inp[0] == "0":
        a,b=int(inp[1]), int(inp[2])
        a-=1
        b-=1
        graph = [float("inf")] * N
        graph[a]=0
        h = [[0,a]]
        heapify(h)
        while len(h)>0:
            oc,ot=heappop(h)
            for nt,nc in in_list[ot]:
                st = nc+oc
                if graph[nt] <= st:continue
                graph[nt]=st
                heappush(h,[st,nt])
        print(graph[b] if graph[b] != float("inf") else -1)
    else:
        a,b,c = list(map(int, inp[1:]))
        a-=1
        b-=1
        in_list[b].append([a,c])
        in_list[a].append([b,c])
