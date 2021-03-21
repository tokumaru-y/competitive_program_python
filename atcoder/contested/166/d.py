X=int(input())
for i in range(-500,500+1):
    for j in range(-500,500+1):
        if i**5 - j**5 == X:
            print(i,j)
            exit()