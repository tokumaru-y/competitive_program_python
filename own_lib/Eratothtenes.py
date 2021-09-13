def Eratosthenes(num):
    """エラトステネスのふるい"""
    res = [True] * (num+1)
    res[0]=False
    res[1]=False
    for i in range(2, num + 1):
        if res[i]:
            k = i+i
            while k <= num:
                res[k]=False
                k+=i
    return res