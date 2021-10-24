# https://atcoder.jp/contests/abc079/tasks/abc079_c
ABCD=list(input())
for bit in range(1<<3):
    tmp = ABCD[0]
    tmp_sum = int(ABCD[0])
    for i in range(3):
        if bit & (1<<i):
            tmp += "+"+ABCD[i+1]
            tmp_sum += int(ABCD[i+1])
        else:
            tmp += "-"+ABCD[i+1]
            tmp_sum -= int(ABCD[i+1])
    if tmp_sum == 7:
        print(tmp+"=7")
        exit()
