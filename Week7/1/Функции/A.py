def min(a,b,c,d):
    if(a<b):
        if(a<c):
            if(a<d):
                print(a)
            else:
                print(d)
        else:
            if(c<d):
                print(c)
            else:
                print(d)
    else:
        if(b<c):
            if(b<d):
                print(b)
            else:
                print(d)
        else:
            if(c<d):
                print(c)
            else:
                print(d)

a = input().split()
min(a[0],a[1],a[2],a[3])