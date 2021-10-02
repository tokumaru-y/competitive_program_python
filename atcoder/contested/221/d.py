N=int(input())
AB=[list(map(int, input().split())) for _ in range(N)]
user_list = []
ans = [0] * (2*10**5 + 1)
login_users = 0
for a,b in AB:
    user_list.append([a,1])
    user_list.append([a+b,-1])
user_list.sort()
current_day = user_list[0][0]
origin = 0
idx = 0
len_u = len(user_list)
while idx < len_u:
    add = 0
    while idx < len_u and user_list[idx][0] == current_day:
        add += user_list[idx][1]
        idx+=1
    if idx<len_u:
        origin = current_day
        current_day = user_list[idx][0]
    login_users += add
    ans[login_users] += 1 * (current_day - origin)
print(*ans[1:N+1],sep=" ")