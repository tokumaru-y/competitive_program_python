K=int(input())
ans = 0
for i in range(1,K+1):
    ans += (i*2+((K//i)-1)*i)*(K//i)//2
print(ans)