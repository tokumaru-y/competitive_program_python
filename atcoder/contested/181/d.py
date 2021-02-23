S=input().rstrip()
dic={}
for s in S:
    if int(s) not in dic:
        dic[int(s)]=1
    else:
        dic[int(s)]+=1
ll=[]
for i in range(9):
    if i+1 in dic:
        cnt=min(3,dic[i+1])
        lis=[i+1]*cnt
        ll+=lis
if len(ll)==1:
    print("Yes" if ll[0]==8 else "No")
elif len(ll)==2:
    tmp1=ll[0]*10+ll[1]
    tmp2=ll[1]*10+ll[0]
    if tmp1 % 8==0 or tmp2%8==0:
        print("Yes")
    else:
        print("No")
else:
    for i in range(len(ll)):
        for j in range(len(ll)):
            if i==j:continue
            for k in range(len(ll)):
                if i==k or j==k:continue
                tmp=ll[i]*100+ll[j]*10+ll[k]
                if tmp%8==0:
                    print("Yes")
                    exit()
    print("No")