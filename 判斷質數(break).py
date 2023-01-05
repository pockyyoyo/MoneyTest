for n in range(2, 20):
    for x in range(2, n):
        # 第一次n=2進來時，range不包含2，因此exception
        # 第二次n=3進來時，range為2~3，此時3%2!=0，因此exception
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
