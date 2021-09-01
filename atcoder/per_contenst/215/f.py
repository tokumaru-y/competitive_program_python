N=int(input())
XY=[list(map(int, input().split())) for _ in range(N)]
sort_x = sorted(XY, key= lambda x: x[0])
sort_y = sorted(XY, key= lambda x: x[1])
ans = 0
for i in range(N-1):
    x1,x2 = sort_x[i], sort_x[i+1]
    y1,y2 = sort_y[i], sort_y[i+1]
    ans = max(ans, min(abs(x1[0] - x2[0]), abs(x1[1] - x2[1])), min(abs(y1[0] - y2[0]), abs(y1[1] - y2[1])))
print(ans)