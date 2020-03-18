def xor(a,b):
    c = int(a)
    d = int(b)
    print((c+d)%2)

a = input().split()
xor(a[0],a[1])