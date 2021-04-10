N=int(input())
AB=[list(map(int, input().split())) for _ in range(N)]
AB.sort()
a,b=AB[-1]
print(a+b)