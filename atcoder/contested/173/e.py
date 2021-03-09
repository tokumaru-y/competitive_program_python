N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
A.sort()
minus =[]
plus = []
for i in range(A):
    if A[i]>0:
        if i > 0:minus=A[:i]
        plus = A[i:]
plus_div = []
minus_div = []
if len(minus)>=2:
    for i in range(1,len(minus)):
        minus_div.append(minus[i]*minus[i-1])
minus_div.extend(minus)
if len(plus)>=2:
    for i in range(1,len(plus)):
        plus_div.append(plus[i]*plus[i-1])
plus_div.extend(plus)
all_list=[]
all_list.extend(plus_div)
all_list.extend(minus_div)
all_list.sort(reverse=True)
