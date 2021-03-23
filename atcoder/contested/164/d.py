S=input().rstrip()
ll = len(S)
mod_list = [0]*2019
now = 0
keta = 1
mod_list[now]+=1
for i in range(ll):
    target = int(S[ll-i-1])
    now = (now+target*keta)%2019
    keta = keta*10%2019
    mod_list[now]+=1
ans = 0
for i in range(2019):
    ans += mod_list[i] * (mod_list[i] - 1)//2
print(ans)
