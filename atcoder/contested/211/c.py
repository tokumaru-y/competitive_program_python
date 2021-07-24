S=input().rstrip()
ls = len(list(S))
dp = [[0] * 8 for _ in range(ls+1)]
# dd = {"c":[], "h":[],"o":[],"k":[],"u":[],"d":[],"a":[],"i":[]}
key_list = ["c","h","o","k","u","d","a","i"]
MOD = 10**9+7
for i in range(ls):
    for j in range(8):
        dp[i+1][j] = dp[i][j]
        if S[i] == key_list[j]:
            if key_list[j] == 'c':
                dp[i+1][j] = dp[i][j]+1
            else:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + dp[i][j])
        dp[i+1][j]%=MOD
print(dp[ls][7]%MOD)
    # if S[i] in key_list:
    #     if S[i] !="c":dp[i+1][key_list.index(S[i])] = dp[i][key_list.index(S[i])]
# ccnt= 0
# hcnt= 0
# ocnt= 0
# kcnt= 0
# ucnt= 0
# dcnt= 0
# acnt= 0
# icnt= 0
# com_cnt = 0
# dd = {"c":[], "h":[],"o":[],"k":[],"u":[],"d":[],"a":[],"i":[]}
# key_list = ["c","h","o","k","u","d","a","i"]
# ans = 0
# ll=0
# for i in range(ls):
#     if S[i] in key_list:
#         dd[S[i]].append(i)
#         if S[i]=='c':ll+=1
# while len(dd['c']) > 0:
#     tmp = dd['c'].pop()
#     tmp_cnt = 1
#     for key,value in dd.items()[1:]:
        
# print(ans)