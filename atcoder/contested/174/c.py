K=int(input())
div={}
num=0
cnt=0
while True:
    num = num*10 + 7
    num %= K
    cnt += 1
    if num == 0:
        print(cnt)
        exit()
    if num in div:
        print(-1)
        exit()
    div[num]=1