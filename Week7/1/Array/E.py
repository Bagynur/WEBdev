n = int(input())
b = input().split()
ok = bool(False)

a = []

for i in range(0,n):
    a.append(int(b[i]))

for i in range(1,n):
    if((a[i] < 0 and a[i-1] < 0) or (a[i] > 0 and a[i-1] > 0)):
        ok = True
        break

if(ok):
    print("YES")
else:
    print("NO")