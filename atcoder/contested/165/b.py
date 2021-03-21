X = int(input())
now = 100
for i in range(1,10**7):
    now += now//100
    if now >= X:
        print(i)
        exit()