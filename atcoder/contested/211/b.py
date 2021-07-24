s = set()
for _ in range(4):
    t = input().rstrip()
    s.add(t)
print("Yes" if len(list(s)) == 4 else "No")