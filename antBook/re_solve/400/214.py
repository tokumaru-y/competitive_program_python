# https://atcoder.jp/contests/abc007/tasks/abc007_4
# Digit Dpの練習
A,B=list(map(int, input().split()))
def count_num(num):
    leng = len(str(num))
    num_str = str(num)
    dp= [[[0] * 2 for _ in range(2)] for _ in range(leng+1)]
    dp[0][0][0]=1
    for i in range(leng):
        n = int(num_str[i])
        for j in range(2):
            for k in range(2):
                for d in range(10 if j else n+1):
                    dp[i+1][j or (d < n)][k or d==4 or d==9] += dp[i][j][k]
    return dp[leng][0][1] + dp[leng][1][1] - 1
print(count_num(B) - count_num(A-1))