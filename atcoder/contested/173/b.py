N=int(input())
dic = {"AC": 0, "WA": 0,"TLE": 0, "RE": 0}
for _ in range(N):
    dic[input().rstrip()]+=1
for k,v in dic.items():
    print("{} x {}".format(k,v))