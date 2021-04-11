S=input().rstrip()
T=input().rstrip()
ls = len(S)
ans = 'z'*ls
for i in range(ls):
    if (S[i] == '?' or S[i] == T[0]) and i+len(T)-1 < ls:
        for j in range(1,len(T)):
            if not (S[i+j] == T[j] or S[i+j] == '?'):break
        else:
            tmp = ''
            tmp =  S[:i] + T + S[i+len(T):]
            strtmp = ''
            for t in tmp:
                if t == '?':strtmp += 'a'
                else:strtmp+=t
            ans = min(ans, strtmp)
print(ans if not ans == 'z'*ls else "UNRESTORABLE")
