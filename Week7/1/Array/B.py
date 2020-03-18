n = int(input())
b = input().split()

a = []

for i in range(0,n):
    a.append(int(b[i]))

for i in range(0,n):
    if(a[i]%2 == 0):
        print(a[i], sep=" ", end=" ", flush=True)