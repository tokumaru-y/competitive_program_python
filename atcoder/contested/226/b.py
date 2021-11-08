N=int(input())
ll = []
for _ in range(N):
    inl = input().split()
    inl = inl[1:]
    inl = tuple(inl)
    ll.append(inl)
print(len(list(set(ll))))
