import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n=int(input())
ab=[tuple(map(int,input().split())) for _ in range(n-1)]
q=int(input())
qs=[tuple(map(int,input().split())) for _ in range(q)]

link_list=[[] for _ in range(n)]
for a,b in ab:
    a-=1
    b-=1
    link_list[a].append(b)
    link_list[b].append(a)

deepth=[0]*n
def descive_deepth(top,pre=-1):
    next_list=link_list[top]
    for n_top in next_list:
        if n_top==pre:continue
        deepth[n_top] += deepth[top]+1
        descive_deepth(n_top,top)
descive_deepth(0)

total_cnt=0
ans=[0]*n
for t,e,x in qs:
    e-=1
    a,b=ab[e]
    a-=1
    b-=1
    if t==2:
        a,b=b,a
    if deepth[a] < deepth[b]:
        total_cnt+=x
        ans[b]-=x
    else:
        ans[a]+=x
ans[0]+=total_cnt
def dfs(top,pre=-1):
    next_list=link_list[top]
    for n_top in next_list:
        if n_top == pre:continue
        ans[n_top]+=ans[top]
        dfs(n_top,top)
dfs(0)

print(*ans,sep="\n")
