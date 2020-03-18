n = int(input())
b = input().split()

a = []

for i in range(0,n):
    a.append(int(b[i]))

for i in range(0,n):
    print(a[n-1-i], sep=" ", end=" ", flush=True)