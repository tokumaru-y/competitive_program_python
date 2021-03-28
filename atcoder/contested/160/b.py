N=int(input())
ans = 0
ans += (N//500)*1000
N %=500
ans += (N//5)*5
print(ans)