import itertools
N=int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i_list = [i for i in range(N)]
total = 0
cnt = 0
for l in itertools.permutations(i_list):
    a_win = 0
    b_win = 0
    for ind, i in enumerate(l):
        if a[i] > b[ind]:a_win+=1
        elif b[ind] > a[i]:b_win+=1
    if a_win > b_win:cnt+=1
    total+=1
print(cnt/total)