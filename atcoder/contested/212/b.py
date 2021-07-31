inl = list(input())
ans = "Strong"
if len(list(set(inl))) == 1:
    ans = "Weak"
else:
    for ind in range(3):
        if inl[ind]=="9" and inl[ind+1] == "0":
            continue
        elif int(inl[ind+1]) - int(inl[ind]) == 1:
            continue
        else:
            break
    else:
        ans = "Weak"
print(ans)