K=int(input())
S=input().rstrip()
T=input().rstrip()
t_sum=0
tt={}
a_sum=0
aa={}
cards={}
total_left = 9*K
for i in range(1,10):
    total = K
    tt=S.count(str(i))
    aa=T.count(str(i))
    left = total-tt-aa
    cards[i]=left
    t_sum+=i*(10**tt)
    a_sum+=i*(10**aa)
    total_left-=tt+aa
al = total_left*(total_left-1)
cnt = 0
for i in range(1,10):
    for j in range(1,10):
        if cards[i] ==0 or cards[j]==0:continue
        if i==j and cards[i] < 2:continue
        tmpa = t_sum
        tmpa -= i*(10**(S.count(str(i))))
        tmpa += i*(10**((S.count(str(i))+1)))
        tmpb = a_sum
        tmpb -= j*(10**(T.count(str(j))))
        tmpb += j*(10**((T.count(str(j))+1)))
        if tmpa > tmpb:
            cnt+=cards[i]*cards[j] if i!=j else cards[i]*(cards[i]-1)

print(cnt/al)
