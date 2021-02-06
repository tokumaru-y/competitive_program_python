h,w=list(map(int,input().split()))
grid=[input().rstrip() for _ in range(h)]
cnt_table=[[0] * w for _ in range(h)]
cnt_table[0][0]=1

def search(x,y,cnt):
    if x==0 and y==0:
        return cnt_table[x][y]
    nx=x-1 if x-1>=0 else x
    ny=y-1 if y-1>=0 else y
    if nx == x and ny == y:
        return 0
    if nx == x or ny ==y:
        search(nx,ny,cnt+1)
    else:
        search(nx,y,cnt+1)
        search(x,ny,cnt+1)
        search(nx,ny,cnt+1)
