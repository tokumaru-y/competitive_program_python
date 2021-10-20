# https://atcoder.jp/contests/abc085/tasks/abc085_c
N,Y=list(map(int,input().split()))
for s in range(N+1):
    for h in range(N-s+1):
        left = Y - (10**4)*s - (5*10**3)*h
        if left >= 0 and left % 1000 == 0 and s + h + left//1000 == N:
            print(s,h,left//1000)
            exit()
print(-1,-1,-1)