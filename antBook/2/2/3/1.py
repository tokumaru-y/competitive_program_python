import copy
import string
S=input().rstrip()
T=input().rstrip()
ll = len(S)
ind_list = []
for i in range(ll):
    if S[i] == '?':
        ind_list.append(i)
def dfs(s, next_index):
    if len(ind_list) == next_index:
        ss = ''.join(s)
        if T in ss:
            print(ss)
            exit()
        return
    tmp = copy.deepcopy(s)
    for i in string.ascii_lowercase:
        tmp[ind_list[next_index]] = i
        dfs(tmp, next_index+1)
dfs(list(S), 0)
print("UNRESTORABLE")