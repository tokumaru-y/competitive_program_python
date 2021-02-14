import sys
input = sys.stdin.readline
N=int(input())
XY=[list(map(int,input().split()))]
M=int(input())
Ms=[]
for _ in range(M):
    t=list(map(int,input().split()))
    if t[0] == 1 or t[0] == 2:
        Ms.append(t[0])
    else:
        Ms.append([t[0],t[1]])

# 行列計算の知識補填のため、一旦ストップ