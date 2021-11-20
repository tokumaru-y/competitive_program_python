S,T,X=list(map(int, input().split()))
ans = "No"
if S>T:
    if S<=X or X<T:
        ans ="Yes"
else:
    if S<=X<T:ans="Yes"
print(ans)