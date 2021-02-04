from collections import deque
import sys
input=sys.stdin.readline
h,w=list(map(int,input().split()))
grid=[]
h_table={}
d_h=[1,0,-1,0]
d_w=[0,1,0,-1]
for h_i in range(h):
    ll = input().rstrip()
    grid.append(ll)
    for w_i in range(w):
        target=ll[w_i]
        if target=='S':
            s_h=h_i
            s_w=w_i
        elif target=='G':
            e_h=h_i
            e_w=w_i
        elif 'a'<=target<='z':
            if target in h_table.keys():
                h_table[target].append([h_i,w_i])
            else:
                h_table[target] = [[h_i,w_i]]
q=deque()
cnt_table=[[-1] * w for _ in range(h)]
cnt_table[s_h][s_w]=0
passed = [[False]* w for _ in range(h)]
passed[s_h][s_w]=True
q.append([s_h,s_w])
print(h_table)
ans = float('inf')
while len(q) > 0:
    nx=q.popleft()
    n_h,n_w = nx
    for i in range(4):
        hi=n_h+d_h[i]
        wi=n_w+d_w[i]
        if not(0<=hi<=h-1 and 0<=wi<=w-1) or grid[hi][wi] == '#' or passed[hi][wi]:continue
        cnt_table[hi][wi]=cnt_table[n_h][n_w]+1
        passed[hi][wi]=True
        if hi==e_h and wi==e_w:
            ans=cnt_table[n_h][n_w]+1
            print(ans)
            exit(0)
        q.append([hi,wi])
        if grid[hi][wi] == '.':
            q.append([hi,wi])
            cnt_table[hi][wi] = cnt_table[n_h][n_w]+1
        if grid[hi][wi] in h_table:
            for ll in h_table[grid[hi][wi]]:
                x,y=ll
                if passed[x][y]:continue
                cntt= cnt_table[hi][wi]+1
                q.append([x,y])
                cnt_table[x][y]=cntt
                passed[x][y]=True
            del h_table[grid[hi][wi]]
print(ans if ans!=float('inf') else -1)
