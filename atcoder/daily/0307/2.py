N=int(input())
tak = input().rstrip()
aoki = input().rstrip()
cnt = 0
cards = [N] * 9
for i in range(4):
    t = int(tak[i])-1
    a = int(aoki[i])-1
    cards[t]-=1
    cards[a]-=1
all = 0
for i in range(9):
    for j in range(9):
        if i==j and cards[i] < 2:continue
        if cards[i] == 0 or cards[j]==0:continue
        t_sum = 0
        a_sum = 0
        for k in range(9):
            t_cnt = tak.count(str(k+1))
            if k==i:t_cnt+=1
            a_cnt = aoki.count(str(k+1))
            if k==j:a_cnt+=1
            t_sum+=(k+1)*10**(t_cnt)
            a_sum+=(k+1)*10**(a_cnt)
        if t_sum > a_sum:cnt+=cards[i]*cards[j] if i!=j else cards[i]*(cards[i]-1)
        all+= cards[i]*cards[j] if i!=j else cards[i]*(cards[i]-1)
print(cnt/all)
