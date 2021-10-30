# https://atcoder.jp/contests/abc007/tasks/abc007_2
A=input()
if len(A)==1:
    import string
    ll = [-1] + list(string.ascii_letters)
    print(ll[ord(A)-96-1])
else:
    print(A[:-1])