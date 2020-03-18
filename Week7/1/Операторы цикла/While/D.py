a = int(input())
b = int(1)
ok = bool(False)

while b < a+1:
    if(a == 1 or a == 2):
        ok = bool(True)
        break
    else:
        if (b*2 == a):
            ok = bool(True)
            break
        else:
            b = b * 2

if(ok):
    print("YES")
else:
    print("NO")
