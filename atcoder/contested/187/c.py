n=int(input())
h_table = {}
h2_table ={}
inlist = []
for _ in range(n):
    s=input()
    s1= s[1:] if s[0] == "!" else s
    s2= s if s[0] == "!" else "!" + s
    if s[0] == "!":
        h2_table[s]=1
    else:
        h_table[s]=1
    inlist.append(s1)
for i in range(n):
    if h_table.get(inlist[i]) and h2_table.get("!"+inlist[i]):
        print(inlist[i])
        exit(0)
print("satisfiable")