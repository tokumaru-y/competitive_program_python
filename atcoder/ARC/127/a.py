# https://atcoder.jp/contests/arc127/tasks/arc127_a
N=int(input())
ans = 0
for i in range(1,17):
    start = int("1" * i)
    end = min(int("1" * (i-1) + "2"), N+1)
    while start <= N and start < end:
        ans += end - start
        start *= 10
        end = min(end *10 , N+1)
print(ans)