# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0503
from collections import deque


while True:
    N,M=list(map(int, input().split()))
    if N+M==0:break
    dp = [-1] * (15000000)
    A=[0] + list(map(int,input().split()))[1:]
    B=[0] + list(map(int, input().split()))[1:]
    C=[0] + list(map(int, input().split()))[1:]
    # A->B:1,B->A:2,B->C:3,C->B:4
    que = deque([[A,B,C,0,-1]])
    correct_list = [i for i in range(N+1)]
    while len(que)>0:
        _A,_B,_C,cnt,pre = que.popleft()
        if cnt > M:
            print(-1)
            break
        if _A == correct_list or _C == correct_list:
            print(cnt)
            break
        if _A[-1] > B[-1] and pre != 1:
            que.append([_A[:-1],_B+[_A[-1]],_C[:],cnt+1,1])
        if _B[-1] > _A[-1] and pre != 2:
            que.append([_A+[_B[-1]],_B[:-1],_C[:],cnt+1,2])
        if _B[-1] > _C[-1] and pre != 3:
            que.append([_A[:],_B[:-1],_C+[_B[-1]],cnt+1,3])
        if _C[-1] > _B[-1] and pre != 4:
            que.append([_A[:],_B+[_C[-1]],_C[:-1],cnt+1,4])