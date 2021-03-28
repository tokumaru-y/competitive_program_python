N=int(input())
cnt = {}
A=list(map(int ,input().split()))
for a in A:
    if a in cnt:
        cnt[a]+=1
    else:
        cnt[a]=1
com = {}
total = 0
for k,v in cnt.items():
    com[k] = v*(v-1)//2 if v >=2 else 0
    total += com[k]
for a in A:
    if cnt[a]<2:
        print(total)
    else:
        tmp = total - com[a]
        tmp += (cnt[a]-1)*(cnt[a]-2)//2  if cnt[a]>=3 else 0
        print(tmp)
