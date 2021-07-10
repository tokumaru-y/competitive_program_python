import string
slist = list(string.ascii_lowercase)
A=input().rstrip()
len = len(A)
if len == 1:
    if A == 'a':
        print(-1)
    else:
        ind = slist.index(A)
        print(slist[ind-1])
else:
    print(A[:len-1])