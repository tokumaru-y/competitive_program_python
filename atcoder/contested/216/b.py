N=int(input())
dict = {}
for _ in range(N):
    inp=input()
    if inp in dict:
        print("Yes")
        exit()
    dict[inp]=1
print("No")