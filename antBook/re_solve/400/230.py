# https://atcoder.jp/contests/arc115/tasks/arc115_a
N,M=list(map(int, input().split()))
S=[input() for _ in range(N)]
cnt_list = [0] * 2
for s in S:
    one_cnt = 0
    for i in range(M):
        if s[i] == "1":one_cnt+=1
    cnt_list[one_cnt%2] += 1
print(cnt_list[0] * cnt_list[1])