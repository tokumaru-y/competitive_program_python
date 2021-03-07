h,w=list(map(int,input().split()))
m=float('inf')
grid=[list(map(int,input().split())) for _ in range(h)]
s=0
for ll in grid:
    for l in ll:
        m=min(m,l)
        s+=l
print(s - h*w*m)