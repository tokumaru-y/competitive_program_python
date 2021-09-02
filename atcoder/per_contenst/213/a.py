A,B=list(map(int, input().split()))
ans = ""
if B==0:
    ans="Gold"
elif A==0:
    ans="Silver"
else:
    ans="Alloy"
print(ans)