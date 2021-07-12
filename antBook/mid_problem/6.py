N,M=list(map(int, input().split()))
X=[int(input())-1 for _ in range(M)]
left=0
right=10**9
def check(ans):
    checked = 0
    for i in range(M):
        dif = X[i]-checked
        if dif > ans:return False
        if dif <= 0:
            checked=X[i]+ans+1
        else:
            tmp=max(ans+2*checked-X[i]+1, (ans+X[i]+1+checked+1)//2)
            checked=min(checked,tmp)
    return checked>=ans
while right-left > 1:
    mid = (right+left)//2
    if check(mid):
        right=mid
    else:
        left=mid
print(right)