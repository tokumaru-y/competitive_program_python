from collections import deque
import sys
sys.setrecursionlimit(10**9)
N,M=list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c=input().split()
    a=int(a)-1
    b=int(b)-1
    graph[a].append([b,int(c=='r')])
    graph[b].append([a,int(c=='r')])
