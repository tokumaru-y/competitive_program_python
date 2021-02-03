import heapq

h,w=list(map(int,input().split()))
grid=[input().rstrip() for _ in range(h)]
h_table={}
checked={}
d_h=[1,0,-1,0]
d_w=[0,1,0,-1]
for h_i in range(h):
    for w_i in range(w):
        target=grid[h_i][w_i]
        if target=='S':
            s_h=h_i
            s_w=w_i
        elif target=='G':
            e_h=h_i
            e_w=w_i
        elif 'a'<=target<='z':
            if target in h_table:
                h_table[target].append([h_i,w_i])
            else:
                h_table[target] = [[h_i,w_i]]
q=[[0,s_h,s_w]]
passed=[[False] * w for _ in range(h)]
passed[s_h][s_w]=True
heapq.heapify(q)
ans = float('inf')
while len(q) > 0:
    nx=heapq.heappop(q)
    cnt,n_h,n_w = nx
    for i in range(4):
        hi=n_h+d_h[i]
        wi=n_w+d_w[i]
        if not(0<=hi<=h-1 and 0<=wi<=w-1) or grid[hi][wi] == '#' or passed[hi][wi]:continue
        passed[hi][wi]=True
        if hi==e_h and wi==e_w:
            ans=min(ans,cnt+1)
            break
        heapq.heappush(q,[cnt+1,hi,wi])
        if grid[hi][wi] != '.' and not grid[hi][wi] in checked:
            checked[grid[hi][wi]]=True
            for ll in h_table[grid[hi][wi]]:
                x,y=ll
                if not passed[x][y]:
                    heapq.heappush(q,[cnt+2,x,y])
                    passed[x][y]=True
print(ans if ans!=float('inf') else -1)
