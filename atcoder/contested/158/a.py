S=input().rstrip()
s = set([x for x in S])
print("No" if len(s) == 1 else "Yes")