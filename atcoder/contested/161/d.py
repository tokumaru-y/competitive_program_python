from collections import deque
K=int(input())
q = deque([])
cnt = 0
num_list = ['0','1','2','3','4','5','6','7','8','9']
if K <= 9:
    print(K)
    exit()
for n in num_list[1:]:
    cnt+=1
    q.append(n)
while len(q) != 0:
    n_num = q.popleft()
    for i in range(max(0,int(n_num[-1])-1), min(9,int(n_num[-1])+1)+1):
        nst = str(n_num)+str(i)
        cnt += 1
        if cnt == K:
            print(nst)
            exit()
        else:
            q.append(nst)