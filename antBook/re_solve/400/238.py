# https://atcoder.jp/contests/abc002/tasks/abc002_3
a,b,c,d,e,f=list(map(int, input().split()))
ans = abs((a-e) * (d-f) - (c-e) * (b-f))/2
print(ans)