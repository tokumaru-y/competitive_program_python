X=list(input())
ans = False
if len(list(set(X))) == 1:
    ans = False
else:
    for i in range(3):
        if not(X[i]=="9" and X[i+1] == "0" or int(X[i+1]) - int(X[i])== 1):
            ans = True
            break
print("Strong" if ans else "Weak")