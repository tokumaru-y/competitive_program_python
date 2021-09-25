# https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_c
N,M,H,K=list(map(int, input().split()))
points = [int(input()) for _ in range(N)]
lines = [list(map(int, input().split())) for _ in range(M)]
lines = sorted(lines, key=lambda x:x[1])
scores = points[::]
for line in lines[::-1]:
    line_num = line[0]-1
    scores[line_num], scores[line_num+1] = scores[line_num+1],scores[line_num]
min_dif = 0
now_position = [i+1 for i in range(0, N)]
for line in lines:
    line_num = line[0]-1
    from_left=now_position[line_num]
    from_right=now_position[line_num+1]
    if from_left <= K and from_right > K:
        min_dif = min(min_dif, scores[from_right-1] - scores[from_left-1])
    elif from_left > K and  from_right <= K:
        min_dif = min(min_dif, scores[from_left-1] - scores[from_right-1])
    now_position[line_num], now_position[line_num+1] = now_position[line_num+1], now_position[line_num]
ans = sum(scores[:K]) + min_dif
print(ans)