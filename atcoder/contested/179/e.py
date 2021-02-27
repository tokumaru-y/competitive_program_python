N,X,M=list(map(int,input().split()))
div_list={X:1}
div = [X]
ans = X
pre = X
for i in range(1,N):
    calc = (pre**2)%M
    if calc == 0:
        break
    if calc in div_list:
        left = N-i-1
        ans += sum(div) * (len(div_list)//left)
        if len(div_list) % left != 0:
            ans+=sum(div[:left+1])
        break
    div.append(calc)
    div_list[calc]=1
    ans += calc
    pre = calc
print(ans)