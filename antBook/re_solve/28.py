# TODO https://atcoder.jp/contests/abc032/tasks/abc032_d
N,W=list(map(int,input().split()))
VW = [list(map(int, input().split())) for _ in range(N)]
if N<=30:
    half = N//2
    sum_a = []
    sum_b = []
    def serch(list, is_minus=False):
        end = len(list)
        res_list = []
        for bit in range(1<<end):
            tmp_v = 0
            tmp_w = 0
            for i in range(end):
                if bit & 1 << i:
                    value ,weight = list[i]
                    tmp_v += value
                    tmp_w += weight
            if is_minus:
                res_list.append([tmp_w, -tmp_v])
            else:
                res_list.append([tmp_w, tmp_v])
        return sorted(res_list)
    from bisect import bisect_right, bisect_left
    sum_a = serch(VW[:half])
    sum_b = serch(VW[half:], True)
    target_keys = [w for w,_ in sum_b]
    sum_value_b = [float("inf")] * (len(target_keys)+1)
    sum_value_b[0]=0
    for i in range(len(target_keys)):
        sum_value_b[i+1]=min(sum_value_b[i], sum_b[i][1])
    ans = 0
    for weight, value in sum_a:
        left = W - weight+1
        if left < 0:continue
        ind = bisect_right(target_keys, left)
        ans = max(ans, value-sum_value_b[ind])
    print(ans)
else:
    is_w_lower = True
    for value, weight in VW:
        if weight > 10**3:
            is_w_lower = False
    if is_w_lower:
        limit_w = 200*10**3+1
        dp = [0] * limit_w
        for i in range(N):
            value, weight = VW[i]
            for w in reversed(range(limit_w)):
                if w-weight>=0:dp[w] = max(dp[w], dp[w-weight]+value)
        ans = max(dp) if W>=limit_w else max(dp[:W+1])
        print(ans)
    else:
        limit_v = 200*10**3+1
        dp = [float("inf")] * limit_v
        dp[0]=0
        for i in range(N):
            value, weight = VW[i]
            for v in reversed(range(limit_v)):
                if 0<=v-value:dp[v]=min(dp[v], dp[v-value]+weight)
        for i in reversed(range(limit_v)):
            if dp[i] <= W:
                print(i)
                exit()