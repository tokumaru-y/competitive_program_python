from collections import deque
n=int(input())
deepth=[0]*n
edge_list=[[] for _ in range(n)]
input_list=[]
num_list=[0]*n
ans=[0]*n
total_num = 0
for _ in range(n):
    a,b=list(map(int,input().split()))
    a-=1
    b-=1
    edge_list[a].append(b)
    edge_list[b].append(a)
    input_list.append([a,b])
q=deque(edge_list[0])
deep_cnt=1
while len(q) > 0:
    n_list=q.pop()
    tmp_list=[]
    for i in n_list:
        if deepth[i] == 0 and i != 0:
            deepth[i]=deep_cnt
            tmp_list.append(edge_list[i])
    q.append(sum(tmp_list,[]))
    deep_cnt+=1

query=int(input())
for _ in range(query):
    t,s,c=list(map(int,input().split()))
    s-=1
    a,b=input_list[s]
    if t==1:
        start=a
        end=b
    else:
        start=b
        end=a
    if deepth[start] < deepth[end]:
        ans[start]+=c
        num_list[start]+=c
        num_list[end]-=c
    else:
        total_num+=c
        ans[end]-=c
        num_list[end]-=c
q=deque()
q.append(edge_list[0])
passed=[False]*n
passed[0] = True
