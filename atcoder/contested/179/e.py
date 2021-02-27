N,X,M=list(map(int,input().split()))
orders = [-1]*M
histories = []
rounds=[]
ans = 0
now = X
for i in range(N):
    if orders[now]!= -1:
        for j in range(orders[now],i):
            rounds.append(histories[j])
        break
    orders[now]= i
    histories.append(now)
    ans+=now
    now = now**2%M
left = N-len(histories)
if left == 0:
    print(ans)
    exit()
add_list=[0]*(len(rounds)+1)
for i in range(len(rounds)):
    add_list[i+1] = add_list[i] + rounds[i]
ans += add_list[len(rounds)] * (left // len(rounds)) + add_list[left%len(rounds)]
print(ans)