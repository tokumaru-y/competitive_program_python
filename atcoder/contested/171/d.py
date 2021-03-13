N=int(input())
A=list(map(int,input().split()))
Q=int(input())
sum_n= sum(A)
cnt = {}
for a in A:
    if a in cnt:
        cnt[a]+=1
    else:
        cnt[a]=1

for _ in range(Q):
    b,c=list(map(int,input().split()))
    cnt_b=cnt[b] if b in cnt else 0
    if cnt_b != 0:
        cnt_c=cnt[c] if c in cnt else 0
        sum_n -= b * cnt_b
        sum_n += c * (cnt_b)
        cnt[b]=0
        cnt[c]=cnt_b+cnt_c
    print(sum_n)
