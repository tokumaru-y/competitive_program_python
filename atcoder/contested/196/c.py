N=int(input())
now = 1
leng = 1
ans = 0
while now + now*10**leng <= N:
    ans +=1
    now += 1
    if now == 10**leng:
        leng+=1
print(ans)