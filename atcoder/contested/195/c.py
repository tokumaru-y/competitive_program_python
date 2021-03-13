N=int(input())
ans = 0
# n = 1
# cnt = 0
# while n <=N:
#     ans += (n-(n//(1000**cnt)))*cnt
#     if n * 1000 > N:
#         ans += ()
#     n *= 1000
# st = str(N)
# le=len(st)
# ll = le//3
# if ll % 3 == 0:
#     ll-=1
#     for i in range(ll):
#         ans += 
# elif ll % 3 == 1:
# else:
cnt = 1
n = 1000
while n<=N:
    ans +=cnt + (n-1-((1000**(cnt-1))))*(cnt-1)
    if n*1000 > N:
        ans += (N-n)*(cnt)
    n*=1000
    cnt+=1 
print(ans)
