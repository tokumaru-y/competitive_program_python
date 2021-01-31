n,m=list(map(int,input().split()))
if m==0:
    print(1)
    exit(0)
a_list=list(map(int,input().split()))
dif_array=[]
pre = 1
a_list.sort()
for i,a in enumerate(a_list):
    if i==0:
        if a==1:
            continue
        else:
            dif_array.append(a-1)
    else:
        dif_array.append(a-1-pre)
    pre=a
dif_array.sort()
if a_list[-1]!=n:
    dif_array.append(n-pre)
if len(dif_array)==1 and dif_array[0]==0:
    print(0)
else:
    if len(dif_array)==0 or dif_array[-1]==0:
        print(0)
        exit(0)
    dif = next(filter(lambda x : x > 0, dif_array))
    ans = 0 
    # print(dif,dif_array)
    for d in dif_array:
        ans+=(d//dif) if d%dif==0 else (d//dif) + 1
    print(ans)