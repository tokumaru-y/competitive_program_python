X=input().rstrip()
M=int(input())
max_num = int(max(X))
if len(X)==1:
    print(int(M>=max_num))
else:
    left = max_num
    right= 10**18+2
    def is_ok(m):
        tmp_sum = 0
        k = 1
        for x in X[::-1]:
            tmp_sum+=int(x)*k
            if tmp_sum > M:
                return False
            k *= m
        return True
    while right-left>1:
        middle = (right+left)//2
        if is_ok(middle):
            left = middle
        else:
            right= middle
    print(left-max_num)