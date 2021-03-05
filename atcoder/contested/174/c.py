K=int(input())
div={}
num=0
cnt=0
while True:
    cnt+=1
    num = (num+7*10**(cnt-1))%K
    if num == 0:
        print(cnt)
        exit()
    if num in div:
        print(-1)
        exit()
    div[num]=1
