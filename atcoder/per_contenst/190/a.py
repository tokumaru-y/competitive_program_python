A,B,C=list(map(int,input().split()))
if C ==0:
    dif = A-B
    ans = "Takahashi" if dif > 0 else "Aoki"
else:
    dif = B-A
    ans = "Aoki" if dif > 0 else "Takahashi"
print(ans)