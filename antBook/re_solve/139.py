# https://atcoder.jp/contests/joi2013ho/tasks/joi2013ho1
N=int(input())
A=list(map(int, input().split()))
cnt_list = []
pre = -1
cnt = 0
for i in range(N):
    if A[i] != pre:
        cnt+=1
        pre = A[i]
    else:
        cnt_list.append(cnt)
        cnt = 1
if cnt > 0:cnt_list.append(cnt)
ans = 0
if len(cnt_list) == 1:
    ans = cnt_list[0]
elif len(cnt_list) == 2:
    ans = sum(cnt_list)
else:
    for i in range(1,len(cnt_list)-1):
        ans = max(ans, cnt_list[i-1]+cnt_list[i]+cnt_list[i+1])
print(ans)