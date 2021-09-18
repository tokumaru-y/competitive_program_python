# https://atcoder.jp/contests/joi2013ho/tasks/joi2013ho1
N=int(input())
L=list(map(int, input().split()))
cnt_list = [0]
cnt = 1
pre = L[0]
for i in range(1,N):
    if pre == L[i]:
        cnt_list.append(cnt)
        cnt = 1
    else:
        cnt+=1
        pre=L[i]
cnt_list.append(cnt)
cnt_list.append(0)
ans = 0
for i in range(len(cnt_list)-2):
    ans = max(ans, cnt_list[i]+cnt_list[i+1]+cnt_list[i+2])
print(ans)