def power(a,b):
    c = float(a)
    d = int(b)
    if(d == 0):
        print(1)
    elif(d == 1):
        print(c)
    else:
        cnt = float(c)
        for i in range(2, d+1):
            cnt = cnt * c
        print(cnt)

a = input().split()
power(a[0],a[1])